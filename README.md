# 🌟 Supermarket Santa Clara Data Analysis, Modeling, and Dashboard

Welcome to the **Supermarket Santa Clara Data Analysis, Modeling, and Dashboard** project, a comprehensive data science pipeline applied to real-world supermarket sales data. This project covers data wrangling, exploratory analysis, product segmentation, predictive modeling, and interactive dashboard development, delivering actionable insights for sales performance and decision-making.

---

## 🚀 Project Overview

The primary objective of this project is to analyze and forecast product sales and profitability by transforming raw sales transactions into structured insights. The project includes:

- A full **data wrangling and cleaning process**
- **Exploratory Data Analysis (EDA)** to uncover sales and profitability patterns
- **Product Segmentation** to classify items by performance
- A **machine learning model** to predict product sales
- An **interactive Streamlit dashboard** for real-time analysis and visualization
- A **final presentation** summarizing the project workflow and insights

---

## 📥 About The Dataset

The dataset consists of monthly sales data exported from the company’s internal transaction management system (**Linear Systems**) covering **April 2024 to April 2025**. It contains:

- Product codes and descriptions (originally in Portuguese)
- Sales dates, quantities sold, unit costs, and unit prices
- Total sales and profit metrics
- Margin percentages and other profitability indicators

---

## 🔍 Key Project Components

### 🛠️ 1. Data Wrangling & Cleaning
- Translated product descriptions from Portuguese to English using `deep-translator`
- Standardized inconsistent numeric formats (e.g., comma vs period separators)
- Converted data types for reliable analysis
- Removed invalid or missing data rows
- Ensured clean, uniform data ready for visualization and modeling

### 📈 2. Exploratory Data Analysis (EDA)
- Analyzed **March 2025** sales as an example period
- Identified top-selling and low-profit products
- Visualized margin distributions to detect pricing anomalies
- Created a **product segmentation (A, B, C, D categories)** based on normalized performance metrics

### 🔢 3. Predictive Modeling
- Developed machine learning models (**Random Forest, Linear Regression, SVR**) to forecast product-level sales
- Engineered features including lagged sales, rolling averages, and time encodings
- Used historical data from **April 2024 to March 2025** to predict sales for **April 2025**
- Random Forest Regressor achieved the best accuracy (**R² ≈ 0.87**), confirming the feasibility of sales forecasting based on historical patterns

### 🌐 4. Interactive Dashboard (Streamlit)
- Built a user-friendly **Streamlit app** to explore sales, profit, and predictions dynamically
- Filters by product and date range to drill into specific product performance
- Displays KPIs, sales trends, and the model’s profit predictions
- ⚠️ **The dashboard has its own README** explaining how to install dependencies and run the app step by step

### 🎯 5. Final Presentation
- Summarized the full workflow and results in a clear, business-focused presentation
- Highlighted key visualizations, model performance, and actionable insights for decision-makers

---

## 🧠 Techniques & Tools Used

- **Python Libraries:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `Streamlit`, `Deep-translator`
- **Data Engineering:** String manipulation, date processing, categorical encoding, lag features
- **Modeling:** Supervised regression models (Random Forest, SVR, Linear Regression), feature selection, and evaluation with R² and MAE
- **Visualization:** Interactive dashboards (Streamlit) and static plots

---

## 📊 Outcome

This project equips business users and analysts with:
- Insights into product performance and profit margins
- A clear segmentation of top and low-performing items
- A predictive model for future sales planning
- An interactive dashboard to explore results without needing to code
- A structured presentation to share results with stakeholders

---

## 🚀 How to Run
First of all, download the source files in the folder 'processed', and then:

### ➤ Data Wrangling & EDA
1. Clone or download this repository.
2. Open the Jupyter notebooks (`Data_Wrangling.ipynb`, `Data_Visualization.ipynb`).
3. Run the notebooks step by step to process and analyze the data.

### ➤ Predictive Modeling
1. Open the `Model.ipynb` notebook.
2. Run all cells to train and evaluate the models.

### ➤ Streamlit Dashboard
1. Navigate to the `dashboard/` folder.
2. Follow the step-by-step instructions in the **dashboard’s own README** to install dependencies and run the app.

---

## 📞 Contact

Feel free to reach out if you want to discuss the project or collaborate!

📧 **Email:** [alcantaracaio99@gmail.com](mailto:alcantaracaio99@gmail.com)  
🔗 **LinkedIn:** https://www.linkedin.com/in/caio-alcântara/
