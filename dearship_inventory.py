import pandas as pd
import numpy as np

# Read the reference data from a CSV file
def read_reference_data(filepath):
    reference_data = pd.read_csv(filepath)
    return reference_data['model_id'].unique(), reference_data['dealership_id'].unique()

# Use numpy to generate the sinusoidal quantity pattern
def generate_quantity(num_entries):
    x = np.linspace(0, num_entries / 15, num_entries)
    y = np.sin(x) * 5 + 6
    return np.round(y).astype(int)

# Generate data for the dim_dealership_inventory table using vectorized operations
def generate_inventory_data(num_entries, model_ids, dealership_ids):
    if num_entries > len(dealership_ids):
        raise ValueError("Not enough unique dealership_ids for the number of entries requested.")
    
    np.random.shuffle(dealership_ids)  # Shuffle dealership ids to randomize assignments
    inventory_id = [f"INV{str(i).zfill(3)}" for i in range(1, num_entries + 1)]
    model_id = np.random.choice(model_ids, size=num_entries, replace=True)  # Allow models to repeat
    condition = np.where(np.arange(num_entries) % 2 == 0, 'New', 'Used')
    quantity = generate_quantity(num_entries)
    sales_status = np.tile(['Available', 'Sold', 'In Negotiation'], num_entries // 3 + 1)[:num_entries]

    return pd.DataFrame({
        "inventory_id": inventory_id,
        "dealership_id": dealership_ids[:num_entries],  # Assign each unique dealership to an entry
        "model_id": model_id,
        "condition": condition,
        "quantity": quantity,
        "sales_status": sales_status
    })

# Main function
def main():
    filepath = '/home/gauravsingh/Desktop/pythonfiles/dim_dealership_data_new_final.csv'
    model_ids, dealership_ids = read_reference_data(filepath)
    inventory_data = generate_inventory_data(1000, model_ids, dealership_ids)  # Now requesting 1000 rows
    inventory_data.to_csv('dim_dealership_inventory.csv', index=False)
    print("Data has been successfully written to dim_dealership_inventory.csv")

# Run the script
if __name__ == "__main__":
    main()
