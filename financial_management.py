import pandas as pd
from datetime import datetime

def load_financial_data(file_path):
    """Loads financial data from an Excel file into pandas DataFrames."""
    revenues_df = pd.read_excel(file_path, sheet_name='Revenues', engine='openpyxl')
    expenses_df = pd.read_excel(file_path, sheet_name='Expenses', engine='openpyxl')
    return revenues_df, expenses_df


def aggregate_details(df, current_month):
    aggregated_df = df.groupby(['Month', 'Category']).sum().reset_index()
    detailed_df = pd.pivot_table(aggregated_df, values='Amount', index='Month', columns='Category', fill_value=0).reset_index()
    if 'Advance Member Payments' in detailed_df.columns:
        if current_month in detailed_df['Month'].values:
            detailed_df.loc[detailed_df['Month'] == current_month, 'Members Payments'] += detailed_df.loc[detailed_df['Month'] == current_month, 'Advance Member Payments'].fillna(0)
    detailed_df['Total'] = detailed_df.sum(axis=1, numeric_only=True)
    return detailed_df


def calculate_monthly_profits(revenues_detailed, expenses_detailed):
    rev = revenues_detailed.set_index('Month')['Total'].rename('Total Revenue')
    exp = expenses_detailed.set_index('Month')['Total'].rename('Total Expense')
    profit_df = pd.concat([rev, exp], axis=1).reset_index()
    profit_df['Net Profit'] = profit_df['Total Revenue'] - profit_df['Total Expense']
    return profit_df


def ensure_all_months(df):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    all_months_df = pd.DataFrame(months, columns=['Month'])
    df = pd.merge(all_months_df, df, on="Month", how='outer').fillna(0)
    return df.sort_values(by='Month', key=lambda x: x.map(months.index))


def identify_unpaid_debts(expenses_df):
    max_hall_expenses = expenses_df[expenses_df['Category'] == 'Hall Expenses']['Amount'].max()
    max_coach_payments = expenses_df[expenses_df['Category'] == 'Coach Payments']['Amount'].max()
    relevant_expenses = expenses_df[expenses_df['Category'].isin(['Hall Expenses', 'Coach Payments'])].copy()
    relevant_expenses['Expected'] = relevant_expenses['Category'].apply(lambda x: max_hall_expenses if x == 'Hall Expenses' else max_coach_payments)
    relevant_expenses['Unpaid'] = relevant_expenses['Expected'] - relevant_expenses['Amount']
    high_urgency_threshold = 1000
    medium_urgency_threshold = 500
    relevant_expenses['Urgency'] = relevant_expenses['Unpaid'].apply(lambda x: 'High' if x > high_urgency_threshold else ('Medium' if x > medium_urgency_threshold else 'Low'))
    unpaid_debts = relevant_expenses[relevant_expenses['Unpaid'] > 0]
    return unpaid_debts[['Month', 'Category', 'Unpaid', 'Urgency']]


def prepare_income_statement(file_path):
    revenues_df, expenses_df = load_financial_data(file_path)
    current_month = datetime.now().strftime('%B')
    revenues_detailed = aggregate_details(revenues_df, current_month)
    expenses_detailed = aggregate_details(expenses_df, current_month)
    profits_df = calculate_monthly_profits(revenues_detailed, expenses_detailed)
    profits_df = ensure_all_months(profits_df)
    return profits_df, revenues_detailed, expenses_detailed, expenses_df 


def save_detailed_to_excel(dfs, sheet_names, file_path):
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        for df, sheet_name in zip(dfs, sheet_names):
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Detailed financial reports have been saved to Excel.")


def save_financial_reports(profits_df, revenues_detailed, expenses_detailed, unpaid_debts_log, file_path):
    dfs = [profits_df, revenues_detailed, expenses_detailed, unpaid_debts_log]
    sheet_names = ['Monthly Profits', 'Detailed Revenues', 'Detailed Expenses', 'Unpaid Debts Log']
    save_detailed_to_excel(dfs, sheet_names, file_path)


if __name__ == "__main__":
    file_path = 'club_finances.xlsx'
    profits_df, revenues_detailed, expenses_detailed, expenses_df = prepare_income_statement(file_path)  # Now includes expenses_df
    unpaid_debts_log = identify_unpaid_debts(expenses_df)
    save_financial_reports(profits_df, revenues_detailed, expenses_detailed, unpaid_debts_log, file_path)
    print("Financial reports and unpaid debts have been processed and saved.")
