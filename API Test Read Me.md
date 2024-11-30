# Instruction for running API request 
# API url endpoint
    https://fxi92sp7di.execute-api.us-east-1.amazonaws.com/dev/predict-fire

# Method 
    GET
# body JSON format example
    {
    "region": 1,
    "date" : "12/11/2023"
    }
# Testing tool 

 - Option1 - POSTMan:
    Create a new GET request:
    URL: Paste the API Gateway endpoint.
    Headers:
        Content-Type: application/json
    Body: Select raw and paste the JSON input.
    Click **Send** to test the API.
    Check the response under the Body tab.

 - Option2 - CURL (command line)
    use the following curl command:
        curl -X GET https://fxi92sp7di.execute-api.us-east-1.amazonaws.com/dev/predict-fire \
        -H "Content-Type: application/json" \
        -d '{
        "region": 1,
        "date" : "12/11/2023"
        }'
    
    Replace the region and date of your choice

# Note: 
    my API is working but I had issues with installing the python packages. 
    I just want to demonstrate my ability to deploy API endpoint the response will be some source of unable to import packages