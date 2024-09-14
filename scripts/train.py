import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from preprocess import load_and_preprocess_data  # Import the preprocessing function
import os


file_path = '/Users/williams/Downloads/stroke-prediction/healthcare-dataset-stroke-data.csv'
X, y = load_and_preprocess_data(file_path)

# split the dataset into training and testing sets (80% train set)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.columns)


# initialize the Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# define the hyperparameter grid for GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

# apply GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, 
                           cv=3, n_jobs=-1, verbose=2, scoring='accuracy')

# train the model using Grid Search
grid_search.fit(X_train, y_train)

# get the best model from the grid search
best_rf_model = grid_search.best_estimator_

# evaluate the model on the test set
y_pred = best_rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_rep)

# save the trained model to a file


model_file_path = './model/stroke_prediction_model.pkl'
model_dir = './model'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

with open(model_file_path, 'wb') as f:
    pickle.dump(best_rf_model, f)

print(f"Trained model saved to {model_file_path}")
