# Car Price Predictor

This is a machine learning-based web application for predicting car resale prices with an **85% accuracy score**. The application is live and accessible at: [Car Price Predictor](https://gautam-k05.github.io/car_price_predictor/). 

The server for this application is deployed on [Render.com](https://render.com).

## Application Overview

The application takes user inputs through a **form** that includes the following fields:

- **Brand**: Dropdown menu populated with available car brands.
- **Year of Manufacturing**: Text input for the car's manufacturing year.
- **Kilometres Driven**: Text input for the car's driven distance (in thousands of kilometers).
- **Mileage**: Text input for the car's mileage (km/l).
- **Fuel Type**: Radio buttons for selecting the type of fuel (Petrol, Diesel, LPG, CNG).
- **Transmission Type**: Radio buttons for selecting the transmission type (Manual, Automatic).

After submitting the form, the application predicts the resale price of the car and displays it below the form.

## Features

1. **Interactive Frontend**:
   - Built with HTML, CSS, and JavaScript.
   - Dynamically fetches car brands from the server and provides predictions based on user input.

2. **Flask Backend**:
   - **Endpoints**:
     - `/get_brands`: Returns a list of car brands.
     - `/predict_price`: Accepts user inputs and returns the predicted car resale price.
   - Deployed using **Gunicorn** on Render.com.

3. **Machine Learning Model**:
   - Built using Random Forest Regression.
   - Trained in the `Cars_resell.ipynb` notebook.
   - Serialized as `car_price_predict_model.pickle` and deployed alongside the server.

4. **Utility Functions**:
   - **`load_artefacts`**: Loads model and columns data from files.
   - **`get_brand_names`**: Retrieves a list of car brands for the form.
   - **`predict_price`**: Generates the resale price prediction based on user inputs.

## Project Structure

```

├── docs
│   ├── app.css                # Styling for the frontend
│   ├── app.js                 # JavaScript logic for fetching and posting data
│   ├── index.html             # Frontend HTML structure
├── model
│   ├── Cars_resell.ipynb      # Jupyter Notebook for model creation and training
│   ├── car_price_predict_model.pickle  # Trained Random Forest model
│   ├── columns.json           # Features used by the model
├── server
│   ├── pycache            # Cached Python files
│   ├── artifacts              # Folder containing runtime artefacts
│   ├── requirements.txt       # Flask backend dependencies
│   ├── server.py              # Flask application with API routes
│   ├── util.py                # Utility functions for model usage
├── .gitattributes             # Git configuration
├── README.md                  # Project documentation
```

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Model**: Scikit-learn (Random Forest Regression)
- **Deployment**: GitHub Pages (Frontend), Render.com (Backend)

## Dependencies

The `requirements.txt` file includes the following:
- Flask
- Pandas
- Scikit-learn
- Numpy
- Gunicorn
- Flask-Core

## Live Demo

Try the application here: [Car Price Predictor](https://gautam-k05.github.io/car_price_predictor/)
