# 🌐 Live Dashboard
[Open the Supermarket Data Insights Dashboard](https://supermarket-datainsights-vaqrtmh93hk9ge348deohh.streamlit.app/)

---

# 📊 Product Sales & Profit Analysis Dashboard

This project is a **Streamlit dashboard** to visualize and analyze product sales and profit performance over time.  
It also includes a simple **Machine Learning regression model** to predict monthly profit based on historical data.

---

## 🎯 Features

- Filter products by **Description** or **Code**
- Select custom **date ranges**
- Visualize:
  - Monthly sales trends
  - Monthly profit trends
  - Units sold trends
  - Margin % distribution with boxplots and data points
- View **KPIs** (Total Units Sold, Total Sales, Total Profit, Average Margin)
- Train a **Linear Regression model** to predict Total Profit
- Inspect model metrics and coefficients

---

## How to Run (Step-by-Step Instructions)

💡 Tip:
You can do all the steps below either in:

- VS Code’s integrated terminal (recommended for convenience), or
- Command Prompt / PowerShell on Windows, or
- Terminal on Mac/Linux.

### 💻 1. Check Python Installation (must be version 3.7 or newer)

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

    python --version

or

    python3 --version

If Python is not installed or version is below 3.7, download and install from:  
👉 https://www.python.org/downloads/  
*Remember to check “Add Python to PATH” during installation on Windows.*

---

### 📂 2. Create Your Project Folder

Choose a place on your computer, e.g., your Desktop:

Example Windows folder:

    C:\Users\YourUsername\Desktop\ProductDashboard
    
---

### 🧪 3. Create a Virtual Environment (venv)

Virtual environments keep your project dependencies isolated.

Windows:

    python -m venv venv

Mac/Linux:

    python3 -m venv venv

---

### ✅ 4. Activate the Virtual Environment

Windows:

    venv\Scripts\activate

Mac/Linux:

    source venv/bin/activate

*You’ll know it’s active when your prompt starts with `(venv)`.*

---

### 📦 5. Install Required Python Packages

Make sure the virtual environment is activated, then run:

    pip install streamlit pandas matplotlib seaborn scikit-learn

---

### 🚀 6. Add Project Files

Place these files inside your `ProductDashboard` folder:

- `app.py` — your Streamlit dashboard code  
- `ModelSource.csv` — your data file

---

### 🛑 7. Run the Dashboard

Inside the project folder, with the venv activated, run:

    streamlit run app.py

This will open the dashboard automatically in your default browser at `http://localhost:8501`.  
If it doesn’t open, copy and paste that URL into your browser.

---

### 🧹 8. Stop the Server

When done, go back to your terminal and press:

    Ctrl + C

---

## Summary Checklist

- [x] Python 3.7+ installed  
- [x] Project folder created  
- [x] Virtual environment created and activated  
- [x] Packages installed inside venv  
- [x] `app.py` and `ModelSource.csv` added  
- [x] Dashboard running with `streamlit run app.py`  

---

