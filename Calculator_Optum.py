import streamlit as st
import pandas as pd
import plotly.express as px
import math

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")
patients_per_month = st.sidebar.number_input("Number of PA's per Month", value=50000)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=2)

# Prior Authorization module
enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:**\nBefore: 30 min × PA's/month × hourly wage\nAfter: $prior auth price + 1 min × PA's/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=8.00, step=0.05, format="%.2f")

# Revenue inputs
baseline_approval_rate = st.sidebar.number_input("Baseline Approval Rate (%)", value=40, min_value=0, max_value=100, step=1)
improved_approval_rate = st.sidebar.number_input("Improved Approval Rate (%)", value=46, min_value=0, max_value=100, step=1)
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

# Summary (ROI removed)
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

# Revenue Generated from Approvals Graph
st.header("Revenue Generated from Approvals")

# X-axis: Range of PA's Submitted Annually (e.g., 0 to max value)
max_pas = patients_per_month * 12 * years
step_size = max(1000, int(max_pas / 10))
pa_submitted_range = list(range(0, max_pas + 1, step_size))

# Calculate revenue for each scenario
baseline_revenue = [
    pa * (baseline_approval_rate / 100) * (annual_revenue_per_patient * years) / 1_000_000
    for pa in pa_submitted_range
]
improved_revenue = [
    pa * (improved_approval_rate / 100) * (annual_revenue_per_patient * years) / 1_000_000
    for pa in pa_submitted_range
]

revenue_plot_df = pd.DataFrame({
    "PA's Submitted": pa_submitted_range,
    f"Baseline Revenue ({baseline_approval_rate}%)": baseline_revenue,
    f"Revenue Recaptured ({improved_approval_rate}%)": improved_revenue
})

revenue_plot_df_melted = revenue_plot_df.melt(
    id_vars="PA's Submitted",
    var_name="Scenario",
    value_name="Revenue Generated ($M)"
)

fig3 = px.line(
    revenue_plot_df_melted,
    x="PA's Submitted",
    y="Revenue Generated ($M)",
    color="Scenario",
    title="Revenue Generated from Approvals",
    markers=True
)
fig3.update_layout(
    xaxis_title="PA's Submitted",
    yaxis_title="Revenue Generated ($M)",
    legend_title='Scenario'
)

st.plotly_chart(fig3)

st.caption("""
**Calculation Logic:**

Baseline Revenue = PA's Submitted × Baseline Approval Rate × Annual Revenue per PA × Time Horizon

Revenue Recaptured = PA's Submitted × Improved Approval Rate × Annual Revenue per PA × Time Horizon

Chart values are expressed in **$1M units**.
""")
