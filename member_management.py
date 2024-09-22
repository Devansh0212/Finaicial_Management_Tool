import pandas as pd

# Load data from Excel with specified engine for .xlsx files
def load_data(file_path):
    members_df = pd.read_excel(file_path, sheet_name='Members', engine='openpyxl')
    attendance_payments_df = pd.read_excel(file_path, sheet_name='Attendance_Payments', engine='openpyxl')
    return members_df, attendance_payments_df


# Sort members by frequency of attendance
def sort_by_attendance(attendance_payments_df):
    attendance_counts = attendance_payments_df.groupby('MemberID')['Attended'].apply(lambda x: (x == 'Yes').sum()).reset_index(name='AttendanceCount')
    return attendance_counts.sort_values(by='AttendanceCount', ascending=False)


# Apply discount based on attendance
def apply_attendance_discounts(attendance_counts, members_df):
    top_attendees = attendance_counts.head(10)
    members_df['Discount'] = members_df['MemberID'].apply(lambda x: 10 if x in top_attendees['MemberID'].values else 0)
    return members_df


# Sort and apply penalties based on payment status
def apply_payment_penalties(attendance_payments_df, members_df):
    payment_status = attendance_payments_df.groupby('MemberID')['Paid'].apply(lambda x: (x == 'No').sum()).reset_index(name='MissedPayments')
    members_df = pd.merge(members_df, payment_status, on='MemberID', how='left')
    members_df['Penalty'] = members_df['MissedPayments'].apply(lambda x: 'Fee' if x > 1 else None)
    return members_df


# Main function to orchestrate the operations
def main(file_path):
    members_df, attendance_payments_df = load_data(file_path)
    
    # Sort by attendance and apply discounts
    attendance_counts = sort_by_attendance(attendance_payments_df)
    members_df = apply_attendance_discounts(attendance_counts, members_df)
    
    # Apply penalties based on payment status
    members_df = apply_payment_penalties(attendance_payments_df, members_df)
    
    # Save updated members data to a new Excel file or sheet
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        members_df.to_excel(writer, sheet_name='Members_Updated', index=False)
        attendance_payments_df.to_excel(writer, sheet_name='Attendance_Payments', index=False)
    
    print("Members data updated and saved to Excel.")


if __name__ == "__main__":
    file_path = 'club_data.xlsx'
    main(file_path)
