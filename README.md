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
