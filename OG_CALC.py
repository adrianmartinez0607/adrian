-import streamlit as st
import pandas as pd
import plotly.express as px
import math

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")

patients_per_month = st.sidebar.number_input("Number of Patients per Month", value=200)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=2)

# Module toggles and costs
enable_fax = st.sidebar.checkbox("Include Fax Processing", value=True)
st.sidebar.caption("**Fax Processing Formula:** Before: 15 min × patients/month × hourly wage\nAfter: $fax price + 1 min × patients/month × hourly wage")
fax_price = st.sidebar.number_input("Lamar Fax Processing Price ($)", value=.50)

enable_benefit = st.sidebar.checkbox("Include Benefit Check", value=True)
st.sidebar.caption("**Benefit Check Formula:** Before: 30 min × patients/month × hourly wage\nAfter: $benefit check price + 1 min × patients/month × hourly wage")
benefit_price = st.sidebar.number_input("Lamar Benefit Check Price ($)", value=10.00)

enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:** Before: 40 min × patients/month × hourly wage\nAfter: $prior auth price + 1 min × patients/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=10.00)

enable_order_entry = st.sidebar.checkbox("Include Order Entry Automation", value=True)
st.sidebar.caption("**Order Entry Formula:** Before: 4 min × patients/month × hourly wage\nAfter: $order entry price + 0.5 min × patients/month × hourly wage")
order_entry_price = st.sidebar.number_input("Lamar Order Entry Price ($)", value=.50)

# Revenue inputs
st.sidebar.markdown("---")
baseline_approval_rate = st.sidebar.number_input("Baseline Approval Rate (%)", value=40, min_value=0, max_value=100)
improved_approval_rate = st.sidebar.number_input("Improved Approval Rate (%)", value=46, min_value=0, max_value=100)
annual_revenue_per_patient = st.sidebar.number_input("Annual Revenue per PA Processed ($)", value=10000, step=1000)

# Constants
months = years * 12
minutes_to_hours = 1 / 60
patients_per_year = patients_per_month * 12

fax_time = 15
benefit_time = 30
auth_time = 40
post_lamar_time = 1
order_entry_time_before = 4
order_entry_time_after = 0.5  # <-- THIS LINE FIXES THE ERROR

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

# Summary
savings = cost_before_total - cost_after_total
time_saved_hours = savings / hourly_salary if hourly_salary else 0
roi_percent = (savings / cost_before_total) * 100 if cost_before_total else 0

# Revenue Gain
approval_improvement = max(0, (improved_approval_rate - baseline_approval_rate) / 100)
revenue_generated = patients_per_year * annual_revenue_per_patient * approval_improvement * years
rounded_revenue = math.ceil(revenue_generated / 100000) * 100000
revenue_display = f"${rounded_revenue / 1_000_000:.2f}M" if rounded_revenue < 1_000_000_000 else f"${rounded_revenue / 1_000_000_000:.2f}B"

# Display summary
st.title("Lamar Health ROI Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Time Saved (Hours)", f"{time_saved_hours:,.2f}")
col2.metric("Cost Savings ($)", f"${savings:,.2f}")
col3.metric("Revenue Generated ($)", revenue_display)

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

df_costs = pd.DataFrame({
    'Month': months_range,
    'Cost Before Lamar': costs_before,
    'Cost After Lamar': costs_after
})
fig1 = px.line(df_costs, x='Month', y=['Cost Before Lamar', 'Cost After Lamar'],
               title='Cost Over Time', markers=True,
               labels={'value': 'Cost ($)', 'variable': 'Scenario'})
st.plotly_chart(fig1)

# Revenue Generated from Approvals
st.header("Revenue Generated from Approvals")

max_pas = patients_per_month * 12 * years
step_size = max(1000, int(max_pas / 10))
pa_range = list(range(0, max_pas + 1, step_size))

baseline_rev = [pa * (baseline_approval_rate / 100) * (annual_revenue_per_patient * years) / 1_000_000 for pa in pa_range]
improved_rev = [pa * (improved_approval_rate / 100) * (annual_revenue_per_patient * years) / 1_000_000 for pa in pa_range]

df_revenue = pd.DataFrame({
    "PA's Submitted": pa_range,
    f"Baseline Revenue ({baseline_approval_rate}%)": baseline_rev,
    f"Revenue Recaptured ({improved_approval_rate}%)": improved_rev
}).melt(id_vars="PA's Submitted", var_name="Scenario", value_name="Revenue Generated ($M)")

fig2 = px.line(df_revenue, x="PA's Submitted", y="Revenue Generated ($M)", color="Scenario",
               title="Revenue Generated from Approvals", markers=True)
st.plotly_chart(fig2)

st.caption("""
**Calculation Logic:**

Baseline Revenue = PA's Submitted × Baseline Approval Rate × Annual Revenue per PA × Time Horizon  
Revenue Recaptured = PA's Submitted × Improved Approval Rate × Annual Revenue per PA × Time Horizon  
Chart values are in **$Millions ($M)**.
""")
