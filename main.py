import pandas as pd
from datetime import datetime
from financial_management import (
    aggregate_details, calculate_monthly_profits, 
    identify_unpaid_debts, save_detailed_to_excel, load_financial_data
)


def save_to_excel(accounts_df, file_path):
    accounts_df.to_excel(file_path, index=False)
    print("Excel file has been updated.")


def load_data(file_path):
    return pd.read_excel(file_path)


def create_account(accounts_df, excel_file_path):
    print("Creating a new account.")
    first_name = input("Enter first name: ").strip()
    while first_name == '':
        first_name = input("First name cannot be empty. Please Re-Enter: ").strip()
    
    last_name = input("Enter last name: ").strip()
    while last_name == '':
        last_name = input("Last name cannot be empty. Please Re-Enter: ").strip()

    email = input("Enter email: ").strip()
    while email == '' or email.find("@")==-1 or (not accounts_df[(accounts_df['Email'] == email)].empty):
        email= input("Invalid email. Please Re-Enter: ").strip()

    username = input("Choose a username: ").strip()
    while username == '' or (not accounts_df[(accounts_df['Username'] == username)].empty):
        username = input("Invalid Username. Please Re-Enter: ").strip()


    password = input("Choose a password. Password must be at least 6 characters: ").strip()
    while len(password) < 6:
        password= input("Invalid password. Please Re-Enter: ").strip()

    perms = ""
    status = input("Are you a Member (1) or Coach (2)?\nInput your role as a number: ")
    # Check if statis is valid
    while(status != "1" and status != "2"):   
        print("Invalid Status.\n")
        status = input("Are you a Member (1) or Coach (2)?\nInput your role as a number: ")

    if status == "1":
        perms = "Member"
    elif status == "2":
        perms = "Coach"

    if accounts_df[(accounts_df['Email'] == email) | (accounts_df['Username'] == username)].empty:
        new_account_df = pd.DataFrame([{
            'First Name': first_name.title(), 'Last Name': last_name.title(),
            'Email': email, 'Username': username, 'Password': password,
            'Permissions': perms
        }])
        accounts_df = pd.concat([accounts_df, new_account_df], ignore_index=True)
        save_to_excel(accounts_df, excel_file_path)
        print("\033c", end="")
        print("Account created successfully.")
        return True
    else:
        print("Account Creation Failed.")
        return None # Return None to indicate failed account creation


def remove_account(accounts_df, excel_file_path):
    username = input("Enter the username of the account to remove: ").strip()
    if accounts_df[accounts_df['Username'] == username].empty:
        print("No account found with that username.")
    else:
        accounts_df = accounts_df[accounts_df['Username'] != username]
        save_to_excel(accounts_df, excel_file_path)
        print(f"Account {username} has been removed.")


def login(accounts_df):
    attempts = 0
    while attempts < 4:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        user = accounts_df[(accounts_df['Username'] == username) & (accounts_df['Password'] == password)]
        if not user.empty:
            print("\033c", end="")
            print("Login successful.")
            return user['Permissions'].iloc[0]
        else:
            attempts += 1
            print("Login failed. Incorrect username or password.")
    
    print("\033c", end="")
    print("Too many login attempts. Closing the app.")
    quit()


def treasurer_menu():
    while True:
        print('''
Welcome, Treasurer. What would you like to do:
1) View Financial Reports.
2) Manage Financial Details.
3) Log Out.
0) Quit.
        ''')
        option = input("> ")
        if option == "0":
            print("\033c", end="")
            print("Goodbye, Treasurer.")
            quit()
        elif option == "1":
            print("\033c", end="")
            view_financial_reports()
        elif option == "2":
            print("\033c", end="")
            manage_financial_details()
        elif option == "3":
            print("\033c", end="")
            print("Logging out...")
            break
        else:
            print("\033c", end="")
            print("Invalid option, please try again.\n")


def view_financial_reports():
    print("\033c", end="")
    file_path = 'club_finances.xlsx'
    revenues_df, expenses_df = load_financial_data(file_path)
    current_month = datetime.now().strftime('%B')

    revenues_detailed = aggregate_details(revenues_df, current_month)
    revenue_string = revenues_detailed.to_string()
    print("DETAILED REVENUE: \n", revenue_string)

    expenses_detailed = aggregate_details(expenses_df, current_month)
    expenses_string = expenses_detailed.to_string()
    print("\nDETAILED EXPENSES: \n", expenses_string)

    profits_df = calculate_monthly_profits(revenues_detailed, expenses_detailed)
    print("\nNET PROFITS: \n", profits_df)


def manage_financial_details():
    print("\033c", end="")
    file_path = 'club_finances.xlsx'
    _, expenses_df = load_financial_data(file_path)
    unpaid_debts_log = identify_unpaid_debts(expenses_df)
    print("\nUNPAID DEBTS:\n", unpaid_debts_log, "\n") 
    save_detailed_to_excel([unpaid_debts_log], ['Unpaid Debts Log'], file_path)


def handle_user_permissions(user_perms):
    if user_perms.lower() == "member":
        print("Welcome, Member!") # Just prints this and quits the app. Replace with member menu later.
        quit()
    elif user_perms.lower() == "coach":
        print("Welcome, Coach!") # Just prints this and quits the app. Replace with coach menu later.
        quit()
    elif user_perms.lower() == "treasurer":
        treasurer_menu()


def main():
    user_perms = False
    while (user_perms == False):
        file_path = 'accounts.xlsx'
        accounts_df = load_data(file_path)
        user_action = input("Do you want to (1) Login, (2) Create Account, or (3) Quit?\n> ")

        if user_action == "1":
            user_perms = login(accounts_df)
            if user_perms:
                handle_user_permissions(user_perms)

        elif user_action == "2":
            if create_account(accounts_df, file_path):
                print("You may now login with your new account.")

        elif user_action == "3":
            print("\033c", end="")
            print("Goodbye, User.")
            quit()

        else:
            print("\033c", end="")
            print("Invalid selection. Please try again.\n")

        # if this is reached, it means the user logged out without quitting the app. Therefore, the loop continues.
        # Only way to end the loop is to quit the app, which runs the 'quit()' command
        user_perms = False;

if __name__ == "__main__":
    main()
