# ❄️ Air Conditioner Energy Cost Estimator

A machine learning-powered web application that estimates an air conditioner's monthly electricity consumption (kWh) and operating cost (₱) based on its specifications and daily usage.

Built using **Python**, **scikit-learn**, and **Streamlit**, this project applies a **Random Forest Regressor** to provide more realistic energy consumption estimates than fixed-hour calculations.

## ✨ Features
- Predicts monthly electricity consumption (kWh)
- Estimates monthly electricity cost (₱)
- Supports customizable daily usage hours
- Simple and interactive Streamlit web interface

## 📊 Dataset
The model was trained using data from the **Philippine Government's certified room air conditioner database**.

### Input Features
- **Power Rating (W)**
- **Cooling Seasonal Performance Factor (CSPF)**
- **Hours Used per Day**

### Target
- **Monthly Energy Consumption (kWh)**

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 🤖 Machine Learning Model
- **Algorithm:** Random Forest Regressor
- **Methodology:** CRISP-DM
- **Train/Test Split:** 80/20

## 🚀 Future Improvements
- Hyperparameter tuning with GridSearchCV
- Include room size and ambient temperature
- Integrate real-time electricity rates
- Improve prediction accuracy with additional data

---
Developed by **Ummair Ansari** as a Data Science course project at **Mapúa Malayan Colleges Mindanao**.
