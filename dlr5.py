import csv
import random
from faker import Faker

fake = Faker()

# Indian states list
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", 
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", 
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Set to track unique dealership IDs
used_dealership_ids = set()

# Function to generate a unique dealership ID
def generate_dealership_id():
    while True:
        new_id = "D344" + str(random.randint(100, 1100))
        if new_id not in used_dealership_ids:
            used_dealership_ids.add(new_id)
            return new_id

# Function to generate a random VIN (Vehicle Identification Number)
def generate_vin():
    return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=17))

# Function to generate a random Indian state
def generate_indian_state():
    return random.choice(indian_states)

# Function to generate a random Indian-like dealership name
def generate_indian_dealership_name():
    return fake.last_name() + " " + random.choice(['Motors', 'Automobiles', 'Cars', 'Vehicles', 'Auto'])  # Adding a random suffix

# Read vehicle.csv and extract the values you want to reference
vehicle_values = []
with open('vehicle_data_new.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming 'manufacturer_id' and 'model_id' are the columns you want to reference
        vehicle_values.append((row['manufacturer_id'], row['model_id']))

# Generate sample data
data = []
for i in range(1000):
    vehicle = random.choice(vehicle_values)
    row = [
        generate_dealership_id(),  # Ensuring unique dealership_id
        vehicle[0],  # Using manufacturer_id from vehicle.csv
        "S" + str(random.randint(1, 10)).zfill(3),
        generate_indian_dealership_name(),  # Generating Indian-like dealership name
        "B" + str(i+1).zfill(3),
        "SP" + str(i+1).zfill(3),
        fake.name(),
        generate_indian_state(),  # Generating Indian state for location
        fake.name(),
        "Y" if random.random() > 0.5 else "N",  # Randomly select 'Y' or 'N' for facility availability
        vehicle[1],  # Using model_id from vehicle.csv
        random.randint(1990, 2022),
        generate_vin()  # Generating a random VIN
    ]
    data.append(row)

# Write data to CSV file
with open('dim_dealership_data_new_final.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['dealership_id', 'manufacturer_id', 'service_id', 'dealership_name', 'booking_id', 'sales_person_id', 'sales_person_name', 'location', 'owner_name', 'facilities', 'model_id', 'year_established', 'VIN'])
    writer.writerows(data)

print("CSV file generated successfully with unique dealership IDs!")
