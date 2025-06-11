# 🚘 Car Price Prediction Web App

This is a **Car Price Prediction** web application built using **Streamlit** and a **Linear Regression** model. It predicts the estimated selling price of a used car based on various user-provided specifications.

---

## 🔗 Live Demo

👉 [Click here to try the app](https://car-price-prediction-tjkkgddgjc66um4aewkncg.streamlit.app/)

---

## 📌 Features

- Predicts car resale price based on key features:
  - Year of manufacture
  - Seller type (Dealer / Individual / Trustmark)
  - Kilometers driven
  - Fuel type (Petrol / Diesel / CNG / LPG / Electric)
  - Transmission type (Manual / Automatic)
  - Mileage (in kmpl or km/kg)
  - Engine capacity (in CC)
  - Maximum power (in bhp)
  - Number of seats

---

## 🤖 Machine Learning Model

- **Model Used:** Linear Regression
- **Preprocessing:**
  - Handled missing values
  - Encoded categorical variables
  - Scaled numerical features
- **Training:** The model was trained using historical car data to learn the relationship between features and price.

---

## 🛠️ Technologies Used

- **Frontend:** Streamlit (for UI)
- **Backend/ML:** Python, Scikit-learn
- **Libraries:** Pandas, NumPy, Matplotlib (optional)
- **Deployment:** Streamlit Cloud

---

## 🧪 How to Run Locally

Follow these steps to run the project on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/mrankit560/Car-Price-Prediction.git
cd Car-Price-Prediction

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate           # On Windows use: venv\Scripts\activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run Car_Price.py

# 5. Open your browser and go to
# http://localhost:8501
