import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")
patients_per_month = st.sidebar.number_input("Number of PA's per Month", value=200)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=3)

# Prior Authorization module
enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:**\nBefore: 30 min × PA's/month × hourly wage\nAfter: $prior auth price + 1 min × PA's/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=6.00, step=0.05, format="%.2f")

# Revenue Recapture inputs
baseline_denial_rate = st.sidebar.number_input("Baseline Denial Rate (%)", value=60, min_value=0, max_value=100, step=1)
annual_revenue_per_patient = st.sidebar.number_input("Annual Estimated Cost per Patient ($)", value=80000, step=1000)

# Constants
months = years * 12
minutes_to_hours = 1 / 60
auth_time = 40
post_lamar_time = 1  # 1 minute of staff time per patient per module

# Cost before and after Lamar
cost_before_auth = auth_time * minutes_to_hours * patients_per_month * hourly_salary * months if enable_auth else 0
cost_after_auth = (auth_price + post_lamar_time * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_auth else 0

cost_before_total = cost_before_auth
cost_after_total = cost_after_auth

# Savings
savings = cost_before_total - cost_after_total
time_saved_hours = savings / hourly_salary if hourly_salary != 0 else 0
roi_percent = (savings / cost_before_total) * 100 if cost_before_total != 0 else 0

# Summary
st.title("Lamar Health ROI Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Time Saved (Hours)", f"{time_saved_hours:,.2f}")
col2.metric("Cost Savings ($)", f"${savings:,.2f}")
col3.metric("ROI (%)", f"{roi_percent:.2f}%")

# Time graph data
months_range = list(range(1, months + 1))
costs_before = [(auth_time * minutes_to_hours * patients_per_month * hourly_salary) * m for m in months_range]
costs_after = [((auth_price) + (post_lamar_time * minutes_to_hours * hourly_salary)) * patients_per_month * m for m in months_range]

# Create DataFrame for plotting
data_plot = pd.DataFrame({
    'Month': months_range,
    'Cost Before Lamar': costs_before,
    'Cost After Lamar': costs_after
})

# Plot cost comparison
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

# Revenue Recapture from Lamar PA Submissions
st.header("Revenue Recapture from Lamar PA Submissions")

# Generate improvement scenarios: 1% to 20% improvement
denial_rate_improvements = [x for x in range(1, 21)]  # 1% to 20% improvement
patients_per_year = patients_per_month * 12

# Calculate revenue recaptured for each improvement level
revenue_recaptured = [
    (patients_per_year * annual_revenue_per_patient * (baseline_denial_rate / 100) * (improvement / 100)) / 100000
    for improvement in denial_rate_improvements
]

# Prepare data for plotting
revenue_data_display = pd.DataFrame({
    'Denial Rate Improvement (%)': denial_rate_improvements,
    'Revenue Recaptured ($100,000s)': revenue_recaptured
})

# Plot
fig2 = px.line(
    revenue_data_display,
    x='Denial Rate Improvement (%)',
    y='Revenue Recaptured ($100,000s)',
    title='Revenue Recapture vs. Denial Rate Improvement',
    markers=True
)
fig2.update_layout(
    xaxis_title='Denial Rate Improvement (%)',
    yaxis_title='Revenue Recaptured ($100,000s)'
)
st.plotly_chart(fig2)

st.caption(f"""
**Calculation Logic:**
Revenue Recaptured = Patients per Year × Annual Cost per Patient × Baseline Denial Rate × Denial Rate Improvement (%)

- **Baseline Denial Rate:** {baseline_denial_rate}%
- **Annual Cost per Patient:** ${annual_revenue_per_patient:,.0f}
""")
