# Import required libraries
import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of rows to generate
num_rows = 10000

# Generate dataset columns
data = {
    "Lead ID": [f"LD{str(i).zfill(4)}" for i in range(1, num_rows + 1)],  # Unique IDs: LD0001, LD0002, ...
    "Location": [fake.city() for _ in range(num_rows)],  # Random cities
    "College": [fake.company() + " University" for _ in range(num_rows)],  # Random fake university names
    "Year of Study": np.random.choice(["1st", "2nd", "3rd", "4th"], size=num_rows),  # Random study years
    "Program Interest": np.random.choice(
        ["Data Science", "Robotics", "AI", "Electric Vehicle"], size=num_rows
    ),  # Program interests
    "Lead Source": np.random.choice(
        ["Instagram", "LinkedIn", "College Collaboration", "Google Form", "Mass Mailing", "WhatsApp"], 
        size=num_rows
    ),  # Sources
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
output_file = "hypothetical_dataset.csv"
df.to_csv(output_file, index=False)

print(f"Dataset with {num_rows} rows has been generated and saved as '{output_file}'.")
