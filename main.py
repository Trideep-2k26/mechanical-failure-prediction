import pandas as pd
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model
import joblib

def main():
    # Preprocess data
    raw_data_path = 'data/vibration_data.csv'
    df = preprocess_data(raw_data_path)

    # Train model
    model = train_model(df)

    # Prepare data for evaluation
    X = df[['Vibration_X', 'Vibration_Y', 'Vibration_Z', 'Temperature', 'RPM', 'Operating_Time']]
    y = df['Fault_Class']

    # Evaluate model
    evaluate_model(model, X, y)

    # Save the trained model
    joblib.dump(model, 'models/machinery_failure_model.pkl')
    print("Model trained and saved to 'models/machinery_failure_model.pkl'.")

if __name__ == "__main__":
    main()
