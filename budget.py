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

# Calculate recommended values
def calculate_budget(income, budget_percentages):
    return {category: income * percentage for category, percentage in budget_percentages.items()}

# Streamlit app
st.title("Personal Budget Planner")

# Input income
income = st.number_input("Enter your monthly income:", min_value=0.0, format="%f")

if income > 0:
    # Default budget
    default_budget = calculate_budget(income, DEFAULT_BUDGET)

    # Adjust budget percentages
    st.sidebar.header("Adjust Budget Percentages")
    housing_pct = st.sidebar.slider("Housing", 0, 100, int(DEFAULT_BUDGET['Housing'] * 100))
    food_pct = st.sidebar.slider("Food", 0, 100, int(DEFAULT_BUDGET['Food'] * 100))
    transportation_pct = st.sidebar.slider("Transportation", 0, 100, int(DEFAULT_BUDGET['Transportation'] * 100))
    savings_pct = st.sidebar.slider("Savings", 0, 100, int(DEFAULT_BUDGET['Savings'] * 100))
    entertainment_pct = st.sidebar.slider("Entertainment", 0, 100, int(DEFAULT_BUDGET['Entertainment'] * 100))
    miscellaneous_pct = st.sidebar.slider("Miscellaneous", 0, 100, int(DEFAULT_BUDGET['Miscellaneous'] * 100))

    # Adjust total percentage to be 100%
    total_pct = (housing_pct + food_pct + transportation_pct +
                 savings_pct + entertainment_pct + miscellaneous_pct)

    if total_pct != 100:
        st.sidebar.error("The total percentage must be 100%.")
    else:
        adjusted_budget = {
            'Housing': housing_pct / 100,
            'Food': food_pct / 100,
            'Transportation': transportation_pct / 100,
            'Savings': savings_pct / 100,
            'Entertainment': entertainment_pct / 100,
            'Miscellaneous': miscellaneous_pct / 100
        }

        # Calculate adjusted budget
        adjusted_budget_values = calculate_budget(income, adjusted_budget)

        # Display results
        st.subheader("Budget Overview")

        # Create dataframes for better formatting
        import pandas as pd
        
        # Default Budget
        default_df = pd.DataFrame(list(default_budget.items()), columns=['Category', 'Default Amount'])
        
        # Adjusted Budget
        adjusted_df = pd.DataFrame(list(adjusted_budget_values.items()), columns=['Category', 'Adjusted Amount'])
        
        # Merge dataframes for comparison
        budget_comparison = pd.merge(default_df, adjusted_df, on='Category')
        
        st.write(budget_comparison)

else:
    st.warning("Please enter a valid income amount.")

