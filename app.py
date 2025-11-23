# from flask import Flask, render_template, request, jsonify
# import pickle
# import numpy as np

# # Load the trained model and scaler
# with open('rf_model.pkl', 'rb') as model_file:
#     rf_model = pickle.load(model_file)

# with open('scaler.pkl', 'rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# @app.route('/predict', methods=['POST'])

# def predict():
#     data = request.get_json()
#     input_data = np.array(data['data'], dtype=float)   # Convert to float

#     scaled_data = scaler.transform(input_data)
#     prediction = rf_model.predict(scaled_data)

#     return jsonify({'prediction': int(prediction[0])})

# # def predict():
# #     data = request.get_json()
# #     input_data = np.array(data['data'])

# #     # Apply the same scaling as the training phase
# #     scaled_data = scaler.transform(input_data)

# #     # Get prediction from the model
# #     prediction = rf_model.predict(scaled_data)

# #     # Return the prediction result
# #     return jsonify({'prediction': int(prediction[0])})

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import pickle
# import numpy as np

# # Load the trained model and scaler
# with open('rf_model.pkl', 'rb') as model_file:
#     rf_model = pickle.load(model_file)

# with open('scaler.pkl', 'rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     input_data = np.array(data['data'], dtype=float)

#     scaled_data = scaler.transform(input_data)
#     prediction = rf_model.predict(scaled_data)

#     return jsonify({'prediction': int(prediction[0])})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

# Force Flask to use templates folder (Fix for OneDrive issues)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

# Load model and scaler correctly
with open(os.path.join(BASE_DIR, 'rf_model.pkl'), 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert input to numpy array
    input_data = np.array(data['data'], dtype=float)

    # FIX: reshape data for scaler + model
    input_data = input_data.reshape(1, -1)

    # Scale input
    scaled = scaler.transform(input_data)

    # Predict
    prediction = rf_model.predict(scaled)

    return jsonify({'prediction': int(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)
