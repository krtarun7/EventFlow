import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('EventAuditLogs')

def lambda_handler(event, context):
    detail = event.get('detail', {})
    event_id = event.get('id', 'test-id')
    amount = detail.get('amount', 0)
    order_id = detail.get('order_id', 'N/A')

    action = "PRIORITY_PROCESSING" if amount >= 100 else "STANDARD"

    table.put_item(
        Item={
            'eventId': event_id,
            'timestamp': datetime.utcnow().isoformat(),
            'orderId': order_id,
            'amount': str(amount),
            'action': action
        }
    )

    return {'statusCode': 200, 'body': 'Processed successfully!'}
