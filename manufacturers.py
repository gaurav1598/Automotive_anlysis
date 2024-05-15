import csv

data = [
    {"model_id": "V001", "model_name": "Tata Tiago", "manufacturer_id": "M001", "year_release": 2016, "market_segment": "Hatchback", "variant_name": "XE", "engine_type": "Petrol", "transmission_type": "Manual", "features": "Power steering, AC, ABS", "fuel_efficiency": "23 kmpl", "safety_ratings": "4-star NCAP", "trim_levels": "XE, XT, XZ", "target_audience": "Budget-conscious buyers", "warranty_coverage": "2 years/75,000 km"},
    {"model_id": "V002", "model_name": "Maruti Suzuki Swift", "manufacturer_id": "M002", "year_release": 2005, "market_segment": "Hatchback", "variant_name": "LXi", "engine_type": "Petrol", "transmission_type": "Manual", "features": "Power steering, AC, ABS", "fuel_efficiency": "21.21 kmpl", "safety_ratings": "3-star NCAP", "trim_levels": "LXi, VXi, ZXi", "target_audience": "Urban commuters", "warranty_coverage": "2 years/40,000 km"},
    {"model_id": "V003", "model_name": "Mahindra XUV500", "manufacturer_id": "M003", "year_release": 2011, "market_segment": "SUV", "variant_name": "W5", "engine_type": "Diesel", "transmission_type": "Automatic", "features": "Touchscreen infotainment, Sunroof, Leather seats", "fuel_efficiency": "15.1 kmpl", "safety_ratings": "5-star NCAP", "trim_levels": "W5, W7, W9", "target_audience": "Family-oriented buyers", "warranty_coverage": "3 years/100,000 km"},
    {"model_id": "V004", "model_name": "Hyundai Creta", "manufacturer_id": "M004", "year_release": 2015, "market_segment": "SUV", "variant_name": "E", "engine_type": "Petrol", "transmission_type": "Manual", "features": "Touchscreen infotainment, Rear parking sensors, Cruise control", "fuel_efficiency": "16.8 kmpl", "safety_ratings": "4-star NCAP", "trim_levels": "E, EX, S", "target_audience": "Urban adventurers", "warranty_coverage": "3 years/unlimited km"},
    {"model_id": "V005", "model_name": "Honda City", "manufacturer_id": "M005", "year_release": 1998, "market_segment": "Sedan", "variant_name": "SV", "engine_type": "Petrol", "transmission_type": "CVT", "features": "Sunroof, LED headlamps, Climate control", "fuel_efficiency": "17.8 kmpl", "safety_ratings": "4-star NCAP", "trim_levels": "SV, V, VX", "target_audience": "City drivers", "warranty_coverage": "3 years/100,000 km"}
]

# Define CSV file path
csv_file = "vehicle_data.csv"

# Define CSV fieldnames
fieldnames = ["model_id", "model_name", "manufacturer_id", "year_release", "market_segment", "variant_name", "engine_type", "transmission_type", "features", "fuel_efficiency", "safety_ratings", "trim_levels", "target_audience", "warranty_coverage"]

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write data
    for row in data:
        writer.writerow(row)

print("CSV file generated successfully!")
