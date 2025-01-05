import pickle
import json
import numpy as np

# Global variables to store model and brand names
model = None
brand_names = None
data_columns = None

def load_artifacts():
    global model
    global brand_names
    global data_columns
    
    # Load the model
    with open("server/artifacts/car_price_predict_model.pickle", "rb") as f:
        print("Reading model pickle...")
        model = pickle.load(f)
        print("Reading model pickle completed")
    
    # Load brand names from JSON
    with open("server/artifacts/columns.json", "r") as f:
        data = json.load(f)
        data_columns = data.get("data_columns", [])
        brand_names = data_columns[3:-4]
    

def get_brand_names():
    return brand_names

def predict_price(
        year=2017,  # Default to most common year or mode of 'year'
        km=70,  # Default to mode or median of 'km_driven'
        mileage=19.5,  # Default to mode or median of 'mileage'
        name="maruti",  # Default to most common name in 'name'
        fuel="Diesel",  # Default to mode of 'fuel'
        transmission="Manual"  # Default to mode of 'transmission'
):
    # Convert 'year' to 'car_age' (2025 - year)
    car_age = 2025 - year

    input_data = np.zeros(len(data_columns))  # Create a zero array of feature size

    # Handle 'name'
    if name in data_columns:
        name_loc = data_columns.index(name)
        input_data[name_loc] = 1

    # Handle 'fuel'
    if fuel in data_columns:
        fuel_loc = data_columns.index(fuel)
        input_data[fuel_loc] = 1

    # Handle 'transmission'
    if transmission in data_columns:
        transmission_loc = data_columns.index(transmission)
        input_data[transmission_loc] = 1

    # Fill other numerical fields
    input_data[0] = km
    input_data[1] = mileage
    input_data[2] = car_age

    return round(model.predict([input_data])[0],2)
