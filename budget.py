import streamlit as st

# Title
st.title("Budget Calculator")

# Input fields for income and expenses
st.header("Monthly Budget")

# Set up columns for a tighter layout
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Income", min_value=0.0, value=0.0, step=100.0)
    housing = st.number_input("Housing", min_value=0.0, value=0.0, step=50.0)
    groceries = st.number_input("Groceries", min_value=0.0, value=0.0, step=10.0)
    entertainment = st.number_input("Entertainment", min_value=0.0, value=0.0, step=10.0)

with col2:
    utilities = st.number_input("Utilities", min_value=0.0, value=0.0, step=10.0)
    transportation = st.number_input("Transportation", min_value=0.0, value=0.0, step=10.0)
    other_expenses = st.number_input("Other Expenses", min_value=0.0, value=0.0, step=10.0)

# Calculate total expenses
total_expenses = housing + utilities + groceries + transportation + entertainment + other_expenses

# Calculate remaining balance
remaining_balance = income - total_expenses

# Display results
st.subheader("Summary")
st.write(f"**Total Expenses:** ${total_expenses:.2f}")
st.write(f"**Remaining Balance:** ${remaining_balance:.2f}")

# Feedback on balance
if remaining_balance < 0:
    st.error("Warning: Your expenses exceed your income!")
elif remaining_balance == 0:
    st.info("You're breaking even. Consider saving or reducing expenses.")
else:
    st.success(f"Good job! You have ${remaining_balance:.2f} left over.")











