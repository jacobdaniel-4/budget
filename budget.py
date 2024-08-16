import streamlit as st

# Define default budget percentages
DEFAULT_BUDGET = {
    'Housing': 0.30,
    'Food': 0.15,
    'Transportation': 0.10,
    'Savings': 0.10,
    'Entertainment': 0.05,
    'Miscellaneous': 0.10
}

# Calculate budget values based on income and percentages
def calculate_budget(income, budget_percentages):
    return {category: income * percentage for category, percentage in budget_percentages.items()}

# Streamlit app
st.title("Personal Budget Planner")

# Input income
income = st.number_input("Enter your monthly income:", min_value=0.0, format="%f")

if income > 0:
    st.subheader("Budget")

    # Adjust budget percentages via sliders
    housing_pct = st.slider("Housing", 0, 100, int(DEFAULT_BUDGET['Housing'] * 100))
    food_pct = st.slider("Food", 0, 100, int(DEFAULT_BUDGET['Food'] * 100))
    transportation_pct = st.slider("Transportation", 0, 100, int(DEFAULT_BUDGET['Transportation'] * 100))
    savings_pct = st.slider("Savings", 0, 100, int(DEFAULT_BUDGET['Savings'] * 100))
    entertainment_pct = st.slider("Entertainment", 0, 100, int(DEFAULT_BUDGET['Entertainment'] * 100))
    miscellaneous_pct = st.slider("Miscellaneous", 0, 100, int(DEFAULT_BUDGET['Miscellaneous'] * 100))

    # Calculate the total percentage
    total_pct = (housing_pct + food_pct + transportation_pct +
                 savings_pct + entertainment_pct + miscellaneous_pct)

    if total_pct == 100:
        # Adjusted budget based on slider values
        adjusted_budget = {
            'Housing': housing_pct / 100,
            'Food': food_pct / 100,
            'Transportation': transportation_pct / 100,
            'Savings': savings_pct / 100,
            'Entertainment': entertainment_pct / 100,
            'Miscellaneous': miscellaneous_pct / 100
        }
        budget = calculate_budget(income, adjusted_budget)
    else:
        st.error("The total percentage must equal 100%.")
        budget = calculate_budget(income, DEFAULT_BUDGET)

    # Display the budget (either default or adjusted)
    for category, amount in budget.items():
        st.write(f"{category}: ${amount:.2f}")
else:
    st.warning("Please enter a valid income amount.")








