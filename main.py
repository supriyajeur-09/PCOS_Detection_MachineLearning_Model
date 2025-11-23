import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Load your dataset
data = pd.read_csv('CLEAN- PCOS SURVEY SPREADSHEET.csv')

# Preprocessing and preparing data
data.columns = [
    "Age", "Weight", "Height", "Blood_Group", "Cycle_Regularity", 
    "Weight_Gain", "Excess_Hair", "Skin_Darkening", "Hair_Loss",
    "Acne", "Fast_Food", "Exercise", "PCOS_Diagnosis", 
    "Mood_Swings", "Periods_Regular", "Period_Duration"
]

# Separate features and target
X = data.drop("PCOS_Diagnosis", axis=1)
y = data["PCOS_Diagnosis"]

# Standardizing features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a RandomForest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Save the model and the scaler as .pkl files
with open('rf_model.pkl', 'wb') as model_file:
    pickle.dump(rf_model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Model and Scaler saved as .pkl files")
