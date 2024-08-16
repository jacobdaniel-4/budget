import streamlit as st

# Title
st.title("Budget Calculator")

# Input fields
st.header("Income")
income = st.number_input("Enter your total monthly income", min_value=0.0, value=0.0, step=100.0)

st.header("Expenses")
housing = st.number_input("Housing (Rent/Mortgage)", min_value=0.0, value=0.0, step=50.0)
utilities = st.number_input("Utilities (Electricity, Water, etc.)", min_value=0.0, value=0.0, step=10.0)
groceries = st.number_input("Groceries", min_value=0.0, value=0.0, step=10.0)
transportation = st.number_input("Transportation", min_value=0.0, value=0.0, step=10.0)
entertainment = st.number_input("Entertainment", min_value=0.0, value=0.0, step=10.0)
other_expenses = st.number_input("Other Expenses", min_value=0.0, value=0.0, step=10.0)

# Calculate total expenses
total_expenses = housing + utilities + groceries + transportation + entertainment + other_expenses

# Calculate remaining balance
remaining_balance = income - total_expenses

# Display results
st.header("Summary")
st.write(f"Total Expenses: ${total_expenses:.2f}")
st.write(f"Remaining Balance: ${remaining_balance:.2f}")

# Tips based on balance
if remaining_balance < 0:
    st.error("Warning: Your expenses exceed your income!")
elif remaining_balance == 0:
    st.info("You're breaking even. Consider saving or cutting down on expenses.")
else:
    st.success(f"Good job! You have ${remaining_balance:.2f} left over.")










