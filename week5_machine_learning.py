import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load and prepare data
df = pd.read_csv('Walmart_Cleaned.csv')

# We pick our 'Features' (What causes sales) and our 'Target' (The Sales)
features = ['Holiday_Flag', 'Temperature', 'Fuel_Price', 'Unemployment']
X = df[features]
y = df['Weekly_Sales']

# Initialize and Train the Model
model = LinearRegression()
model.fit(X, y)

# --- THE EXTRAORDINARY INSIGHTS ---
print("📊 --- WEEK 5 CAPSTONE: PREDICTIVE ANALYTICS --- 📊")

# 1. Feature Importance (Which marketing lever is strongest?)
importance = model.coef_
for i, v in enumerate(importance):
    print(f"Impact of {features[i]}: ${v:,.2f} change in sales per unit.")

# 2. The "What-If" Scenario
# Imagine a Holiday week, 70 degrees, $3.50 gas, and 8% unemployment
scenario = np.array([[1, 70, 3.50, 8]])
prediction = model.predict(scenario)

print(f"\n🔮 [PREDICTION ENGINE]")
print(f"Scenario: Holiday Week + 70°F + $3.50 Fuel + 8% Unemployment")
print(f"Projected Weekly Revenue: ${prediction[0]:,.2f}")

# 3. Managerial Strategy
print(f"\n✅ [STRATEGIC RECOMMENDATION]")
if importance[0] > 50000:
    print("Strategy: Holiday marketing is your highest ROI. Pivot all Q4 budget to digital ads.")
if importance[3] < 0:
    print(f"Risk Alert: For every 1% rise in unemployment, you lose ${abs(importance[3]):,.2f} per store.")