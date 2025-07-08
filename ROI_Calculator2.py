# Revenue Recapture from Lamar PA Submissions
st.header("Revenue Recapture from Lamar PA Submissions")

# Editable inputs
baseline_denial_rate = st.sidebar.number_input("Baseline Denial Rate (%)", value=60, min_value=0, max_value=100, step=1)
annual_revenue_per_patient = st.sidebar.number_input("Annual Estimated Cost per Patient ($)", value=80000, step=1000)

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
