elif option == "💰 Credit/Debit Simulation":

    st.subheader("💰 Deposit / Withdraw Money")

    Enter_account_id = st.text_input("Enter Account ID:")
    Enter_Amount = st.number_input("Enter Amount(₹):", min_value=0.0)

    select_action = st.radio(
    "Select Action",
    ["Check Balance", "Deposit", "Withdraw"]
)
    if st.button("Submit"):
        st.success(f"")

 


