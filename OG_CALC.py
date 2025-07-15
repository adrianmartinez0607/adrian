import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")

patients_per_month = st.sidebar.number_input("Number of Patients per Month", value=200)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=3)

# Module toggles with prices and formulas
enable_fax = st.sidebar.checkbox("Include Fax Processing", value=True)
st.sidebar.caption("**Fax Processing Formula:**\nBefore: 15 min × patients/month × hourly wage\nAfter: $fax price + 1 min × patients/month × hourly wage")
fax_price = st.sidebar.number_input("Lamar Fax Processing Price ($)", value=2)

enable_benefit = st.sidebar.checkbox("Include Benefit Check", value=True)
st.sidebar.caption("**Benefit Check Formula:**\nBefore: 30 min × patients/month × hourly wage\nAfter: $benefit check price + 1 min × patients/month × hourly wage")
benefit_price = st.sidebar.number_input("Lamar Benefit Check Price ($)", value=5)

enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:**\nBefore: 40 min × patients/month × hourly wage\nAfter: $prior auth price + 1 min × patients/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=6)

enable_order_entry = st.sidebar.checkbox("Include Order Entry Automation", value=True)
st.sidebar.caption("**Order Entry Formula:**\nBefore: 4 min × patients/month × hourly wage\nAfter: $order entry price + 0.5 min × patients/month × hourly wage")
order_entry_price = st.sidebar.number_input("Lamar Order Entry Price ($)", value=1.50)

# Constants
months = years * 12
minutes_to_hours = 1 / 60

# Time per task (in minutes)
fax_time = 15
benefit_time = 30
auth_time = 40
post_lamar_time = 1
order_entry_time_before = 4
order_entry_time_after = 0.5

# Cost before Lamar
cost_before_fax = fax_time * minutes_to_hours * patients_per_month * hourly_salary * months if enable_fax else 0
cost_before_benefit = benefit_time * minutes_to_hours * patients_per_month * hourly_salary * months if enable_benefit else 0
cost_before_auth = auth_time * minutes_to_hours * patients_per_month * hourly_salary * months if enable_auth else 0
cost_before_order_entry = order_entry_time_before * minutes_to_hours * patients_per_month * hourly_salary * months if enable_order_entry else 0
cost_before_total = cost_before_fax + cost_before_benefit + cost_before_auth + cost_before_order_entry

# Cost after Lamar
cost_after_fax = (fax_price + post_lamar_time * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_fax else 0
cost_after_benefit = (benefit_price + post_lamar_time * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_benefit else 0
cost_after_auth = (auth_price + post_lamar_time * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_auth else 0
cost_after_order_entry = (order_entry_price + order_entry_time_after * minutes_to_hours * hourly_salary) * patients_per_month * months if enable_order_entry else 0
cost_after_total = cost_after_fax + cost_after_benefit + cost_after_auth + cost_after_order_entry

# Summary metrics
savings = cost_before_total - cost_after_total
time_saved_hours = savings / hourly_salary if hourly_salary != 0 else 0
roi_percent = (savings / cost_before_total) * 100 if cost_before_total != 0 else 0

# Display summary
st.title("Lamar Health ROI Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Time Saved (Hours)", f"{time_saved_hours:,.2f}")
col2.metric("Cost Savings ($)", f"${savings:,.2f}")
col3.metric("ROI (%)", f"{roi_percent:.2f}%")

# Cost over time chart
months_range = list(range(1, months + 1))
costs_before = [((fax_time * int(enable_fax) +
                  benefit_time * int(enable_benefit) +
                  auth_time * int(enable_auth) +
                  order_entry_time_before * int(enable_order_entry))
                 * minutes_to_hours * patients_per_month * hourly_salary) * m for m in months_range]

costs_after = [((fax_price * int(enable_fax) +
                 benefit_price * int(enable_benefit) +
                 auth_price * int(enable_auth) +
                 order_entry_price * int(enable_order_entry)) +
                (post_lamar_time * (int(enable_fax) + int(enable_benefit) + int(enable_auth)) +
                 order_entry_time_after * int(enable_order_entry)) * minutes_to_hours * hourly_salary)
               * patients_per_month * m for m in months_range]

df_plot = pd.DataFrame({
    'Month': months_range,
    'Cost Before Lamar': costs_before,
    'Cost After Lamar': costs_after
})

fig = px.line(
    df_plot,
    x='Month',
    y=['Cost Before Lamar', 'Cost After Lamar'],
    title='Cost Over Time',
    labels={'value': 'Cost ($)', 'Month': 'Month', 'variable': 'Scenario'},
    markers=True
)
fig.update_layout(xaxis_title='Month', yaxis_title='Cost ($)', legend_title='Scenario')
st.plotly_chart(fig)

st.write("Lamar Health offers automation solutions across four modules: Fax Processing, Benefit Check, Prior Authorization, and Order Entry Automation. Customize the inputs on the left to see how much you can save.")

# Revenue Recapture section
st.header("Revenue Recapture from Policy Review")
denial_rates = [x / 100 for x in range(1, 21)]
patients_per_year = patients_per_month * 12
revenue_per_patient = 80000
revenue_recaptured = [(patients_per_year * revenue_per_patient * rate) / 100000 for rate in denial_rates]

df_revenue = pd.DataFrame({
    'Denial Rate Improvement (%)': [r * 100 for r in denial_rates],
    'Revenue Recaptured ($100,000s)': revenue_recaptured
})

fig2 = px.line(
    df_revenue,
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

st.caption("""
**Calculation Logic:**
Revenue Recaptured = Number of Patients per Year × $80,000 (estimated chronic care revenue per patient) × Denial Rate Improvement (%)
This assumes each patient contributes $80,000 annually and that improvement in denial rates results in direct revenue recovery.
""")
