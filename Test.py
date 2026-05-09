import streamlit as st
from datetime import datetime
import pandas as pd
import mysql.connector
from decimal import Decimal

#=================== Connect to MySQL ====================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aarthiba@123",
    database="banksight"
)
cursor = conn.cursor()

#============= Data Loading & Preprocessing ==============

customers = pd.read_sql("SELECT * FROM customers", conn)
accounts = pd.read_sql("SELECT * FROM accounts", conn)
transactions = pd.read_sql("SELECT * FROM transactions", conn)
loans = pd.read_sql("SELECT * FROM loans", conn)
credit_cards = pd.read_sql("SELECT * FROM credit_cards", conn)
branches = pd.read_sql("SELECT * FROM branches", conn)
support_tickets = pd.read_sql("SELECT * FROM support_tickets", conn)

customers['join_date'] = pd.to_datetime(customers['join_date'], errors='coerce')
accounts['last_updated'] = pd.to_datetime(accounts['last_updated'], errors='coerce')
transactions['txn_time'] = pd.to_datetime(transactions['txn_time'], errors='coerce')
loans['start_date'] = pd.to_datetime(loans['start_date'], errors='coerce')
loans['end_date'] = pd.to_datetime(loans['end_date'], errors='coerce')
credit_cards['issued_date'] = pd.to_datetime(credit_cards['issued_date'], errors='coerce')
credit_cards['expiry_date'] = pd.to_datetime(credit_cards['expiry_date'], errors='coerce')
branches['opening_date'] = pd.to_datetime(branches['opening_date'], errors='coerce')
support_tickets['date_opened'] = pd.to_datetime(support_tickets['date_opened'], errors='coerce')
support_tickets['date_closed'] = pd.to_datetime(support_tickets['date_closed'], errors='coerce')

#================= Sidebar Navigation ====================

st.sidebar.title("📚 BankSight Navigation")
option = st.sidebar.radio(
    "Go to:",
    [
        "🏠 Introduction",
        "📊 View Tables",
        "🔍 Filter Data",
        "✏️ CRUD Operations",
        "💰 Credit/Debit Simulation",
        "🧠 Analytical Insights",
        "👩‍💻 About Creator"
    ]
)

#================== Introduction ========================

if option == "🏠 Introduction":

    st.title("🏦 BankSight: Transaction Intelligence Dashboard")

    st.subheader("Project Overview")

    st.write("""BankSight is a financial analytics system built using Python, Streamlit, and SQLite3. It allows users to explore customer, account,
              transaction, loan, and support data, perform CRUD operations, simulate deposits/withdrawals, and view analytical insights.""")

    st.subheader("Objectives:")

    st.markdown("""
- Understand customer & transaction behavior 
- Detect anomalies and potential fraud  
- Evaluate branch and account performance  
- Provide interactive data exploration  
""")
    
# =================== VIEW TABLES ===================

elif option == "📊 View Tables":

    st.subheader("📊 View Database Table")

    table_option = st.selectbox(
        "Select a Table",
        [
            "customers", "accounts", "transactions",
            "loans", "credit_cards", "branches", "support_tickets"
        ]
    )

    df = pd.read_sql(f"SELECT * FROM {table_option}", conn)
    st.dataframe(df)

