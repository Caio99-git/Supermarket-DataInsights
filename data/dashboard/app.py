# Install the required packages using - pip install streamlit pandas matplotlib seaborn scikit-learn
# to run - streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Set page title and layout to wide screen
st.set_page_config(page_title="Product Performance & ML Dashboard", layout="wide")

# Title and description at the top of the dashboard
st.title("Product Sales & Profit Analysis Dashboard")
st.markdown("Select a product and date range to analyze sales/profit and see ML regression predicting total profit.")

# Load data once and cache it to improve performance
@st.cache_data
def load_data():
    return pd.read_csv("data/dashboard/ModelSource.csv")

df = load_data()

# Keep only data between Apr 2024 - Apr 2025
df = df[((df['Year'] == 2024) & (df['Month'] >= 4)) | ((df['Year'] == 2025) & (df['Month'] <= 3))]

# Sidebar section
st.sidebar.header("Filters")

# Selection method: either by product Description or product Code
search_mode = st.sidebar.radio("Search by:", ["Description", "Code"])

if search_mode == "Description":
    # Create dropdown with all unique product descriptions
    options = sorted(df["Description"].unique())
    selection = st.sidebar.selectbox("Select Product Description", options)
    # Filter data to only include selected description
    df_filtered = df[df["Description"] == selection]

else:
    # Create dropdown with all unique product codes
    options = sorted(df["Code"].unique())
    selection = st.sidebar.selectbox("Select Product Code", options)
    df_filtered = df[df["Code"] == selection]
    
    # After filtering by code, retrieve the corresponding product description
    # This helps later to display product name consistently even if the selection was by code
    if not df_filtered.empty:
        selection = df_filtered["Description"].iloc[0]

# Show warning and stop app if no data found for selected product
if df_filtered.empty:
    st.warning("No data for selected product.")
    st.stop()

# Build month selection options: Apr-Dec 2024 and Jan-Apr 2025
allowed_months = [(y, m) for y in [2024, 2025] for m in (range(4, 13) if y == 2024 else range(1, 4))]

# Convert tuple (year, month) to a readable label like "April 2024"
def ym_to_label(ym): 
    return pd.to_datetime(f"{ym[0]}-{ym[1]:02d}-01").strftime("%B %Y")

month_labels = [ym_to_label(ym) for ym in allowed_months]
month_map = dict(zip(month_labels, allowed_months))  # Map labels back to year-month tuple

# Select start and end month in sidebar
start_label = st.sidebar.selectbox("Start Month", month_labels, index=0)
end_label = st.sidebar.selectbox("End Month", month_labels, index=len(month_labels)-1)

# Retrieve year-month tuples for filtering
start_ym, end_ym = month_map[start_label], month_map[end_label]

# Ensure that end month is not earlier than start month
if end_ym < start_ym:
    st.sidebar.error("End month must be same or after start month.")
    st.stop()

# Filter rows that fall within the selected year-month range
# Each row’s year and month is compared as a tuple (Year, Month)
df_range = df_filtered[df_filtered.apply(lambda r: start_ym <= (r['Year'], r['Month']) <= end_ym, axis=1)]

# Show warning if no data in selected month range
if df_range.empty:
    st.warning("No data in selected range.")
    st.stop()

# KPIs (Key Performance Indicators)
st.subheader(f"KPIs for {selection} from {start_label} to {end_label}")

# Aggregate metrics
total_units = df_range['Amount_Sold'].sum()
total_sales = df_range['Total_Sale'].sum()
total_profit = df_range['Total_Profit'].sum()
avg_margin = df_range['Margin%'].mean()

# Display KPIs in 4 columns
cols = st.columns(4)
cols[0].metric("Total Units Sold", f"{total_units:,.0f}")
cols[1].metric("Total Sales ($)", f"${total_sales:,.2f}")
cols[2].metric("Total Profit ($)", f"${total_profit:,.2f}")
cols[3].metric("Avg Margin %", f"{avg_margin:.2f}%")

# Prepare data for time series analysis
monthly = df_range.groupby(['Year', 'Month']).agg({
    'Amount_Sold': 'sum',
    'Total_Sale': 'sum',
    'Total_Profit': 'sum',
    'Margin%': 'mean',
    'Unit_Cost': 'mean',
    'Unit_Profit': 'mean'
}).reset_index()

# Create a date column for plotting and sort chronologically
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(DAY=1))
monthly = monthly.sort_values("Date")

# Also create YearMonth string for plotting boxplot
monthly["YearMonth"] = monthly.apply(lambda r: f"{r['Year']}-{r['Month']:02d}", axis=1)

# Reusable function to generate line plots
def plot_line(x, y, title, ylabel, color=None):
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=x, y=y, marker="o", color=color, ax=ax)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    st.pyplot(fig)

# Generate 3 time-series trend plots
plot_line(monthly["Date"], monthly["Total_Sale"], "Monthly Sales Trend", "Total Sales ($)")
plot_line(monthly["Date"], monthly["Total_Profit"], "Monthly Profit Trend", "Total Profit ($)", color="green")
plot_line(monthly["Date"], monthly["Amount_Sold"], "Monthly Units Sold Trend", "Units Sold", color="orange")

# Boxplot + Swarmplot: margin % per month
st.subheader("Margin % Distribution with Data Points")

# The boxplot shows summary stats: median, IQR, and outliers.
sns.boxplot(x='YearMonth', y='Margin%', data=monthly, color="skyblue")

# The swarmplot overlays individual data points on top of the boxplot.
# It gives a clearer idea of actual data distribution each month.
sns.swarmplot(x='YearMonth', y='Margin%', data=monthly, color="black", size=6, alpha=0.7)

plt.xticks(rotation=45)
plt.title("Margin % per Month")
plt.xlabel("Month")
plt.ylabel("Margin %")

# IMPORTANT: plt.gcf() means "get current figure" — it retrieves the latest matplotlib figure that’s currently active
# This is necessary if you're using the state-based interface (like plt.figure()) instead of explicitly storing fig
st.pyplot(plt.gcf())

# Regression Model using Scikit-learn to predict monthly Total Profit
st.subheader("Predicting Total Profit per Month (Regression Model)")

# Select features and target
features = ["Amount_Sold", "Unit_Cost", "Unit_Profit", "Margin%"]
X = monthly[features]
y = monthly["Total_Profit"]

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Evaluate model with MAE and R2 score
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Show evaluation metrics
cols = st.columns(2)
cols[0].metric("Mean Absolute Error", f"${mae:,.2f}")
cols[1].metric("R2 Score", f"{r2:.2f}")

# Display feature coefficients to interpret model behavior
coef_df = pd.DataFrame({"Feature": features, "Coefficient": model.coef_})
st.write("Model Coefficients:")
st.dataframe(coef_df)

# Plot actual vs predicted profit values over time
fig, ax = plt.subplots(figsize=(10,4))
sns.lineplot(x=monthly["Date"], y=y, marker="o", label="Actual", ax=ax)
sns.lineplot(x=monthly["Date"], y=y_pred, marker="o", label="Predicted", color="red", ax=ax)
ax.set_title("Actual vs Predicted Total Profit")
ax.set_ylabel("Total Profit ($)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Expandable section with raw data table
with st.expander("Raw Data for Selected Range"):
    st.dataframe(df_range)
