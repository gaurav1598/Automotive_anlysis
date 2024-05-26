import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Load data from CSVs
dealership_model_df = pd.read_csv('/home/gauravsingh/Desktop/datafiles/dim_dealership_data_new_final.csv')

# Constants
NUM_ROWS = 4000
CATEGORIES = ['SUV', 'Sedan', 'Coupe', 'Convertible']
CATEGORY_PROBABILITIES = [0.4, 0.3, 0.2, 0.1]  # Adjusted probabilities
STATUSES = ['pending', 'canceled']  # Only "pending" and "canceled"

# Generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

start_date = datetime(2018, 1, 1)
end_date = datetime(2022, 12, 31)

# Initialize empty lists for each column
booking_id = []
dealership_id = []
customer_id = []
model_id = []
booking_status = []
description = []
booking_date = []
last_updated_date = []
active_or_inactive_flag = []
category = []

# Generate data
for i in range(NUM_ROWS):
    booking_id.append(f'B{str(i+1).zfill(5)}')
    
    # Randomly select dealership_model row
    d_m_row = dealership_model_df.sample(n=1).iloc[0]
    dealership_id.append(d_m_row['dealership_id'])
    model_id.append(d_m_row['model_id'])
    
    # Generate customer_id in the format CU001, CU002, etc.
    customer_id.append(f'CU{str(i+1).zfill(3)}')
    
    # Randomly assign booking_status to either 'pending' or 'canceled'
    status = random.choice(STATUSES)
    booking_status.append(status)
    
    # Assign category based on probabilities
    cat = np.random.choice(CATEGORIES, p=CATEGORY_PROBABILITIES)
    category.append(cat)
    
    # Create description based on category and booking status
    if status == 'pending':
        description.append(f'Awaiting payment for the {cat.lower()}')
    else:  # status == 'canceled'
        description.append(f'Booking canceled for the {cat.lower()}')
    
    b_date = random_date(start_date, end_date)
    booking_date.append(b_date.strftime('%Y-%m-%d'))
    last_updated_date.append((b_date + timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'))
    
    active_or_inactive_flag.append(random.choice(['active', 'inactive']))

# Create DataFrame
data = {
    'booking_id': booking_id,
    'dealership_id': dealership_id,
    'customer_id': customer_id,
    'model_id': model_id,
    'booking_status': booking_status,
    'description': description,
    'booking_date': booking_date,
    'last_updated_date': last_updated_date,
    'active_or_inactive_flag': active_or_inactive_flag,
    'category': category
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('dim_booking_status3.csv', index=False)
