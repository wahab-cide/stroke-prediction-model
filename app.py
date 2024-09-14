from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

# load the trained model
model_file_path = './model/stroke_prediction_model.pkl'
with open(model_file_path, 'rb') as f:
    model = pickle.load(f)



@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.get_json()

    # Extract features from the JSON data (must match model training)
    features = np.array([[
        data['gender'],
        data['age'],
        data['hypertension'],
        data['heart_disease'],
        data['ever_married'],
        data['Residence_type'],
        data['avg_glucose_level'],
        data['bmi'],
        data['work_type_Never_worked'],
        data['work_type_Private'],
        data['work_type_Self-employed'],
        data['work_type_children'],
        data['smoking_status_formerly smoked'],
        data['smoking_status_never smoked'],
        data['smoking_status_smokes']
]])


    # Make a prediction using the loaded model
    prediction = model.predict(features)
    
    # Return the prediction as a JSON response
    result = {
        'prediction': int(prediction[0]),  # 0 for no stroke, 1 for stroke
    }
    
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
