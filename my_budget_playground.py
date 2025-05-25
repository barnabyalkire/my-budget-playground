
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Budget Playground", layout="centered")

st.title("💸 My Budget Playground")
st.markdown("Adjust your monthly budget to reflect your real life — or explore a new one. This isn’t about guilt. It’s a mirror, a sandbox, and a reset button.")

# Monthly income
income = st.slider("Monthly Income ($)", 1000, 20000, 4000, 100)

# Expense sliders
st.subheader("Your Expenses")
housing = st.slider("Housing", 0, income, int(income * 0.3), 50)
food = st.slider("Food", 0, income, int(income * 0.15), 25)
transport = st.slider("Transport", 0, income, int(income * 0.1), 25)
fun = st.slider("Fun & Leisure", 0, income, int(income * 0.1), 25)
debt = st.slider("Debt Payments", 0, income, int(income * 0.1), 25)
savings = st.slider("Savings", 0, income, int(income * 0.1), 25)
other = st.slider("Other", 0, income, 0, 25)

# Calculations
total_spent = housing + food + transport + fun + debt + savings + other
balance = income - total_spent

# Display balance
st.subheader("Monthly Outcome")
if balance > 0:
    st.success(f"You have a surplus of ${balance:,} this month.")
elif balance < 0:
    st.error(f"You're over budget by ${-balance:,}.")
else:
    st.info("You broke even this month.")

# Visualization
st.subheader("Budget Breakdown")
labels = ["Housing", "Food", "Transport", "Fun", "Debt", "Savings", "Other"]
sizes = [housing, food, transport, fun, debt, savings, other]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# Optional reflection
st.markdown("### Reflection")
st.text_area("What did you notice about your budget?", placeholder="Your thoughts here...")

st.caption("Built with love. This is your space.")
