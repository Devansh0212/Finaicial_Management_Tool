# Club Financial Management System

This project is a comprehensive Club Management System designed to handle various aspects of club operations, including financial management, member management, and user account management. The system is implemented in Python using Pandas for data manipulation and Excel for data storage.

## Features

### Financial Management
- **Load Financial Data:** Load revenues and expenses from Excel sheets.
- **Aggregate Financial Details:** Aggregate and summarize financial data by month and category.
- **Calculate Monthly Profits:** Compute net profit by subtracting total expenses from total revenues for each month.
- **Identify Unpaid Debts:** Identify and categorize unpaid debts by urgency based on predefined thresholds.
- **Save Financial Reports:** Save detailed financial reports and unpaid debts log to Excel.

### Member Management
- **Load Member Data:** Load member information and attendance/payment records from Excel sheets.
- **Sort by Attendance:** Sort members by the frequency of attendance.
- **Apply Discounts and Penalties:** Apply discounts for top attendees and penalties for missed payments.
- **Save Updated Data:** Save updated member information to Excel.

### User Account Management
- **Account Creation:** Create new user accounts with roles such as Member or Coach.
- **Login System:** Authenticate users based on their credentials.
- **Role-Based Access:** Provide access to different functionalities based on the user's role (e.g., Treasurer, Member, Coach).
- **Treasurer Menu:** Exclusive access for treasurers to view financial reports and manage financial details.

## File Structure

- **financial_management.py:** Handles all financial operations, including loading data, calculating profits, and identifying unpaid debts.
- **member_management.py:** Manages member data, including attendance tracking, discount application, and penalty imposition.
- **main.py:** The main entry point for the application, including user account management and role-based access control.
- **club_finances.xlsx:** Excel file containing financial data, including revenues and expenses.
- **club_data.xlsx:** Excel file containing member data and attendance/payment records.
- **accounts.xlsx:** Excel file containing user account information.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/club-management-system.git
   cd club-management-system
   
2.	**Install dependencies:** Ensure you have Python 3.x installed, and install the necessary packages:
	pip install pandas openpyxl

3. **Prepare Excel Files:**
	•	club_finances.xlsx should include sheets named Revenues and Expenses.
	•	club_data.xlsx should include sheets named Members and Attendance_Payments.
	•	accounts.xlsx should have user account data.
4.	**Run the Application:** Start the system by running the main script:
   python main.py

### Usage

## Financial Management

	•	The treasurer can view detailed financial reports and manage unpaid debts through the treasurer menu in the application.

## Member Management

	•	Member and attendance data are managed automatically by the system. The system applies discounts and penalties based on attendance and payment records.

## User Account Management

	•	Users can create accounts, log in, and access features based on their role (Member, Coach, or Treasurer).

### Suggested Workflow

## 1.	Login/Account Management:
	•	Run the main.py script.
	•	Use existing credentials from the accounts data to log in as a Treasurer, Coach, or Member. For example:
	•	Treasurer: Username - goldAdam2000, Password - AdamAu09!
	•	Coach: Username - IsleAmy45, Password - 416614AI*
	•	Member: Username - dSteele416, Password - Steele1998#
## 2.	Managing Financial Details (Treasurer):
	•	Log in as the Treasurer (goldAdam2000).
	•	View detailed financial reports, including revenues, expenses, and profits.
	•	Manage unpaid debts using the manage_financial_details() function in the financial_management.py.
## 3. Managing Member Data (Coach):
	•	Log in as a Coach (IsleAmy45).
	•	The script would typically greet the user and present options related to member management (e.g., applying discounts based on attendance).
## 4.	Running Financial and Member Operations:
	•	Run financial_management.py to generate and save detailed financial reports to club_finances.xlsx.
	•	Run member_management.py to apply attendance-based discounts or payment penalties, saving updates to club_data.xlsx.

### Future Enhancements

	•	Web-based UI: A future version could include a web-based interface for easier access and management.
	•	Notifications: Integrating email or SMS notifications for unpaid debts or upcoming events.
	•	Advanced Reporting: Additional financial and attendance reports with visualizations.
