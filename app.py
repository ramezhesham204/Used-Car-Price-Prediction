import streamlit as st
import pandas as pd
import joblib

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS for Styling ---
# This makes the final price prediction look like a stylish card
st.markdown("""
    <style>
    .prediction-card {
        background: linear-gradient(135deg, #00C9FF 0%, #92FE9D 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .price-text {
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. App Header ---
st.title("🚗 Revving Up Insights: Used Car Price Predictor")
st.markdown("Enter the specifications of the vehicle below, and our machine learning model will estimate its fair market value.")
st.divider()

# --- 4. Load the Model ---
# Example: We use a placeholder here. You will replace 'model.pkl' with your actual saved model file.
@st.cache_resource
def load_model():
    try:
        # We updated the filename here to match yours exactly!
        return joblib.load('best_model.joblib')
    except FileNotFoundError:
        return None

model = load_model()

# --- 5. User Input Section (Layout) ---
# We use columns to make the interface look balanced and professional, rather than a long single list.
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vehicle Details")
    # Example: If a user selects 'Honda', the variable 'brand' stores this exact string.
    brand = st.selectbox("Car Brand", ["Maruti", "Hyundai", "Honda", "Audi", "BMW", "Mercedes"])
    
    # Example: A slider limits extreme inputs, preventing users from entering impossible values like 5,000,000 km.
    km_driven = st.slider("Kilometers Driven", min_value=0, max_value=300000, value=50000, step=1000)

with col2:
    st.subheader("Engine & Ownership")
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
    owner = st.selectbox("Ownership History", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"])

st.divider()

# --- 6. Prediction Logic & Display ---
if st.button("Predict Selling Price", type="primary"):
    if model is None:
        st.error("Model file ('best_model.joblib') not found. Ensure it is in the exact same folder as app.py!")
    else:
        # STEP 1: Create translation dictionaries matching your notebook EXACTLY
        # IMPORTANT: Change these numbers to match whatever your model was trained on!
        brand_mapping = {"Maruti": 1, "Hyundai": 2, "Honda": 3, "Audi": 4, "BMW": 5, "Mercedes": 6}
        fuel_mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3}
        owner_mapping = {"First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth & Above Owner": 4}
        
        # STEP 2: Apply the translation to the user's input before giving it to the model
        input_data = pd.DataFrame({
            'brand': [brand_mapping[brand]],
            'km_driven': [km_driven], # Already a number, no mapping needed
            'fuel': [fuel_mapping[fuel]],
            'owner': [owner_mapping[owner]]
        })
        
        # STEP 3: Make the prediction
        prediction = model.predict(input_data)[0]
        
        # STEP 4: Display the result
        formatted_price = f"₹{int(prediction):,}"
        
        st.markdown(f"""
            <div class="prediction-card">
                <h2>Estimated Market Value</h2>
                <p class="price-text">{formatted_price}</p>
                <p>Based on current market trends</p>
            </div>
        """, unsafe_allow_html=True)