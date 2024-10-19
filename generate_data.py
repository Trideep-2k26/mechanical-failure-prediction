import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 1000  # Increase the number of samples

data = {
    'Vibration_X': np.random.normal(loc=0.0, scale=1.0, size=n_samples),
    'Vibration_Y': np.random.normal(loc=0.0, scale=1.0, size=n_samples),
    'Vibration_Z': np.random.normal(loc=0.0, scale=1.0, size=n_samples),
    'Temperature': np.random.uniform(low=50, high=120, size=n_samples),
    'RPM': np.random.randint(low=1000, high=3000, size=n_samples),
    'Operating_Time': np.random.randint(low=1, high=1000, size=n_samples),
    'Fault_Class': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/vibration_data.csv', index=False)

print("Synthetic dataset generated with 1000 samples and saved as 'data/vibration_data.csv'.")
