import csv
import random

# Vehicle data template
vehicles = {
    "M001": [  # Tata Motors
        ("Tiago", "Hatchback", "XT", "1.2L Petrol", "Manual", "Airbags, ABS, Touchscreen", "23.84 kmpl", "4-star NCAP", "Base, XT, XZ", "Families", "2 years/75,000 km"),
        ("Nexon", "Compact SUV", "XZ+", "1.5L Diesel", "Automatic", "Sunroof, Touchscreen, ESP", "21.5 kmpl", "5-star NCAP", "XM, XZ+, XZA+", "Young Professionals", "3 years/100,000 km"),
        ("Harrier", "Midsize SUV", "XZ", "2.0L Diesel", "Automatic", "Panoramic Sunroof, JBL Audio", "17 kmpl", "5-star NCAP", "XE, XM, XT, XZ", "Adventure Seekers", "2 years/50,000 km"),
        ("Altroz", "Premium Hatchback", "XZ", "1.5L Diesel", "Manual", "Cruise Control, Harman Audio", "25.11 kmpl", "5-star NCAP", "XE, XM, XT, XZ", "Young Families", "2 years/75,000 km"),
        ("Safari", "SUV", "Adventure Persona", "2.0L Diesel", "Automatic", "4x4, Panoramic Sunroof, ESP", "16.14 kmpl", "4-star NCAP", "XE, XM, XT, XZ", "Large Families", "2 years/50,000 km")
    ],
    "M002": [  # Mahindra & Mahindra
        ("Thar", "Off-road SUV", "LX", "2.0L Petrol", "Automatic", "Convertible Top, Touchscreen", "15.2 kmpl", "4-star NCAP", "AX, LX", "Adventure Enthusiasts", "3 years/100,000 km"),
        ("XUV700", "SUV", "AX7", "2.2L Diesel", "Automatic", "ADAS, Panoramic Sunroof, 7 Seater", "14 kmpl", "5-star NCAP", "MX, AX3, AX5, AX7", "Tech Savvy", "3 years/100,000 km"),
        ("Scorpio", "SUV", "S11", "2.2L Diesel", "Manual", "4x4, Cruise Control, Navigation", "12.4 kmpl", "NA", "S5, S7, S9, S11", "Families", "2 years/75,000 km"),
        ("Bolero", "Utility Vehicle", "Power+", "1.5L Diesel", "Manual", "ABS, Airbags, Bluetooth", "16.5 kmpl", "NA", "B4, B6, B6(O)", "Rural Markets", "1 year/50,000 km"),
        ("Marazzo", "MPV", "M8", "1.5L Diesel", "Manual", "7/8 Seater, Infotainment System", "17.3 kmpl", "4-star NCAP", "M2, M4, M6, M8", "Large Families", "2 years/75,000 km")
    ],
    "M003": [  # Maruti Suzuki
        ("Swift", "Hatchback", "ZXI", "1.2L Petrol", "Manual", "ABS, EBD, Airbags", "22 kmpl", "2-star NCAP", "LXI, VXI, ZXI", "Young Buyers", "2 years/40,000 km"),
        ("Baleno", "Premium Hatchback", "Alpha", "1.2L Petrol", "CVT", "LED Projector Headlamps, SmartPlay Studio", "19.56 kmpl", "3-star NCAP", "Sigma, Delta, Zeta, Alpha", "Families, Young Professionals", "3 years/60,000 km"),
        ("Vitara Brezza", "Compact SUV", "ZDI+", "1.5L Diesel", "Automatic", "Smart Hybrid, Cruise Control", "24.3 kmpl", "4-star NCAP", "LDI, VDI, ZDI, ZDI+", "Small Families", "2 years/50,000 km"),
        ("Ertiga", "MPV", "ZXI+", "1.5L Petrol", "Automatic", "SmartPlay Infotainment, ABS, EBD", "19 kmpl", "NA", "LXI, VXI, ZXI, ZXI+", "Large Families", "3 years/100,000 km"),
        ("Dzire", "Sedan", "ZXI+", "1.2L Petrol", "Automatic", "Auto Gear Shift, SmartPlay Studio", "24 kmpl", "3-star NCAP", "LXI, VXI, ZXI, ZXI+", "Families", "2 years/40,000 km")
    ],
    "M004": [  # Hyundai
        ("i20", "Premium Hatchback", "Asta", "1.2L Petrol", "Manual", "Sunroof, BlueLink, Airbags", "20.35 kmpl", "3-star NCAP", "Magna, Sportz, Asta", "Young Professionals", "3 years/100,000 km"),
        ("Creta", "SUV", "SX", "1.5L Diesel", "Automatic", "Panoramic Sunroof, Voice Commands", "18.5 kmpl", "4-star NCAP", "E, EX, S, SX", "Families", "3 years/unlimited km"),
        ("Venue", "Compact SUV", "SX(O)", "1.0L Turbo Petrol", "DCT", "BlueLink, Sunroof, Six Airbags", "18 kmpl", "4-star NCAP", "E, S, SX, SX(O)", "Urban Buyers", "3 years/100,000 km"),
        ("Verna", "Sedan", "SX(O)", "1.6L Diesel", "Automatic", "Ventilated Seats, Smart Trunk", "21 kmpl", "NA", "S, SX, SX(O)", "Young Executives", "3 years/100,000 km"),
        ("Santro", "Hatchback", "Asta", "1.1L Petrol", "Manual", "Touchscreen, Rear Parking Camera", "20 kmpl", "2-star NCAP", "Era, Magna, Sportz, Asta", "First-Time Buyers", "2 years/40,000 km")
    ],
    "M005": [  # Honda
        ("City", "Sedan", "ZX CVT", "1.5L Petrol", "Automatic", "Sunroof, LaneWatch", "17.8 kmpl", "4-star NCAP", "V, VX, ZX", "Families", "3 years/unlimited km"),
        ("Amaze", "Sedan", "VX CVT", "1.2L Petrol", "Automatic", "Touchscreen Infotainment, Cruise Control", "18.6 kmpl", "NA", "E, S, V, VX", "Small Families", "3 years/100,000 km"),
        ("Jazz", "Hatchback", "ZX CVT", "1.2L Petrol", "CVT", "Magic Seats, Touchscreen Infotainment", "17.1 kmpl", "NA", "V, VX, ZX", "Young Professionals", "2 years/40,000 km")
    ],
    "M006": [  # Toyota
        ("Fortuner", "SUV", "Legender", "2.8L Diesel", "Automatic", "4x4, JBL Sound System", "10.1 kmpl", "NA", "G, GX, VX, ZX", "Adventure Seekers", "3 years/100,000 km"),
        ("Innova Crysta", "MPV", "ZX AT", "2.4L Diesel", "Automatic", "Captain Seats, Touchscreen", "15.1 kmpl", "NA", "G, GX, VX, ZX", "Large Families", "3 years/100,000 km"),
        ("Yaris", "Sedan", "VX CVT", "1.5L Petrol", "CVT", "7 Airbags, Gesture Control", "17.8 kmpl", "NA", "J, G, V, VX", "Small Families", "3 years/100,000 km")
    ],
    "M007": [  # Ford
        ("EcoSport", "Compact SUV", "Titanium+", "1.5L Diesel", "Manual", "Sunroof, SYNC 3", "23 kmpl", "NA", "Ambiente, Trend, Titanium, Titanium+", "Young Families", "3 years/100,000 km"),
        ("Endeavour", "SUV", "Titanium 4x4", "2.0L Diesel", "Automatic", "Panoramic Sunroof, Terrain Management", "12.4 kmpl", "NA", "Titanium, Titanium+", "Adventure Seekers", "3 years/100,000 km"),
        ("Figo", "Hatchback", "Blu", "1.5L Petrol", "Manual", "Touchscreen, 6 Airbags", "18.5 kmpl", "NA", "Ambiente, Trend, Titanium, Blu", "Young Professionals", "2 years/40,000 km")
    ],
    "M008": [  # Kia
        ("Seltos", "Compact SUV", "HTX IVT", "1.5L Petrol", "Automatic", "LED Headlamps, 10.25-inch Touchscreen", "16.8 kmpl", "NA", "HTK, HTX, GTX", "Urban Explorers", "3 years/Unlimited km"),
        ("Sonet", "Subcompact SUV", "HTX+", "1.0L Turbo Petrol", "iMT", "Sunroof, UVO Connectivity", "18.4 kmpl", "NA", "HTE, HTK, HTK+, HTX, GTX+", "City Commuters", "3 years/Unlimited km"),
        ("Carnival", "MPV", "LX", "2.2L Diesel", "Automatic", "Dual Sunroofs, VIP Seats", "13.9 kmpl", "NA", "EX, SX, SX+", "Large Families", "3 years/Unlimited km")
    ],
    "M009": [  # Volkswagen
        ("Polo", "Hatchback", "Highline Plus AT", "1.0L TSI Petrol", "Automatic", "17-inch Alloy Wheels, Rear Parking Sensors", "16.47 kmpl", "NA", "Trendline, Comfortline, Highline, Highline Plus", "Driving Enthusiasts", "4 years/1,00,000 km"),
        ("Vento", "Sedan", "Highline AT", "1.0L TSI Petrol", "Automatic", "LED Headlamps, 8-inch Touchscreen", "17.69 kmpl", "NA", "Trendline, Comfortline, Highline, Highline Plus", "Urban Commuters", "4 years/1,00,000 km"),
        ("Tiguan Allspace", "SUV", "Comfortline", "2.0L TSI Petrol", "Automatic", "Panoramic Sunroof, Virtual Cockpit", "12.65 kmpl", "NA", "Trendline, Comfortline", "Luxury Seekers", "4 years/1,00,000 km")
    ],
    "M010": [  # Renault
        ("Kwid", "Hatchback", "Climber AMT", "1.0L Petrol", "Automatic", "Touchscreen Infotainment, Rear Parking Camera", "22.3 kmpl", "NA", "RXE, RXL, RXT, Climber", "First-time Buyers", "2 years/50,000 km"),
        ("Duster", "SUV", "RXS Turbo", "1.3L Petrol", "Manual", "LED DRLs, Hill Start Assist", "16.5 kmpl", "NA", "RXE, RXS, RXZ", "Adventure Enthusiasts", "2 years/50,000 km"),
        ("Triber", "MPV", "RXZ AMT", "1.0L Petrol", "Automatic", "8-inch Touchscreen, Cooled Storage", "20 kmpl", "NA", "RXE, RXL, RXT, RXZ", "Growing Families", "2 years/50,000 km")
    ]
}

def save_to_csv(data, filename):
    headers = [
        'model_id', 'model_name', 'manufacturer_id', 'year_release', 
        'market_segment', 'variant_name', 'engine_type', 'transmission_type', 
        'features', 'fuel_efficiency', 'safety_ratings', 'trim_levels', 
        'target_audience', 'warranty_coverage'
    ]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for manufacturer_id, models in data.items():
            for idx, model in enumerate(models):
                model_id = f"{manufacturer_id}{idx+1:03d}"
                year_release = random.randint(2010, 2022)
                row = [
                    model_id, 
                    model[0],  # model_name
                    manufacturer_id, 
                    year_release, 
                    model[1],  # market_segment
                    model[2],  # variant_name
                    model[3],  # engine_type
                    model[4],  # transmission_type
                    model[5],  # features
                    model[6],  # fuel_efficiency
                    model[7],  # safety_ratings
                    model[8],  # trim_levels
                    model[9],  # target_audience
                    model[10]  # warranty_coverage
                ]
                writer.writerow(row)

# Save the data to a CSV file
save_to_csv(vehicles, 'vehicle_data_new.csv')

print("Data generation complete and saved to vehicle_data.csv")
