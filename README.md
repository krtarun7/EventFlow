# EventFlow - Serverless Event Automation Engine

EventFlow is an event-driven automation pipeline built on AWS. It uses Amazon EventBridge for content-based routing and triggers an AWS Lambda worker to process and log priority events into DynamoDB.

## Track Submitted
Ring (Smart Home & Security Automation)

## Requirements
To run or deploy this project, you need:
- An active AWS Account
- Access to AWS Management Console (Amazon EventBridge, AWS Lambda, Amazon DynamoDB)

## Setup & Deployment Instructions

### 1. Database Setup (Amazon DynamoDB)
- Go to DynamoDB console.
- Create a new table named `EventAuditLogs`.
- Set the Partition Key to `eventId` (String).

### 2. Compute Layer (AWS Lambda)
- Create a new Lambda function named `EventFlowWorker` using Python 3.11.
- Copy the code from `lambda_function.py` in this repository and paste it into your Lambda editor.
- Attach the `AmazonDynamoDBFullAccess` IAM policy to the Lambda execution role.

### 3. Routing Engine (Amazon EventBridge)
- Create a custom Event Bus named `eventflow-bus`.
- Create a new Rule on this bus.
- Set the Event Pattern using the JSON provided in `eventbridge_rule_pattern.json`.
- Set the target to the `EventFlowWorker` Lambda function.

## How to Test
1. Go to Amazon EventBridge -> Buses -> `eventflow-bus`.
2. Click **Send events**.
3. Use Event source: `eventflow.orders` and Detail type: `OrderPlaced`.
4. Paste the following JSON to trigger the Lambda:
   ```json
   {
     "order_id": "ORD-TEST",
     "amount": 250
   }
