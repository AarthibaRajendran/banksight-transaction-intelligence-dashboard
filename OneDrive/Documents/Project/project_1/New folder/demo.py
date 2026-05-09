import streamlit as st
from datetime import datetime
import pandas as pd
import mysql.connector

# =================== MySQL CONNECTION ===================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aarthiba@123",
    database="banksight"
)
cursor = conn.cursor()

# ================== SIDEBAR NAVIGATION ==================

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

# =================== INTRODUCTION ===================

if option == "🏠 Introduction":

    st.title("🏦 BankSight: Transaction Intelligence Dashboard")

    st.subheader("Project Overview")
    st.write(
        "BankSight is a financial analytics system built using Python, Streamlit, "
        "and MySQL. It helps analyze customers, accounts, transactions, loans, "
        "credit cards, branches, and support tickets."
    )

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

# =================== FILTER DATA ===================

elif option == "🔍 Filter Data":

    st.subheader("🔍 Filter Data")

    table_option = st.selectbox(
        "Select Table",
        ["customers", "accounts", "transactions"]
    )

    if table_option == "customers":
        df = pd.read_sql("SELECT * FROM customers", conn)
        city = st.multiselect("City", df["city"].unique())

        if city:
            df = df[df["city"].isin(city)]

        st.dataframe(df)

    elif table_option == "accounts":
        df = pd.read_sql("SELECT * FROM accounts", conn)
        balance = st.multiselect("Account Balance", df["account_balance"].unique())

        if balance:
            df = df[df["account_balance"].isin(balance)]

        st.dataframe(df)

    elif table_option == "transactions":
        df = pd.read_sql("SELECT * FROM transactions", conn)
        txn_type = st.multiselect("Transaction Type", df["txn_type"].unique())

        if txn_type:
            df = df[df["txn_type"].isin(txn_type)]

        st.dataframe(df)

# =================== CRUD OPERATIONS ===================

elif option == "✏️ CRUD Operations":

    st.subheader("✏️ CRUD Operations")

    operation = st.radio("Select Operation", ["View", "Add"])

    if operation == "View":
        df = pd.read_sql("SELECT * FROM customers", conn)
        st.dataframe(df)

    elif operation == "Add":
        customer_id = st.text_input("Customer ID")
        name = st.text_input("Name")
        city = st.text_input("City")

        if st.button("Add Customer"):
            cursor.execute(
                "INSERT INTO customers (customer_id, name, city) VALUES (%s,%s,%s)",
                (customer_id, name, city)
            )
            conn.commit()
            st.success("Customer Added Successfully")

# =================== CREDIT / DEBIT ===================

elif option == "💰 Credit/Debit Simulation":
    st.subheader("💰 Credit / Debit Simulation")
    st.info("Feature under development")

# =================== ANALYTICS ===================

elif option == "🧠 Analytical Insights":
    st.subheader("🧠 Analytical Insights")
    st.info("Charts will be added here")

# =================== ABOUT ===================

elif option == "👩‍💻 About Creator":
    st.subheader("👩‍💻 About Creator")
    st.write("Created by BankSight Developer")

