# 🌍 Climate Vulnerability Analysis Dashboard (Africa Region)

An interactive Streamlit dashboard that analyzes and compares climate indicators across five African countries (Ethiopia, Sudan, Tanzania, Nigeria, and Kenya) from 2015–2026. The project focuses on temperature trends, precipitation variability, and extreme climate events to support climate vulnerability assessment and decision-making.

---

## 🚀 Live Demo
👉 [Streamlit App](https://your-streamlit-app-link-here)

---

## 📊 Project Objective

This project aims to:
- Compare climate patterns across multiple countries
- Analyze temperature trends (T2M, T2M_MAX, T2M_MIN)
- Study precipitation variability (PRECTOTCORR)
- Detect extreme climate events (heat and drought)
- Provide a data-driven vulnerability overview for policy insights (COP32 context)

---

## 🗂️ Project Structure
climate-challenge-week0/
│
├── app/
│ ├── main.py # Streamlit application entry point
│ ├── utils.py # Data loading and filtering functions
│
├── data/
│ ├── ethiopia_clean.csv
│ ├── sudan_clean.csv
│ ├── tanzania_clean.csv
│ ├── nigeria_clean.csv
│ ├── kenya_clean.csv
│
├── scripts/
│ └── README.md
│
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files and folders
└── README.md # Project documentation

---

## ⚙️ Features

### 🌡️ Climate Analysis
- Temperature trend comparison across countries
- Monthly and yearly climate visualization

### 🌧️ Precipitation Analysis
- Distribution of rainfall patterns
- Variability and extreme rainfall detection

### 🔥 Extreme Events
- Extreme heat days (T2M_MAX > 35°C)
- Dry days (PRECTOTCORR < 1mm)

### 📊 Interactive Dashboard
- Country multi-select filter
- Year range slider
- Variable selector (temperature, rainfall, wind, humidity)
- Dynamic visualizations using Plotly

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly

---

## 📦 Installation (Local Setup)

```bash
# Clone repository
git clone https://github.com/your-username/climate-dashboard.git

# Navigate to project
cd climate-dashboard

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/main.py