# 🛍️ Retail Sales & Inventory Copilot

An AI-powered retail analytics dashboard built with **Streamlit, Pandas, and Gemini AI** to help businesses understand sales performance, monitor inventory, and make data-driven decisions.

## 🚀 Project Overview

**Retail Sales & Inventory Copilot** is a smart retail management dashboard that combines sales analytics, inventory monitoring, AI-powered insights, and demand prediction in one place.

The application helps users:

* 📊 Analyze sales and revenue performance
* 📦 Monitor inventory health
* 🚨 Identify low-stock products
* 🏆 Find best-selling products
* 🤖 Ask questions using an AI retail copilot
* 🔮 Predict next-day sales using recent sales trends
* 🔎 Search and inspect product-level sales details

## ✨ Key Features

### 📊 Sales Intelligence

Visualizes product-wise and category-wise revenue using interactive charts.

### 🚨 Inventory Radar

Classifies inventory into:

* 🔴 Critical
* 🟠 Warning
* 🟢 Healthy

This makes it easier to identify products that may need restocking.

### 📌 Business Pulse

Provides quick business KPIs such as:

* 💰 Total Revenue
* 📦 Units Sold
* 🚨 Low Stock Count
* 🏆 Best-Selling Product

### 🤖 Retail Copilot

An AI-powered assistant using **Gemini** that answers questions based on the selected sales and inventory information.

Example questions:

* Which product is selling the most?
* Which products need restocking?
* What is the total revenue?
* How many units were sold?

### 🔮 Sales Prediction

Uses the average sales of the last 7 available days to estimate next-day sales.

### 🔎 Product Search

Allows users to select a product and view its total units sold, revenue, and sales records.

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Google Gemini API**
* **HTML/CSS** for custom UI styling

## 📁 Project Structure

```text
Retail-Sales-Inventory-Copilot/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    ├── sales.csv
    └── inventory.csv
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hasinimanickam/Retail-Sales-Inventory-Copilot.git
cd Retail-Sales-Inventory-Copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

> ⚠️ Do not upload `secrets.toml` or your API key to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Data Used

The project uses two CSV files:

### `sales.csv`

Contains sales transaction information such as:

* Date
* Product
* Category
* Quantity
* Price

### `inventory.csv`

Contains inventory information such as:

* Product
* Stock
* Reorder Level

## 🎯 Problem Solved

Retail businesses often have sales and inventory data but lack a simple way to turn that data into actionable insights.

This project provides a single dashboard to help users:

**Understand → Monitor → Predict → Act**

## 💡 Future Improvements

* Advanced time-series forecasting
* Automated reorder quantity recommendations
* Sales trend anomaly detection
* Profit and margin analysis
* Downloadable business reports
* Real-time database integration
* More advanced AI-driven recommendations

## 👩‍💻 Author

**Hasini Manickam**

B.Tech Artificial Intelligence & Data Science

## ⭐ Acknowledgement

Built as a hackathon project to explore the use of **AI and data analytics for smarter retail decision-making**.
