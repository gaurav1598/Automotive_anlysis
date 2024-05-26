import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

fake = Faker()

# Define the file paths for each reference CSV
customer_file_path = '/home/gauravsingh/Desktop/datafiles/generated_customers_data_updated1.csv'
dealership_file_path = '/home/gauravsingh/Desktop/datafiles/dim_dealership_data_new_final.csv'
model_file_path = '/home/gauravsingh/Desktop/datafiles/vehicle_data_new.csv'
manufacturer_file_path = '/home/gauravsingh/Desktop/datafiles/indian_car_manufacturers.csv'

# Load reference data from separate CSV files
def load_ids_from_csv(file_path, column_name):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    df = pd.read_csv(file_path)
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in {file_path}")
    return df[column_name].unique()

customer_ids = load_ids_from_csv(customer_file_path, 'customer_id')
dealership_ids = load_ids_from_csv(dealership_file_path, 'dealership_id')
model_ids = load_ids_from_csv(model_file_path, 'model_id')
manufacturer_ids = load_ids_from_csv(manufacturer_file_path, 'manufacturer_id')

# Initialize model prices
model_prices = {model_id: np.random.uniform(600000, 2000000) for model_id in model_ids}

# Define additional options
insurance_options = ['Full Coverage', 'Liability']
warranty_options = ['Extended', 'Standard']

# Define years with a specific distribution
years = [2018, 2019, 2020, 2021]
probabilities = [0.24, 0.26, 0.10, 0.40]  # Custom probabilities for each year

# Generate data
data = []
for i in range(10000):
    order_id = f'O{i+1:04d}'
    customer_id = np.random.choice(customer_ids)
    dealership_id = np.random.choice(dealership_ids)
    model_id = np.random.choice(model_ids)
    manufacturer_id = np.random.choice(manufacturer_ids)
    payments_id = f'PAY{i+1:04d}'
    
    selected_year = np.random.choice(years, p=probabilities)
    start_date = datetime(selected_year, 1, 1).date()  # first day of the year
    end_date = datetime(selected_year, 12, 31).date()  # last day of the year
    order_date = fake.date_between(start_date=start_date, end_date=end_date)
    
    ex_showroom_price = model_prices[model_id]
    onroad_price = ex_showroom_price * 1.20
    quantity = np.random.choice([1, 2, 3])
    discount = round(np.random.uniform(200, 1000), 2) * quantity
    insurance_option = np.random.choice(insurance_options)
    warranty_option = np.random.choice(warranty_options)

    data.append({
        'order_id': order_id,
        'manufacturer_id': manufacturer_id,
        'customer_id': customer_id,
        'payments_id': payments_id,
        'model_id': model_id,
        'dealership_id': dealership_id,
        'order_date': order_date.strftime('%Y-%m-%d'),
        'onroad_price': onroad_price,
        'ex_showroom_price': ex_showroom_price,
        'quantity': quantity,
        'discount': discount,
        'insurance_option': insurance_option,
        'warranty_option': warranty_option
    })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('generated_transactions_data_updated.csv', index=False)

print("Data generation complete with 10,000 rows. Consistent pricing applied for each model.")