# ================== FILTER DATA ==================
elif option == "🔍 Filter Data":

    st.subheader("🔍 Filter Data")

    table_option = st.selectbox(
        "Select Table to Filter",
        ["customers", "accounts", "transactions", "loans",
         "credit_cards", "branches", "support_tickets"]
    )

    # ------------------ CUSTOMERS ------------------

    if table_option == "customers":

        df = pd.read_sql("SELECT * FROM customers", conn)

        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        name = st.multiselect("Name", df['name'].unique())
        gender = st.multiselect("Gender", df['gender'].unique())
        age = st.multiselect("Age", df['age'].unique())
        city = st.multiselect("City", df['city'].unique())
        account_type = st.multiselect("Account Type", df['account_type'].unique())
        join_date = st.multiselect("Join Date", df['join_date'].unique())

        if customer_id or name or gender or age or city or account_type or join_date:

            filtered_df = df.copy()

            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if name: filtered_df = filtered_df[filtered_df['name'].isin(name)]
            if gender: filtered_df = filtered_df[filtered_df['gender'].isin(gender)]
            if age: filtered_df = filtered_df[filtered_df['age'].isin(age)]
            if city: filtered_df = filtered_df[filtered_df['city'].isin(city)]
            if account_type: filtered_df = filtered_df[filtered_df['account_type'].isin(account_type)]
            if join_date: filtered_df = filtered_df[filtered_df['join_date'].isin(join_date)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ ACCOUNTS ------------------

    elif table_option == "accounts":

        df = pd.read_sql("SELECT * FROM accounts", conn)

        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        account_balance = st.multiselect("Account Balance", df['account_balance'].unique())
        last_updated = st.multiselect("Last Updated", df['last_updated'].unique())

        if customer_id or account_balance or last_updated:

            filtered_df = df.copy()

            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if account_balance: filtered_df = filtered_df[filtered_df['account_balance'].isin(account_balance)]
            if last_updated: filtered_df = filtered_df[filtered_df['last_updated'].isin(last_updated)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ TRANSACTIONS ------------------

    elif table_option == "transactions":

        df = pd.read_sql("SELECT * FROM transactions", conn)

        txn_id = st.multiselect("Transaction ID", df['txn_id'].unique())
        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        txn_type = st.multiselect("Transaction Type", df['txn_type'].unique())
        amount = st.multiselect("Amount", df['amount'].unique())
        txn_time = st.multiselect("Transaction Time", df['txn_time'].unique())
        status = st.multiselect("Status", df['status'].unique())

        if txn_id or customer_id or txn_type or amount or txn_time or status:

            filtered_df = df.copy()

            if txn_id: filtered_df = filtered_df[filtered_df['txn_id'].isin(txn_id)]
            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if txn_type: filtered_df = filtered_df[filtered_df['txn_type'].isin(txn_type)]
            if amount: filtered_df = filtered_df[filtered_df['amount'].isin(amount)]
            if txn_time: filtered_df = filtered_df[filtered_df['txn_time'].isin(txn_time)]
            if status: filtered_df = filtered_df[filtered_df['status'].isin(status)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ LOANS ------------------

    elif table_option == "loans":

        df = pd.read_sql("SELECT * FROM loans", conn)

        loan_id = st.multiselect("Loan ID", df['loan_id'].unique())
        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        account_id = st.multiselect("Account ID", df['account_id'].unique())
        branch = st.multiselect("Branch", df['branch'].unique())
        loan_type = st.multiselect("Loan Type", df['loan_type'].unique())
        loan_amount = st.multiselect("Loan Amount", df['loan_amount'].unique())
        interest_rate = st.multiselect("Interest Rate", df['interest_rate'].unique())
        loan_term_months = st.multiselect("Loan Term Months", df['loan_term_months'].unique())
        start_date = st.multiselect("Start Date", df['start_date'].unique())
        end_date = st.multiselect("End Date", df['end_date'].unique())
        loan_status = st.multiselect("Loan Status", df['loan_status'].unique())

        if loan_id or customer_id or account_id or branch or loan_type or loan_amount or interest_rate or loan_term_months or start_date or end_date or loan_status:

            filtered_df = df.copy()

            if loan_id: filtered_df = filtered_df[filtered_df['loan_id'].isin(loan_id)]
            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if account_id: filtered_df = filtered_df[filtered_df['account_id'].isin(account_id)]
            if branch: filtered_df = filtered_df[filtered_df['branch'].isin(branch)]
            if loan_type: filtered_df = filtered_df[filtered_df['loan_type'].isin(loan_type)]
            if loan_amount: filtered_df = filtered_df[filtered_df['loan_amount'].isin(loan_amount)]
            if interest_rate: filtered_df = filtered_df[filtered_df['interest_rate'].isin(interest_rate)]
            if loan_term_months: filtered_df = filtered_df[filtered_df['loan_term_months'].isin(loan_term_months)]
            if start_date: filtered_df = filtered_df[filtered_df['start_date'].isin(start_date)]
            if end_date: filtered_df = filtered_df[filtered_df['end_date'].isin(end_date)]
            if loan_status: filtered_df = filtered_df[filtered_df['loan_status'].isin(loan_status)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ CREDIT CARDS ------------------

    elif table_option == "credit_cards":

        df = pd.read_sql("SELECT * FROM credit_cards", conn)

        card_id = st.multiselect("Card ID", df['card_id'].unique())
        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        account_id = st.multiselect("Account ID", df['account_id'].unique())
        branch = st.multiselect("Branch", df['branch'].unique())
        card_type = st.multiselect("Card Type", df['card_type'].unique())
        card_network = st.multiselect("Card Network", df['card_network'].unique())
        credit_limit = st.multiselect("Credit Limit", df['credit_limit'].unique())
        current_balance = st.multiselect("Current Balance", df['current_balance'].unique())
        status = st.multiselect("Status", df['status'].unique())

        if card_id or customer_id or account_id or branch or card_type or card_network or credit_limit or current_balance or status:

            filtered_df = df.copy()

            if card_id: filtered_df = filtered_df[filtered_df['card_id'].isin(card_id)]
            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if account_id: filtered_df = filtered_df[filtered_df['account_id'].isin(account_id)]
            if branch: filtered_df = filtered_df[filtered_df['branch'].isin(branch)]
            if card_type: filtered_df = filtered_df[filtered_df['card_type'].isin(card_type)]
            if card_network: filtered_df = filtered_df[filtered_df['card_network'].isin(card_network)]
            if credit_limit: filtered_df = filtered_df[filtered_df['credit_limit'].isin(credit_limit)]
            if current_balance: filtered_df = filtered_df[filtered_df['current_balance'].isin(current_balance)]
            if status: filtered_df = filtered_df[filtered_df['status'].isin(status)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ BRANCHES ------------------

    elif table_option == "branches":

        df = pd.read_sql("SELECT * FROM branches", conn)

        branch_id = st.multiselect("Branch ID", df['branch_id'].unique())
        branch_name = st.multiselect("Branch Name", df['branch_name'].unique())
        city = st.multiselect("City", df['city'].unique())
        manager_name = st.multiselect("Manager Name", df['manager_name'].unique())
        total_employees = st.multiselect("Total Employees", df['total_employees'].unique())
        branch_revenue = st.multiselect("Branch Revenue", df['branch_revenue'].unique())
        opening_date = st.multiselect("Opening Date", df['opening_date'].unique())
        performance_rating = st.multiselect("Performance Rating", df['performance_rating'].unique())

        if branch_id or branch_name or city or manager_name or total_employees or branch_revenue or opening_date or performance_rating:

            filtered_df = df.copy()

            if branch_id: filtered_df = filtered_df[filtered_df['branch_id'].isin(branch_id)]
            if branch_name: filtered_df = filtered_df[filtered_df['branch_name'].isin(branch_name)]
            if city: filtered_df = filtered_df[filtered_df['city'].isin(city)]
            if manager_name: filtered_df = filtered_df[filtered_df['manager_name'].isin(manager_name)]
            if total_employees: filtered_df = filtered_df[filtered_df['total_employees'].isin(total_employees)]
            if branch_revenue: filtered_df = filtered_df[filtered_df['branch_revenue'].isin(branch_revenue)]
            if opening_date: filtered_df = filtered_df[filtered_df['opening_date'].isin(opening_date)]
            if performance_rating: filtered_df = filtered_df[filtered_df['performance_rating'].isin(performance_rating)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

    # ------------------ SUPPORT TICKETS ------------------

    elif table_option == "support_tickets":

        df = pd.read_sql("SELECT * FROM support_tickets", conn)

        ticket_id = st.multiselect("Ticket ID", df['ticket_id'].unique())
        customer_id = st.multiselect("Customer ID", df['customer_id'].unique())
        account_id = st.multiselect("Account ID", df['account_id'].unique())
        loan_id = st.multiselect("Loan ID", df['loan_id'].unique())
        branch_name = st.multiselect("Branch Name", df['branch_name'].unique())
        issue_category = st.multiselect("Issue Category", df['issue_category'].unique())
        priority = st.multiselect("Priority", df['priority'].unique())
        status = st.multiselect("Status", df['status'].unique())
        support_agent = st.multiselect("Support Agent", df['support_agent'].unique())
        channel = st.multiselect("Channel", df['channel'].unique())
        customer_rating = st.multiselect("Customer Rating", df['customer_rating'].unique())

        if ticket_id or customer_id or account_id or loan_id or branch_name or issue_category or priority or status or support_agent or channel or customer_rating:

            filtered_df = df.copy()

            if ticket_id: filtered_df = filtered_df[filtered_df['ticket_id'].isin(ticket_id)]
            if customer_id: filtered_df = filtered_df[filtered_df['customer_id'].isin(customer_id)]
            if account_id: filtered_df = filtered_df[filtered_df['account_id'].isin(account_id)]
            if loan_id: filtered_df = filtered_df[filtered_df['loan_id'].isin(loan_id)]
            if branch_name: filtered_df = filtered_df[filtered_df['branch_name'].isin(branch_name)]
            if issue_category: filtered_df = filtered_df[filtered_df['issue_category'].isin(issue_category)]
            if priority: filtered_df = filtered_df[filtered_df['priority'].isin(priority)]
            if status: filtered_df = filtered_df[filtered_df['status'].isin(status)]
            if support_agent: filtered_df = filtered_df[filtered_df['support_agent'].isin(support_agent)]
            if channel:filtered_df = filtered_df[filtered_df['channel'].isin(channel)]
            if customer_rating:filtered_df = filtered_df[filtered_df['customer_rating'].isin(customer_rating)]

            st.success("Data filtered Successfully!")

            st.dataframe(filtered_df)

# =================== CRUD OPERATIONS ==============

elif option == "✏️ CRUD Operations":

    st.subheader("✏️ CRUD Operations")

    table_option = st.selectbox(
        "Select a Table",
        ["customers", "accounts", "transactions", "loans",
         "credit_cards", "branches", "support_tickets"]
    )

    operation = st.radio(
        "Select Operation",
        ["View", "Add", "Update", "Delete"]
    )

    # ================= VIEW =================
    if operation == "View":
        df = pd.read_sql(f"SELECT * FROM {table_option}", conn)
        st.dataframe(df)

    # ================= ADD =================
    elif operation == "Add":

        st.subheader(f"➕ Add New Record to {table_option}")

        # ----------- CUSTOMERS --------------

        if table_option == "customers":
            customer_id = st.text_input("Customer ID")
            name = st.text_input("Name")
            gender = st.selectbox("Gender", ["M", "F"])
            age = st.number_input("Age", min_value=18)
            city = st.text_input("City")
            account_type = st.selectbox("Account Type", ["Savings", "Current"])
            join_date = st.date_input("Join Date")

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO customers
                    (customer_id, name, gender, age, city, account_type, join_date)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (customer_id, name, gender, age, city, account_type, join_date))
                conn.commit()
                st.success("✅ Customer Added")

        # ---------- ACCOUNTS ----------

        if table_option == "accounts":
            customer_id = st.text_input("Customer ID")
            account_balance = st.number_input("Account Balance", min_value=0.0)
            last_updated = st.date_input("Last Updated")

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO accounts
                    (customer_id, account_balance, last_updated)
                    VALUES (%s,%s,%s)
                """, (customer_id, account_balance, last_updated))
                conn.commit()
                st.success("✅ Account Added")

        # ---------- TRANSACTIONS ----------

        if table_option == "transactions":
            txn_id = st.text_input("Transaction ID")
            customer_id = st.text_input("Customer ID")
            txn_type = st.selectbox(
                "Transaction Type",
                ["deposit", "withdrawal", "transfer", "online fraud", "purchase"]
            )
            amount = st.number_input("Amount", min_value=0.0)
            txn_datetime = st.datetime_input("Transaction Date & Time", value=datetime.now())
            status = st.selectbox("Status", ["success", "failed"])

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO transactions
                    (txn_id, customer_id, txn_type, amount, txn_datetime, status)
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (txn_id, customer_id, txn_type, amount, txn_datetime, status))
                conn.commit()
                st.success("✅ Transaction Added")

        # ---------- LOANS ----------

        if table_option == "loans":
            loan_id = st.text_input("Loan ID")
            customer_id = st.text_input("Customer ID")
            account_id = st.text_input("Account ID")
            branch = st.text_input("Branch")
            loan_type = st.selectbox("Loan Type", ["Personal", "Business", "Home", "Auto", "Education"])
            loan_amount = st.number_input("Loan Amount", min_value=0.0)
            interest_rate = st.number_input("Interest Rate", min_value=0.0)
            loan_term = st.number_input("Loan Term (Months)", min_value=1)
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            loan_status = st.selectbox("Loan Status", ["Active", "Closed", "Approved", "Defaulted"])

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO loans
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (loan_id, customer_id, account_id, branch, loan_type,
                      loan_amount, interest_rate, loan_term,
                      start_date, end_date, loan_status))
                conn.commit()
                st.success("✅ Loan Added")

        # ---------- CREDIT CARDS ----------

        if table_option == "credit_cards":
            card_id = st.text_input("Card ID")
            customer_id = st.text_input("Customer ID")
            account_id = st.text_input("Account ID")
            branch = st.text_input("Branch")
            card_number = st.text_input("Card Number")
            card_type = st.selectbox("Card Type", ["Business", "Platinum", "Gold", "Silver"])
            card_network = st.selectbox("Card Network", ["Visa", "RuPay", "Amex", "MasterCard"])
            credit_limit = st.number_input("Credit Limit", min_value=0.0)
            current_balance = st.number_input("Current Balance", min_value=0.0)
            issued_date = st.date_input("Issued Date")
            expiry_date = st.date_input("Expiry Date")
            status = st.selectbox("Status", ["Active", "Expired", "Blocked"])

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO credit_cards
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (card_id, customer_id, account_id, branch, card_number,
                      card_type, card_network, credit_limit,
                      current_balance, issued_date, expiry_date, status))
                conn.commit()
                st.success("✅ Credit Card Added")

        # ---------- BRANCHES ----------

        if table_option == "branches":
            branch_id = st.text_input("Branch ID")
            branch_name = st.text_input("Branch Name")
            city = st.text_input("City")
            manager_name = st.text_input("Manager Name")
            total_employees = st.number_input("Total Employees", min_value=0)
            branch_revenue = st.number_input("Branch Revenue", min_value=0.0)
            opening_date = st.date_input("Opening Date")
            performance_rating = st.number_input("Performance Rating", 1, 5)

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO branches
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """, (branch_id, branch_name, city, manager_name,
                      total_employees, branch_revenue,
                      opening_date, performance_rating))
                conn.commit()
                st.success("✅ Branch Added")

        # ---------- SUPPORT TICKETS ----------

        if table_option == "support_tickets":
            ticket_id = st.text_input("Ticket ID")
            customer_id = st.text_input("Customer ID")
            account_id = st.text_input("Account ID")
            loan_id = st.text_input("Loan ID")
            branch_name = st.text_input("Branch Name")
            issue_category = st.text_input("Issue Category")
            description = st.text_area("Description")
            date_opened = st.date_input("Date Opened")
            date_closed = st.date_input("Date Closed")
            priority = st.selectbox("Priority", ["Critical", "High", "Medium", "Low"])
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            resolution = st.text_area("Resolution Remarks")
            agent = st.text_input("Support Agent")
            channel = st.selectbox("Channel", ["Email", "Phone", "In-person", "Mobile App"])
            rating = st.number_input("Customer Rating", 1, 5)

            if st.button("Add Record"):
                cursor.execute("""
                    INSERT INTO support_tickets
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (ticket_id, customer_id, account_id, loan_id, branch_name,
                      issue_category, description, date_opened, date_closed,
                      priority, status, resolution, agent, channel))
                conn.commit()
                st.success("✅ Ticket Added")

    # ================= UPDATE =================

    elif operation == "Update":

        st.subheader(f"✏️ Update Record in {table_option}")

        # ---------- PRIMARY KEY MAP ----------
        primary_keys = {
            "customers": "customer_id",
            "accounts": "customer_id",
            "transactions": "txn_id",
            "loans": "loan_id",
            "credit_cards": "card_id",
            "branches": "branch_id",
            "support_tickets": "ticket_id"
        }

        pk_column = primary_keys[table_option]

        # ---------- FETCH TABLE DATA ----------
        df = pd.read_sql(f"SELECT * FROM {table_option}", conn)

        # ---------- SELECT PRIMARY KEY VALUE ----------
        pk_value = st.selectbox(
            f"Select {pk_column}",
            df[pk_column].unique()
        )

        # ---------- SELECT COLUMN TO UPDATE ----------
        update_column = st.selectbox(
            "Select Column to Update",
            [col for col in df.columns if col != pk_column]
        )

        # ---------- ENTER NEW VALUE ----------
        new_value = st.text_input("Enter New Value")

        # ---------- UPDATE ----------
        if st.button("Update Record"):
            try:
                sql = f"""
                    UPDATE {table_option}
                    SET {update_column} = %s
                    WHERE {pk_column} = %s
                """

                cursor.execute(sql, (new_value, pk_value))
                conn.commit()

                st.success("✅ Record Updated Successfully in SQL Table")

            except Exception as e:
                st.error(f"❌ Error: {e}")
# ================= DELETE =================
    elif operation == "Delete":
        st.subheader(f"❌ Delete Record from {table_option}")

        # ---------- PRIMARY KEY MAP ----------
        primary_keys = {
            "customers": "customer_id",
            "accounts": "customer_id",
            "transactions": "txn_id",
            "loans": "loan_id",
            "credit_cards": "card_id",
            "branches": "branch_id",
            "support_tickets": "ticket_id"
        }

        pk_column = primary_keys[table_option]

        # ---------- FETCH TABLE DATA ----------
        df = pd.read_sql(f"SELECT * FROM {table_option}", conn)

        # ---------- SELECT PRIMARY KEY VALUE ----------
        pk_value = st.selectbox(
            f"Select {pk_column} to Delete",
            df[pk_column].unique()
        )

        # ---------- DELETE ----------
        if st.button("Delete Record"):
            try:
                sql = f"DELETE FROM {table_option} WHERE {pk_column} = %s"
                cursor.execute(sql, (pk_value,))
                conn.commit()
                st.success(f"✅ Record with {pk_column} = {pk_value} deleted successfully!")
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ================== Credit/Debit Simulation ==================

elif option == "💰 Credit/Debit Simulation":

    st.subheader("💰 Deposit / Withdraw Money")

    # Input fields
    account_id = st.text_input("Enter Account ID:")
    amount = st.number_input("Enter Amount (₹):", min_value=0.0)

    action = st.radio(
        "Select Action",
        ["Check Balance", "Deposit", "Withdraw"]
    )

    # Submit button
    if st.button("Submit"):

        if not account_id:
            st.warning("❌ Please enter an Account ID")
        else:
            # Fetch current balance from DB
            cursor.execute("SELECT account_balance FROM accounts WHERE customer_id=%s", (account_id,))
            result = cursor.fetchone()

            if result is None:
                st.error("❌ Account not found!")
            else:
                current_balance = result[0]  # this is Decimal

                # Convert amount to Decimal
                amount_decimal = Decimal(str(amount))

                if action == "Check Balance":
                    st.info(f"💰 Current Balance: ₹{current_balance:.2f}")

                elif action == "Deposit":
                    new_balance = current_balance + amount_decimal
                    cursor.execute(
                        "UPDATE accounts SET account_balance=%s WHERE customer_id=%s",
                        (new_balance, account_id)
                    )
                    conn.commit()
                    st.success(f"✅ Deposited ₹{amount_decimal:.2f}. New Balance: ₹{new_balance:.2f}")

                elif action == "Withdraw":
                    if amount_decimal > current_balance:
                        st.error("❌ Insufficient Balance!")
                    else:
                        new_balance = current_balance - amount_decimal
                        cursor.execute(
                            "UPDATE accounts SET account_balance=%s WHERE customer_id=%s",
                            (new_balance, account_id)
                        )
                        conn.commit()
                        st.success(f"✅ Withdrawn ₹{amount_decimal:.2f}. New Balance: ₹{new_balance:.2f}")

# ================== Credit/Debit Simulation ==================

elif option == "🧠 Analytical Insights":

    st.subheader("🧠 Analytical Insights")
    st.write("""Explore Key SQL-driven insights from the **BankSight DataBase**. 
                Select any question below to view live results.""")
    
    cust_acc = pd.merge(customers, accounts, on='customer_id', how='left')

    # ------------------- Map Questions to Functions -------------------
    questions = {
        "Q1: How many customers exist per city, and their average account balance?":
            lambda: cust_acc.groupby('city').agg(
                total_customers=('customer_id', 'count'),
                avg_account_balance=('account_balance', 'mean')
            ).reset_index(),

        "Q2: Which account type holds the highest total balance?":
            lambda: cust_acc.groupby('account_type').agg(
                total_balance=('account_balance','sum')
            ).reset_index().sort_values(by='total_balance', ascending=False).head(1),

        "Q3: Top 10 customers by total account balance":
            lambda: cust_acc.groupby(['customer_id','name'])['account_balance'].sum().reset_index().sort_values(by='account_balance', ascending=False).head(10),

        "Q4: Customers opened accounts in 2023 with balance > ₹1,00,000":
            lambda: cust_acc[(cust_acc['join_date'].dt.year == 2023) & (cust_acc['account_balance'] > 100000)][['customer_id','name','account_balance','join_date']],

        "Q5: Total transaction volume by transaction type":
            lambda: transactions.groupby('txn_type').agg(total_amount=('amount', 'sum')).reset_index(),

        "Q6: Failed transactions per transaction type":
            lambda: transactions[transactions['status'].str.lower() == 'failed'].groupby('txn_type').size().reset_index(name='failed_count'),

        "Q7: Total transactions per transaction type":
            lambda: transactions.groupby('txn_type').agg(total_count=('txn_id','count')).reset_index(),

        "Q8: Accounts with ≥5 high-value transactions (>₹20,000)":
            lambda: transactions[transactions['amount'] > 20000].groupby('customer_id').agg(
                txn_count=('txn_id','count'),
                total_amount=('amount','sum')
            ).reset_index().query('txn_count >= 5'),

        "Q9: Average loan amount and interest rate by loan type":
            lambda: loans.groupby('loan_type').agg(
                avg_loan_amount=('loan_amount','mean'),
                avg_interest_rate=('interest_rate','mean')
            ).reset_index(),

        "Q10: Customers with more than one active/approved loan":
            lambda: pd.merge(
                loans[loans['loan_status'].isin(['Active','Approved'])].groupby('customer_id').agg(
                    num_loans=('loan_id','count')
                ).reset_index().query('num_loans > 1'),
                customers[['customer_id','name']],
                on='customer_id',
                how='left'
            ),

        "Q11: Top 5 customers by outstanding (non-closed) loan amounts":
            lambda: pd.merge(
                loans[loans['loan_status']!='Closed'].groupby('customer_id').agg(
                    total_outstanding=('loan_amount','sum')
                ).reset_index().sort_values(by='total_outstanding', ascending=False).head(5),
                customers[['customer_id','name']],
                on='customer_id',
                how='left'
            ),

        "Q12: Average loan amount per branch":
            lambda: loans.groupby('branch').agg(avg_loan_amount=('loan_amount','mean')).reset_index(),

        "Q13: Customers count per age group":
            lambda: customers.assign(
                age_group=pd.cut(customers['age'], bins=[0,18,25,35,45,60,120], labels=['<18','18-25','26-35','36-45','46-60','60+'])
            ).groupby('age_group').agg(total_customers=('customer_id','count')).reset_index(),

        "Q14: Issue categories with longest average resolution time":
            lambda: support_tickets.assign(
                resolution_days=(support_tickets['date_closed'] - support_tickets['date_opened']).dt.days
            ).dropna(subset=['resolution_days']).groupby('issue_category').agg(
                avg_resolution_days=('resolution_days','mean')
            ).reset_index().sort_values(by='avg_resolution_days', ascending=False),

        "Q15: Support agents resolving most critical tickets with high rating (≥4)":
            lambda: support_tickets[
                (support_tickets['priority']=='Critical') & (support_tickets['customer_rating']>=4)
            ].groupby('support_agent').agg(total_critical_tickets=('ticket_id','count')).reset_index().sort_values(by='total_critical_tickets', ascending=False),

        "Q16: City with highest total account balance":
            lambda: cust_acc.groupby('city').agg(total_balance=('account_balance','sum')).reset_index().sort_values(by='total_balance', ascending=False),

        "Q17: Customers with no transactions":
            lambda: customers[~customers['customer_id'].isin(transactions['customer_id'].unique())][['customer_id','name']],

        "Q18: Distribution of loans by loan status":
            lambda: loans.groupby('loan_status').agg(total_loans=('loan_id','count')).reset_index(),

        "Q19: Loan type with highest average interest rate":
            lambda: loans.groupby('loan_type').agg(avg_interest_rate=('interest_rate','mean')).reset_index().sort_values(by='avg_interest_rate', ascending=False),

        "Q20: Customers with both a loan and a credit card":
            lambda: customers[customers['customer_id'].isin(
                set(loans['customer_id'].unique()).intersection(set(credit_cards['customer_id'].unique()))
            )][['customer_id','name']],

        "Q21: Number of loans issued per branch":
            lambda: loans.groupby('branch').agg(total_loans=('loan_id','count')).reset_index(),

        "Q22: Top 5 customers by failed transactions":
            lambda: pd.merge(
                transactions[transactions['status'].str.lower()=='failed'].groupby('customer_id').agg(failed_count=('txn_id','count')).reset_index().sort_values(by='failed_count', ascending=False).head(5),
                customers[['customer_id','name']],
                on='customer_id',
                how='left'
            ),

        "Q23: Average customer rating by support ticket priority":
            lambda: support_tickets.groupby('priority').agg(avg_rating=('customer_rating','mean')).reset_index(),

        "Q24: Average account balance of senior citizens (age>60)":
            lambda: pd.merge(
                customers[customers['age']>60],
                accounts,
                on='customer_id',
                how='left'
            )['account_balance'].mean(),

        "Q25: Average loan duration for closed loans (days)":
            lambda: loans[loans['loan_status']=='Closed'].assign(
                start_date=pd.to_datetime(loans['start_date'], errors='coerce'),
                end_date=pd.to_datetime(loans['end_date'], errors='coerce')
            ).assign(
                loan_duration_days=lambda df: (df['end_date'] - df['start_date']).dt.days
            )['loan_duration_days'].mean()
    }

    selected_question = st.selectbox("Select a Question to Explore:", list(questions.keys()))

    if st.button("Run Analysis"):
        result = questions[selected_question]()

        if isinstance(result, pd.DataFrame):
            st.dataframe(result)
        else:
            st.write(result)

# ================== About Creator ==================

elif option == "👩‍💻 About Creator":

    st.subheader("👩‍💻 About the Creator")
    st.write("""
    **Name:** Aarthiba  
    **Role:** Data Analyst & Python Developer  
    **Project:** BankSight Analytics App  
    **Skills:** Python, Pandas, SQL, Streamlit, Data Visualization  
    **Contact:** aarthibachristy15@gmail.com
    """)







