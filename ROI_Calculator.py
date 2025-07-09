# Revenue Generated from Lamar PA Submissions
st.header("Revenue Generated from Lamar PA Submissions")

# Define actual submitted volume based on user input
submitted_volume = patients_per_month * 12
max_volume = math.ceil(submitted_volume / 150000) * 150000 + 150000
pa_range = list(range(submitted_volume, max_volume + 1, 150000))

revenue_baseline = [
    (pa * (baseline_approval_rate / 100) * annual_revenue_per_patient * years) / 1_000_000
    for pa in pa_range
]
revenue_improved = [
    (pa * (improved_approval_rate / 100) * annual_revenue_per_patient * years) / 1_000_000
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
    value_name="Revenue Generated ($M)"
)

fig2 = px.line(
    revenue_df_melted,
    x="PA's Submitted Annually",
    y="Revenue Generated ($M)",
    color="Scenario",
    title="Revenue Generated vs. PA's Submitted Annually",
    markers=True
)

# Dynamic Y scaling with fixed max of $100M
y_max = max(revenue_baseline + revenue_improved)
y_cap = 100 if y_max <= 100 else math.ceil(y_max / 10) * 10
fig2.update_layout(
    xaxis_title="PA's Submitted Annually",
    yaxis_title="Revenue Generated ($M)",
    xaxis=dict(tickmode='linear', tick0=0, dtick=150000),
    yaxis=dict(tickmode='linear', tick0=0, dtick=10, range=[0, y_cap]),
    legend_title='Scenario'
)

st.plotly_chart(fig2)

st.caption("""
**Calculation Logic:**
Revenue = PA’s Submitted Annually × Approval Rate × Revenue per PA × Time Horizon  
Chart values shown in **$1M units**, starting from your selected PA volume.
""")
