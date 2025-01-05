from flask import Flask, request, jsonify
import util
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Load model and data before the first request
# @app.before_first_request
# def load_data():
util.load_artifacts()

# GET endpoint to fetch brand names
@app.route('/get_brands', methods=['GET'])
def get_brands():
    response = {
        'brands': util.get_brand_names()
    }
    return jsonify(response)

# POST endpoint to predict car price

@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        year = int(request.form['year'])
        km = float(request.form['km_driven'])
        mil = float(request.form['milage'])
        name = request.form['brand']
        fuel = request.form['fuel']
        transmission = request.form['transmission']
        
        prediction = util.predict_price(year, km, mil, name, fuel, transmission)
        
        response = {
            'predicted_price': prediction
        }
        return jsonify(response)
    
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server for Car Resale Price Predict")
    app.run(host='0.0.0.0', port=5000)
