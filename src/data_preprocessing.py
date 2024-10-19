import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    # Load the raw dataset
    df = pd.read_csv(file_path)

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Select features for scaling
    features_to_scale = ['Vibration_X', 'Vibration_Y', 'Vibration_Z', 'Temperature', 'RPM', 'Operating_Time']

    # Fit and transform the features
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

    return df
