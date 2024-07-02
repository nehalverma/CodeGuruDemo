import json

def lambda_handler(event, context):
    # This code tries to access a key 'name' which may not exist
    name = event['name']
    
    # This is missing a return statement
    greeting = "Hello, " + name
    
    return {
        'statusCode': 200,
        'body': json.dumps(greeting)
    }
