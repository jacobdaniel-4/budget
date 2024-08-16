import streamlit as st

# Initial default percentages for each category
DEFAULT_BUDGET = {
    'Housing': 30,
    'Food': 15,
    'Transportation': 10,
    'Savings': 10,
    'Entertainment': 5,
    'Miscellaneous': 10
}

categories = list(DEFAULT_BUDGET.keys())
total_pct = sum(DEFAULT_BUDGET.values())

# Create sliders for each category
st.title("Adjustable Budget Bar")
st.subheader("Drag the sliders to adjust your budget allocations")

percentages = {}
for category in categories:
    percentages[category] = st.slider(f"{category}", 0, 100, DEFAULT_BUDGET[category], key=category)

# Recalculate the total percentage
total_pct = sum(percentages.values())

# Calculate width percentages for the progress bar
progress_values = [percentages[cat] / total_pct for cat in categories]

# Display a visual progress bar
st.write("Budget Allocation Bar:")
st.progress(1)  # To set the scale of the bar

# Display budget in percentage format
for category, pct in percentages.items():
    st.write(f"{category}: {pct}%")

if total_pct != 100:
    st.error("Your total percentage must be 100%. Please adjust.")
else:
    st.success("Your budget is properly allocated.")










