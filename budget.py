import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Budget Calculator")

# Set up columns for a tighter layout
col1, col2 = st.columns([2, 3])

with col1:
    st.header("Monthly Budget")

    # Input fields
    income = st.number_input("Income", min_value=0.0, value=0.0, step=100.0)
    housing = st.number_input("Housing", min_value=0.0, value=0.0, step=50.0)
    groceries = st.number_input("Groceries", min_value=0.0, value=0.0, step=10.0)
    entertainment = st.number_input("Entertainment", min_value=0.0, value=0.0, step=10.0)
    savings = st.number_input("Savings", min_value=0.0, value=0.0, step=10.0)

    utilities = st.number_input("Utilities", min_value=0.0, value=0.0, step=10.0)
    transportation = st.number_input("Transportation", min_value=0.0, value=0.0, step=10.0)
    other_expenses = st.number_input("Other Expenses", min_value=0.0, value=0.0, step=10.0)

    # Calculate total expenses and remaining balance
    total_expenses = housing + utilities + groceries + transportation + entertainment + other_expenses
    total_deductions = total_expenses + savings
    remaining_balance = income - total_deductions

    st.subheader("Summary")
    st.write(f"**Total Expenses:** ${total_expenses:.2f}")
    st.write(f"**Total Deductions (Expenses + Savings):** ${total_deductions:.2f}")
    st.write(f"**Remaining Balance:** ${remaining_balance:.2f}")

    # Feedback on balance
    if remaining_balance < 0:
        st.error("Warning: Your expenses and savings exceed your income!")
    elif remaining_balance == 0:
        st.info("You're breaking even. Consider adjusting your savings or expenses.")
    else:
        st.success(f"Good job! You have ${remaining_balance:.2f} left over after expenses and savings.")

with col2:
    st.header("Savings Growth Projection")

    # User inputs for investment growth
    annual_return_rate = st.slider("Annual Return Rate (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1) / 100
    years = st.slider("Investment Duration (Years)", min_value=1, max_value=50, value=30)

    # Assumptions for investment growth
    months = years * 12

    # Calculate future value of monthly investments
    if savings > 0:
        periods = np.arange(1, months + 1)
        future_values = savings * (((1 + annual_return_rate / 12) ** periods - 1) / (annual_return_rate / 12))

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(periods / 12, future_values / 1e6, label='Future Value (in millions)')
        plt.plot(periods / 12, future_values / 1e3, label='Future Value (in thousands)', linestyle='--')
        plt.xlabel('Years')
        plt.ylabel('Future Value ($)')
        plt.title('Projected Growth of Monthly Savings Over Time')
        plt.legend()
        plt.grid(True)

        # Adjust y-axis labels to show 'k' and 'm'
        ax = plt.gca()
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x) if x < 1e6 else int(x / 1e6)) + ('k' if x < 1e6 else 'M')))

        st.pyplot(plt)
    else:
        st.write("Enter a savings amount to see the growth projection.")













