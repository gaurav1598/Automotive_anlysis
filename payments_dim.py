import pandas as pd
import numpy as np
from faker import Faker
import csv

fake = Faker('en_IN')  # Use the Indian locale for Faker

# Define the file paths for reference CSVs
payments_file_path = '/home/gauravsingh/Desktop/datafiles/generated_transactions_data_updated.csv'
customer_file_path = '/home/gauravsingh/Desktop/datafiles/generated_transactions_data_updated.csv'

# Function to load IDs from CSV
def load_ids_from_csv(file_path, column_name):
    df = pd.read_csv(file_path)
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in {file_path}")
    return df[column_name].unique()

# Load payment and customer IDs
payments_ids = load_ids_from_csv(payments_file_path, 'payments_id')
customer_ids = load_ids_from_csv(customer_file_path, 'customer_id')

# Shuffle IDs to prevent immediate repetition
np.random.shuffle(payments_ids)
np.random.shuffle(customer_ids)

# Initialize indices for ID selection
payments_idx = 0
customer_idx = 0

# Define possible values for payment methods with probabilities
payment_methods = ['UPI', 'Net Banking', 'Credit Card', 'Debit Card', 'Mobile Payment', 'EMI', 'Cash']
payment_method_probs = [0.15, 0.15, 0.20, 0.15, 0.10, 0.20, 0.05]

# Define banks and their probabilities
banks = ['HDFC Bank', 'State Bank of India', 'ICICI Bank', 'Axis Bank', 'Kotak Mahindra Bank', 'Punjab National Bank', 'Yes Bank']
  # Adjust these probabilities as needed

# Define probabilities for financing option
financing_option_probs = [0.80, 0.20]  # 70% Yes, 30% No

# Generate data
data = []
for i in range(10000):
    payments_id = payments_ids[payments_idx]
    customer_id = customer_ids[customer_idx]

    # Move to the next ID, cycling back to start if at the end
    payments_idx = (payments_idx + 1) % len(payments_ids)
    customer_idx = (customer_idx + 1) % len(customer_ids)

    payment_method = np.random.choice(payment_methods, p=payment_method_probs)
    financing_option = np.random.choice(['Y', 'N'], p=financing_option_probs)
    financing_bank = 'N/A' if financing_option == 'N' else np.random.choice(banks)
    additional_purchase = np.random.choice(
        ['Extended Warranty', 'Insurance', 'Service Package', 'Alloy Wheels Upgrade', 'Teflon Coating', 'Full Car Accessories', 'Interior Detailing', 'Premium Sound System'],
        p=[0.15, 0.15, 0.10, 0.10, 0.05, 0.10, 0.10, 0.25])  # Adjusted to sum to 1.0

    offer_type = np.random.choice(
        ['Cashback', 'Festival Offer', 'Special Rate', 'Discount', 'New Year Offer', 'None'],
        p=[0.20, 0.20, 0.15, 0.15, 0.15, 0.15]  # Adjusted probabilities
    )
    offer_value = str(fake.random_int(min=10000, max=50000)) if offer_type != 'None' else 'N/A'

    data.append({
        'payments_id': payments_id,
        'customer_id': customer_id,
        'payment_method': payment_method,
        'financing_option': financing_option,
        'financing_bank': financing_bank,
        'additional_purchase': additional_purchase,
        'offer_type': offer_type,
        'offer_value': offer_value
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV, ensuring proper quoting
df.to_csv('generated_paymments_data_updaated.csv', index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

print("Data generation complete and saved to 'generated_payments_data_updaated.csv'.")


large_dataset_20200511/auto_data/generated_paymments_data_updaated.csv