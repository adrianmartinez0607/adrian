import streamlit as st
import pandas as pd
import plotly.express as px
import math

# Sidebar inputs
st.sidebar.title("Lamar Health ROI Calculator")

patients_per_month = st.sidebar.number_input("Number of Patients per Month", value=200)
hourly_salary = st.sidebar.number_input("Hourly Salary ($)", value=22)
years = st.sidebar.number_input("Time Horizon (Years)", value=3)

# Module toggles and costs
enable_fax = st.sidebar.checkbox("Include Fax Processing", value=True)
st.sidebar.caption("**Fax Processing Formula:** Before: 15 min × patients/month × hourly wage\nAfter: $fax price + 1 min × patients/month × hourly wage")
fax_price = st.sidebar.number_input("Lamar Fax Processing Price ($)", value=2.00)

enable_benefit = st.sidebar.checkbox("Include Benefit Check", value=True)
st.sidebar.caption("**Benefit Check Formula:** Before: 30 min × patients/month × hourly wage\nAfter: $benefit check price + 1 min × patients/month × hourly wage")
benefit_price = st.sidebar.number_input("Lamar Benefit Check Price ($)", value=5.00)

enable_auth = st.sidebar.checkbox("Include Prior Authorization", value=True)
st.sidebar.caption("**Prior Authorization Formula:** Before: 40 min × patients/month × hourly wage\nAfter: $prior auth price + 1 min × patients/month × hourly wage")
auth_price = st.sidebar.number_input("Lamar Prior Authorization Price ($)", value=6.00)

enable_order_entry = st.sidebar.checkbox("Include Order Entry Automation", value=True)
st.sidebar.caption("**Order Entry Formula:** Before: 4 min × patients/month × hourly wage\nAfter: $order entry price + 0.5 min × patients/month × hourly wage")
order_entry_price = st.sidebar.number_input("Lamar Order Entry Price ($)", value=1.50)

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
cost_after_order_entry = (order_entry_price + order_entry_time_after * minutes_to_hours * hourly_salary) * patients*_
