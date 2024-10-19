import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    # Split features and target
    X = df[['Vibration_X', 'Vibration_Y', 'Vibration_Z', 'Temperature', 'RPM', 'Operating_Time']]
    y = df['Fault_Class']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, 'models/machinery_failure_model.pkl')

    return model
