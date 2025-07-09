# Revenue Generated from Lamar PA Submissions
st.header("Revenue Generated from Lamar PA Submissions")

# Generate chart data: X-axis = PA's submitted annually (0 to 750k in steps of 150k)
pa_range = list(range(0, 750001, 150000))  # 0 to 750,000 in 150,000 increments

revenue_baseline = [
    (pa * annual_revenue_per_patient * (baseline_approval_rate / 100) * years) / 10000000
    for pa in pa_range
]
revenue_improved = [
    (pa * annual_revenue_per_patient * (improved_approval_rate / 100) * years) / 10000000
    for pa in pa_range
]

revenue_df = pd.DataFrame({
    "PA's Submitted Annually": pa_range,
    f'Baseline Approval Rate ({baseline_approval_rate}%)': revenue_baseline,
    f'Improved Approval Rate ({improved_approval_rate}%)': revenue_improved
})

revenue_df_melted = revenue_df.melt(
    id_vars="PA's Submitted Annually",
    var_name="Scenario",
    value_name="Revenue Generated ($10M)"
)

fig2 = px.line(
    revenue_df_melted,
    x="PA's Submitted Annually",
    y="Revenue Generated ($10M)",
    color="Scenario", 
    title="Revenue Generated vs. PA's Submitted Annually",
    markers=True
)

fig2.update_layout(
    xaxis_title="PA's Submitted Annually",
    yaxis_title="Revenue Generated ($10M)",
    xaxis=dict(tickmode='linear', tick0=0, dtick=150000),
    legend_title="Scenario"
)

st.plotly_chart(fig2)

st.caption("""
**Calculation Logic:**
Revenue Generated = PA’s Submitted Annually × Annual Revenue per PA × Approval Rate × Time Horizon

Chart values are expressed in **$10M units**.
""")
