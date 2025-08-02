import json 
import boto3 
from decimal import Decimal 
dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('Products') 
class DecimalEncoder(json.JSONEncoder): 
    def default(self, o): 
      if isinstance(o, Decimal): 
            return float(o) 
        return super().default(o)  
def lambda_handler(event, context): 
    try: 
        response = table.scan() 
        products = response.get('Items', []) 
        return { 
          'statusCode': 200, 
            'headers': { 
                'Access-Control-Allow-Origin': '*', 
                'Content-Type': 'application/json' 
            }, 
            'body': json.dumps(products, cls=DecimalEncoder) 
        } 
    except Exception as e: 
        return { 
            'statusCode': 500, 
            'headers': { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' }, 
            'body': json.dumps({'error': str(e)}) 
        } 
