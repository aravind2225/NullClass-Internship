# Dynamic Pricing System for Businesses using Machine Learning  

## 📌 Project Overview  
Traditional static pricing fails to adapt to fluctuating demand, supply, and competitor actions, leading to revenue loss.  
This project introduces a **Dynamic Pricing System** that continuously adjusts prices using **Machine Learning (XGBoost)**.  
The system is deployed with **FastAPI** and integrated with a **web interface** to ensure competitive, adaptive, and profit-optimized pricing.  

---

## 🚀 Problem Statement  
- Static pricing ignores market fluctuations.  
- Leads to **revenue loss** during peak demand or surplus supply.  
- Fails to adapt to **demand-supply variations** and seasonal changes.  
- Need a system that enables **real-time pricing adjustments**.  

---

## 🔎 Proposed Methodology  
- Dataset: **Bike Taxi’s Business Dataset** (Rapido rides).  
- Preprocessing & **Exploratory Data Analysis (EDA)** for demand-supply patterns.  
- Calculate **demand & supply multipliers**:  
  - High demand → price increases  
  - Low demand → price decreases  
- Apply thresholds to avoid extreme pricing.  
- Final ride cost = **historical cost × demand multiplier × supply multiplier**.  
- Deployed via **FastAPI** for real-time predictions.  

---

## ⚙️ Experimental Setup  
- **Data Collection**: Rapido bike taxi rides dataset.  
- **Preprocessing**: Cleaning, feature engineering, handling outliers.  
- **Modeling**: XGBoost algorithm chosen for best performance.  
- **Deployment**: Real-time prediction service using **FastAPI** + Web interface.  

---

## 💻 Tech Stack  
- **Backend**: FastAPI (Python)  
- **Frontend**: HTML, CSS, JavaScript  
- **Data Analysis & Modeling**: Pandas, NumPy, Scikit-learn, XGBoost  
- **Visualization**: Plotly Express  
- **Data Cleaning**: MS Excel  

---

## 🧠 Algorithm Used: XGBoost  
- Ensemble of decision trees.  
- Efficient for large datasets.  
- Captures **demand-supply relationships** effectively.  
- Robust, accurate, and scalable for real-world applications.  

---

## 📊 Use Case Scenarios  
- **E-commerce**: Frequent price updates.  
- **Travel & Hospitality**: Airlines, hotels.  
- **Ride-sharing**: Surge pricing.  
- **Energy sector**: Real-time electricity rates.  
- **Entertainment**: Automated ticket price adjustments.  

---

## ✅ Conclusion  
- The **XGBoost-based dynamic pricing system** provides an accurate, scalable, and practical solution for businesses.  
- Prices update **instantly** based on demand and supply, unlike static/manual updates.  
- Ensures **competitiveness and maximized revenue** in real-world applications.  

---

## 👨‍💻 Author  
**Aravind Udiyana**  
*Summer Intern Project – August 2025*  
