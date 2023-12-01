import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Define the number of samples
n_samples = 300

# Generate engine size data (ranging from 1.0 liters to 5.0 liters)
engine_size = np.random.uniform(1.0, 5.0, n_samples)

# Generate fuel efficiency data
# Assuming a linear relationship with some noise
base_efficiency = 40  # Base MPG for a standard engine size
efficiency = base_efficiency - engine_size * 5 + np.random.normal(0, 2, n_samples)

# Create a DataFrame
fuel_efficiency_data = pd.DataFrame({
    'EngineSize': engine_size,
    'FuelEfficiency': efficiency
})

# Round off the values
fuel_efficiency_data = fuel_efficiency_data.round(2)

# Save to a CSV file
fuel_efficiency_data.to_csv('fuel_efficiency_dataset.csv', index=False)

# Display the first few rows of the dataframe
fuel_efficiency_data.head()
