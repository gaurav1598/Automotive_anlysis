import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

fake = Faker()

# Load reference data for customer_id and model_id from separate files
def load_reference_data(customer_file, model_file):
    customer_df = pd.read_csv(customer_file)
    model_df = pd.read_csv(model_file)
    return customer_df['customer_id'].unique(), model_df['model_id'].unique()

# Assuming the files are located correctly
customer_ids, model_ids = load_reference_data('/home/gauravsingh/Desktop/datafiles/generated_customers_data_updated1.csv', '/home/gauravsingh/Desktop/datafiles/vehicle_data_new.csv')

# Define service types and corresponding costs
service_types = {
    'Maintenance': [50, 10000],
    'Repair': [100, 3000],
    'Safety Check': [30, 6100]
}

# Define feedback types and ratings
feedback_ratings = ['Excellent', 'Very Good', 'Good', 'Satisfactory', 'Poor', 'Unsatisfactory']
feedback_ratings_prob = [0.10, 0.15, 0.25, 0.20, 0.20, 0.10]  # Example probabilities

# Define feedback resolution and probabilities
feedback_resolutions = ['Resolved', 'Resolution Pending', 'Issue Escalated']
feedback_resolution_probs = [0.70, 0.20, 0.10]  # Example probabilities

# Generate data
data = []
start_date = datetime.strptime("2018-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2021-12-31", "%Y-%m-%d")

for i in range(10000):
    service_id = f'S{i+1:04d}'
    service_name = fake.random.choice(['Oil Change', 'Tire Rotation', 'Engine Diagnostics', 'Brake Inspection', 'Battery Replacement'])
    service_type = fake.random.choice(list(service_types.keys()))
    service_date = fake.date_between(start_date=start_date, end_date=end_date)
    model_id = np.random.choice(model_ids)
    customer_id = np.random.choice(customer_ids)
    feedback_rating = np.random.choice(feedback_ratings, p=feedback_ratings_prob)
    selected_feedback_resolution = np.random.choice(feedback_resolutions, p=feedback_resolution_probs)  # Use a different variable
    service_cost = np.random.randint(service_types[service_type][0], service_types[service_type][1] + 1)
    
    data.append({
        'service_id': service_id,
        'service_name': service_name,
        'service_type': service_type,
        'service_date': service_date.strftime('%Y-%m-%d'),
        'model_id': model_id,
        'customer_id': customer_id,
        'feedback_rating': feedback_rating,
        'feedback_resolution': selected_feedback_resolution,  # Corrected variable name
        'service_cost': service_cost
    })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('generated_service_and_feedback_data_neww.csv', index=False)

print("Data generation complete with 10,000 rows. Service dates range from 2018 to 2021.")
