📘 PCOS Prediction Web Application
==================================

### *Machine Learning + Flask Web App*

This project is a complete end-to-end **PCOS Prediction System** built using:

-   Python

-   Scikit-Learn

-   Flask

-   Random Forest Classifier

-   StandardScaler

-   HTML/JS (Front-end)

It takes health & lifestyle inputs from the user and predicts whether the person is likely to have **PCOS (Polycystic Ovary Syndrome)**.

* * * * *

🧠 Project Structure
====================

`project/
│── app.py               # Flask backend for prediction (API)
│── main.py              # ML model training script
│── templates/
│     └── index.html     # Front-end UI (Flask template)
│── CLEAN- PCOS SURVEY SPREADSHEET.csv  # Training dataset
│── rf_model.pkl         # Trained RandomForest model
│── scaler.pkl           # StandardScaler used for preprocessing
│── README.md`

* * * * *

🔍 1. Overview
==============

This project predicts PCOS using a trained machine learning model.\
The workflow includes:

1.  **Dataset Cleaning & Preprocessing**

2.  **Training ML Model**

3.  **Saving Model + Scaler**

4.  **Developing Flask Backend**

5.  **Building a Front-End UI**

6.  **Deploying as a Web Application**

* * * * *

📊 2. Dataset Description
=========================

The project uses a cleaned PCOS survey dataset:

**File:** `CLEAN- PCOS SURVEY SPREADSHEET.csv`

main

### Columns Used

-   Age

-   Weight

-   Height

-   Blood_Group

-   Cycle_Regularity

-   Weight_Gain

-   Excess_Hair

-   Skin_Darkening

-   Hair_Loss

-   Acne

-   Fast_Food

-   Exercise

-   **PCOS_Diagnosis** (Target variable)

-   Mood_Swings

-   Periods_Regular

-   Period_Duration

* * * * *

🤖 3. Model Training Process
============================

Training is done in **main.py**

main

.

Steps:
------

### **✔ Step 1: Load Dataset**

`data = pd.read_csv('CLEAN- PCOS SURVEY SPREADSHEET.csv')`

### ✔ Step 2: Rename Columns

Ensures all column names are consistent.

### ✔ Step 3: Split Features (X) & Target (Y)

`X = data.drop("PCOS_Diagnosis", axis=1)
y = data["PCOS_Diagnosis"]`

### ✔ Step 4: Apply StandardScaler

Scaling ensures equal weightage to all features.

### ✔ Step 5: Train-Test Split

80% training, 20% testing.

### ✔ Step 6: Train RandomForestClassifier

`rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)`

### ✔ Step 7: Save Model & Scaler

Saves files:

-   **rf_model.pkl**

-   **scaler.pkl**

These are later used by Flask to make predictions.

* * * * *

🚀 4. Flask Backend (Prediction API)
====================================

Located in **app.py**

app

.

### 🔧 Key Functionalities:

-   Loads `rf_model.pkl` and `scaler.pkl`

-   Provides `/predict` API route

-   Accepts JSON input

-   Scales input

-   Returns prediction (0 = No PCOS, 1 = PCOS)

### 🔥 Prediction Flow

1.  Front-end sends array of inputs:

`{ "data": [value1, value2, ...] }`

1.  Converts to numpy → reshapes → scales

2.  Passes into ML model

3.  Returns predicted value

* * * * *

🖥 5. Front-End UI (index.html)
===============================

-   Simple and clean web form

-   Collects all patient inputs

-   Sends request via AJAX to `/predict`

-   Displays prediction on screen

* * * * *

▶️ 6. How to Run This Project Locally
=====================================

### **Step 1 --- Install Required Libraries**

`pip install flask scikit-learn pandas numpy`

### **Step 2 --- Train the Model (if needed)**

Run:

`python main.py`

This creates:

-   `rf_model.pkl`

-   `scaler.pkl`

### **Step 3 --- Start Flask App**

`python app.py`

### **Step 4 --- Open in Browser**

`http://127.0.0.1:5000/`

* * * * *

🌐 7. API Endpoint Details
==========================

### **POST → /predict**

#### Example Request

`{
  "data": [21, 60, 162, 2, 1, 0, 1, 0, 1, 0, 1, 0, 2, 1, 5]
}`

#### Example Response

`{
  "prediction": 1
}`

* * * * *

🧪 8. Model Details
===================

| Component | Description |
| --- | --- |
| Algorithm | Random Forest Classifier |
| Input Shape | 15 features |
| Output | Binary (0 = No PCOS, 1 = PCOS) |
| Scaler | StandardScaler |
| Dataset Split | 80/20 |

* * * * *

🛠️ 9. Common Issues & Fixes
============================

### ✔ Template Not Loading

Fixed using absolute path in app.py:

`app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))`

### ✔ Data Reshape Error

Solved by:

`input_data = input_data.reshape(1, -1)`

### ✔ OneDrive Path Issues

Handled via `BASE_DIR = os.path.dirname(os.path.abspath(__file__))`.

* * * * *

🧾 10. Future Improvements
==========================

-   Add more features for better accuracy

-   Improve front-end UI with modern UI frameworks

-   Add charts and visual analytics

-   Deploy on cloud (Render / AWS / GCP / Azure)

-   Add user authentication

* * * * *

🏁 11. Conclusion
=================

This project successfully demonstrates a complete **ML + Flask deployment pipeline** for PCOS prediction.\
It includes:

-   Dataset preprocessing

-   Model training

-   Backend API

-   Interactive web UI

It is production-ready and can be extended for clinical/educational use.