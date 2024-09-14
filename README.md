# **Stroke Prediction Model API**

This project is a machine learning-powered API that predicts the likelihood of a stroke based on a patient's medical data. The model was built using the RandomForestClassifier from Scikit-learn, and the API was developed with Flask and deployed on Heroku.

## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Model](#model)
- [Contributing](#contributing)

---

## **Project Overview**

The **Stroke Prediction Model API** uses a machine learning model to predict the probability of a stroke in a patient based on key medical data such as age, hypertension, heart disease, BMI, and more. The model was trained on the [Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset).

This API allows users to submit patient data via a POST request and returns a prediction indicating whether the patient is at risk for a stroke.

---

## **Features**
- **Machine Learning Model**: Random Forest classifier built using Scikit-learn.
- **REST API**: Developed with Flask to expose the prediction model as an API.
- **Deployed on Heroku**: Accessible via the web.
- **Real-Time Predictions**: Provides stroke risk predictions based on medical data input.

---

## **Technologies Used**
- **Python**: Programming language used for the model and API.
- **Flask**: Micro web framework for developing the API.
- **Scikit-learn**: Used for building the Random Forest classifier.
- **NumPy**: For numerical operations.
- **Gunicorn**: WSGI HTTP server for running the app in production on Heroku.
- **Heroku**: Cloud platform for deployment.

---

## **Installation**

To run the project locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/stroke-prediction-model.git
cd stroke-prediction-model
```

### 2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application:
```bash
python app.py
```

The app will now be running locally at `http://127.0.0.1:5000`.

---

## **Usage**

### API Endpoints

The app provides a single POST endpoint to make predictions:

#### **`POST /predict`**
This endpoint expects a JSON body with the patient's medical data and returns the stroke risk prediction.

### Example Request:
```json
{
    "gender": 1,
    "age": 67,
    "hypertension": 0,
    "heart_disease": 1,
    "ever_married": 1,
    "Residence_type": 0,
    "avg_glucose_level": 228.69,
    "bmi": 36.6,
    "work_type_Never_worked": 0,
    "work_type_Private": 1,
    "work_type_Self-employed": 0,
    "work_type_children": 0,
    "smoking_status_formerly smoked": 1,
    "smoking_status_never smoked": 0,
    "smoking_status_smokes": 0
}
```

### Example Response:
```json
{
    "prediction": 0
}
```
Where `0` indicates low stroke risk and `1` indicates high stroke risk.

---

## **Testing**

You can test the API using:
- **Postman**: To send POST requests with the appropriate JSON body.
- **cURL**: 
  ```bash
  curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": 1,
    "age": 67,
    "hypertension": 0,
    "heart_disease": 1,
    "ever_married": 1,
    "Residence_type": 0,
    "avg_glucose_level": 228.69,
    "bmi": 36.6,
    "work_type_Never_worked": 0,
    "work_type_Private": 1,
    "work_type_Self-employed": 0,
    "work_type_children": 0,
    "smoking_status_formerly smoked": 1,
    "smoking_status_never smoked": 0,
    "smoking_status_smokes": 0
  }'
  ```

---

## **Deployment**

The app has been deployed on Heroku. To deploy the app yourself, follow these steps:

### 1. Create a Heroku account:
Sign up at [Heroku](https://www.heroku.com/).

### 2. Install the Heroku CLI:
```bash
brew tap heroku/brew && brew install heroku
```

### 3. Log in to Heroku:
```bash
heroku login
```

### 4. Create and Deploy to Heroku:
```bash
heroku create your-app-name
git push heroku main
heroku ps:scale web=1
heroku open
```

---

## **Model**

The model used in this project is a **Random Forest Classifier** built using the Scikit-learn library. It was trained on the [Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) and is designed to predict stroke risk based on several features, including age, BMI, smoking status, and more.

### Training Improvements:
- Improved prediction accuracy through feature engineering and hyperparameter tuning.
- Addressed class imbalance by weighing the stroke class during training.

---

## **Contributing**

If you'd like to contribute to this project, feel free to:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---