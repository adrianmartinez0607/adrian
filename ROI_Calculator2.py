import streamlit as st
import pandas as pd
import plotly.express as px
import math

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")
patients_per_month = st.sidebar.number_input("Number of PA's per Month", value=200)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=3)

# Prior Authorization module
enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:**\nBefore: 30 min × PA's/month × hourly wage\nAfter: $prior auth price + 1 min × PA's/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=8.00, step=0.05, format="%.2f")

# Revenue inputs
baseline_approval_rate = st.sidebar.number_input("Baseline Approval Rate (%)", value=40, min_value=0, max_value=100, step=1)
improved_approval_rate = st.sidebar.number_input("Improved Approval Rate (%)", value=41, min_value=0, max_value=100, step=1)
annual_revenue_per_patient = st.sidebar.number_input("Annual Revenue per PA Processed ($)", value=80000, step=1000)

# Constants
months = years * 12
minutes_to_hours = 1 / 60
auth_time = 40
post_lamar_time = 1
patients_per_year = patients_per_month * 12

# Cost before and after Lamar
cost_before_auth = auth_time * minutes_to_hours * patients_per_month * hourly_salary * months if enable_auth else 0
cost_after_auth = (auth_price + post_lamar_time * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_auth else 0

cost_before_total = cost_before_auth
cost_after_total = cost_after_auth

# Savings
savings = cost_before_total - cost_after_total
time_saved_hours = savings / hourly_salary if hourly_salary != 0 else 0

# Revenue Generated (clip negative improvements to zero) and multiply by time horizon
approval_rate_delta = improved_approval_rate - baseline_approval_rate
approval_rate_improvement = max(0, approval_rate_delta / 100)
revenue_generated = patients_per_year * annual_revenue_per_patient * approval_rate_improvement * years

# Round to nearest $100,000 and convert to M or B display
rounded_revenue = math.ceil(revenue_generated / 100000) * 100000
if rounded_revenue >= 1_000_000_000:
    revenue_display = f"${rounded_revenue / 1_000_000_000:.2f}B"
else:
    revenue_display = f"${rounded_revenue / 1_000_000:.2f}M"

# Summary (removed ROI)
st.title("Lamar Health ROI Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Time Saved (Hours)", f"{time_saved_hours:,.2f}")
col2.metric("Cost Savings ($)", f"${savings:,.0f}")
col3.metric("Revenue Generated ($)", revenue_display)

# Time graph data
months_range = list(range(1, months + 1))
costs_before = [(auth_time * minutes_to_hours * patients_per_month * hourly_salary) * m for m in months_range]
costs_after = [((auth_price) + (post_lamar_time * minutes_to_hours * hourly_salary)) * patients_per_month * m for m in months_range]

data_plot = pd.DataFrame({
    'Month': months_range,
    'Cost Before Lamar': costs_before,
    'Cost After Lamar': costs_after
})

fig = px.line(
    data_plot,
    x='Month',
    y=['Cost Before Lamar', 'Cost After Lamar'],
    title='Cost Over Time',
    labels={'value': 'Cost ($)', 'Month': 'Month', 'variable': 'Scenario'},
    markers=True
)
fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Cost ($)',
    legend_title='Scenario'
)
st.plotly_chart(fig)

st.write("Lamar Health offers automation for Prior Authorization. Customize the inputs on the left to see how much you can save.")

# Revenue Generated from Lamar PA Submissions
st.header("Revenue Generated from Lamar PA Submissions")

# Generate chart data for 1–20% approval rate improvement scenarios
approval_rate_improvements = list(range(1, 21))
revenue_baseline = [
    (patients_per_year * annual_revenue_per_patient * (baseline_approval_rate / 100) * (improvement / 100)) / 10000000
    for improvement in approval_rate_improvements
]
revenue_improved = [
    (patients_per_year * annual_revenue_per_patient * (improved_approval_rate / 100) * (improvement / 100)) / 10000000
    for improvement in approval_rate_improvements
]

revenue_df = pd.DataFrame({
    'Approval Rate Improvement (%)': approval_rate_improvements,
    f'Baseline Approval Rate ({baseline_approval_rate}%)': revenue_baseline,
    f'Improved Approval Rate ({improved_approval_rate}%)': revenue_improved
})

revenue_df_melted = revenue_df.melt(id_vars='Approval Rate Improvement (%)',
                                    var_name='Scenario',
                                    value_name='Revenue Generated ($10M)')

fig2 = px.line(
    revenue_df_melted,
    x='Approval Rate Improvement (%)',
    y='Revenue Generated ($10M)',
    color='Scenario',
    title='Revenue Generated vs. Approval Rate Improvement',
    markers=True
)
fig2.update_layout(
    xaxis_title='Approval Rate Improvement (%)',
    yaxis_title='Revenue Generated ($10M)',
    legend_title='Scenario'
)
st.plotly_chart(fig2)

st.caption("""
**Calculation Logic:**
Revenue Generated = Patients per Year × Annual Revenue per PA × (Improved Approval Rate – Baseline Approval Rate) × Time Horizon

Chart values are expressed in **$10M units**.
""")
