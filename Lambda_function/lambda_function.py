import json
import joblib
import pandas as pd

# Load the model and feature list
model_path = '/var/task/logistic_model.pkl'
features_path = '/var/task/model_features.pkl'
csv_file_path = '/var/task/n240.csv'

# Load the model, features, and dataset
model = joblib.load(model_path)
feature_columns = joblib.load(features_path)
data = pd.read_csv(csv_file_path)

def lambda_handler(event, context):
    try:
        # Parse the input JSON
        input_data = json.loads(event['body'])

        # Extract region and date from input
        region = input_data.get("region")
        date = input_data.get("date")

        if not region or not date:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'region' or 'date' in input"})
            }

        # Find the row matching the region and date
        matching_row = data[(data['region_id'] == region) & (data['date'] == date)]

        if matching_row.empty:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "No matching data found for the given region and date"})
            }

        # Extract features for prediction
        features = matching_row.iloc[0][feature_columns].values

        # Make prediction
        prediction = model.predict([features])

        # Prepare the response
        response = {
            "region": region,
            "date": date,
            "prediction": int(prediction[0]),
            "message": "Fire Risk Detected" if prediction[0] == 1 else "No Fire Risk"
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
