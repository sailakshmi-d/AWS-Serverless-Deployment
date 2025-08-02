import json 
import boto3 
import uuid 
from datetime import datetime 
dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('Orders') 
def lambda_handler(event, context): 
    try: 
        # HTTP API sends body as a string 
        if "body" not in event or event["body"] is None: 
            return { 
                "statusCode": 400, 
                "headers": { 
                    "Access-Control-Allow-Origin": "*" 
                }, 
                "body": json.dumps({"message": "Missing request body"}) 
            }  
        data = json.loads(event["body"])  # Safely parse body string into JSON 
        items = data.get("items", [])  
        if not items: 
            return { 
                "statusCode": 400, 
                "headers": { 
                    "Access-Control-Allow-Origin": "*" 
                }, 
                "body": json.dumps({"message": "Order items required"}) 
            }  
        order_id = str(uuid.uuid4()) 
        order_date = datetime.utcnow().isoformat() 
        order = { 
            "orderId": order_id, 
            "items": items, 
            "orderDate": order_date 
        } 
        table.put_item(Item=order) 
        return { 
            "statusCode": 200, 
            "headers": { 
                "Access-Control-Allow-Origin": "*", 
                "Content-Type": "application/json" 
            }, 
            "body": json.dumps({ 
                "message": "Order placed successfully", 
                "orderId": order_id 
            }) 
        } 
    except Exception as e: 
        return { 
            "statusCode": 500, 
            "headers": { 
                "Access-Control-Allow-Origin": "*", 
                "Content-Type": "application/json" 
            }, 
            "body": json.dumps({"error": str(e)}) 
        } 

 
