import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


file_path = '/Users/williams/Downloads/stroke-prediction/healthcare-dataset-stroke-data.csv'




def load_and_preprocess_data(file_path):
    """
    Load and preprocess the dataset.
    
    Parameters:
    - file_path: Path to the CSV file.
    
    Returns:
    - X: Preprocessed feature set
    - y: Target variable

    """
  
    stroke_data = pd.read_csv(file_path)

    # handle missing values (Fill missing BMI values with the median)
    stroke_data['bmi'].fillna(stroke_data['bmi'].median(), inplace=True)

    # encode categorical variables
    le = LabelEncoder()

    # encoding binary categorical columns
    stroke_data['gender'] = le.fit_transform(stroke_data['gender'])
    stroke_data['ever_married'] = le.fit_transform(stroke_data['ever_married'])
    stroke_data['Residence_type'] = le.fit_transform(stroke_data['Residence_type'])

    # One-hot encode the 'work_type' and 'smoking_status' columns
    stroke_data = pd.get_dummies(stroke_data, columns=['work_type', 'smoking_status'], drop_first=True)

    # normalize numerical columns
    scaler = StandardScaler()
    stroke_data[['age', 'avg_glucose_level', 'bmi']] = scaler.fit_transform(stroke_data[['age', 'avg_glucose_level', 'bmi']])

    # define features (X) and target (y)
    X = stroke_data.drop(['id', 'stroke'], axis=1)
    y = stroke_data['stroke']

    return X, y


#if __name__ == "__main__":
#    X, y = load_and_preprocess_data(file_path)
#    file_path = '/Users/williams/Downloads/stroke-prediction'
#    print("Data Preprocessing Completed.")
