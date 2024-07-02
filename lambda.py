import time

def fetch_data():
    time.sleep(2)  # Simulate a long-running process
    return {'name': 'John Doe', 'age': 30}

def process_data(data):
    # Inefficient use of list to accumulate values
    processed_data = []
    for key, value in data.items():
        processed_data.append((key, value))
    return processed_data

def lambda_handler(event, context):
    data = fetch_data()
    
    # Directly accessing potentially missing keys without checking
    name = event['name']
    age = event['age']
    
    processed_data = process_data(data)
    
    return {
        'statusCode': 200,
        'body': f"Hello, {name}. Your processed data is: {processed_data}"
    }
