# Serverless E-Commerce Order Processing System on AWS

##  Project Overview

This is a **serverless e-commerce application** built using AWS services.  
It provides:

- Product listing
- Placing an order
- A secure and scalable architecture using serverless components

---

##  Architecture

<img width="731" height="400" alt="image" src="https://github.com/user-attachments/assets/2b88ac7a-375b-4658-ac04-b54f76d45bf0" />





  
---

##  AWS Services Used

- Amazon S3  
- Amazon CloudFront  
- AWS WAF  
- Amazon API Gateway  
- AWS Lambda  
- Amazon DynamoDB  
- IAM (Roles and Policies)  
- Amazon CloudWatch  

---

##  Features

- Fully serverless – no servers to manage
- Scalable and cost-efficient
- API for listing products and placing orders
- Product images stored in S3
- Secured with WAF and IAM roles

---


---

## API Endpoints

### GET `/products`

- Returns a list of available products

### POST `/order`

- Accepts order payload and stores it in the database

---

## How to Deploy

### Frontend (S3 + CloudFront)

1. Create an S3 bucket
2. Enable static website hosting
3. Upload your `index.html` and other static files

### Backend (API Gateway + Lambda + DynamoDB)

1. Create an API Gateway REST API
2. Create Lambda functions:
   - `get_products.py`
   - `place_order.py`
3. Create DynamoDB tables:
   - `Products` table
   - `Orders` table
4. Give Lambda permission to access DynamoDB and S3

---

##  Security

- Use IAM roles with least privilege
- Add input validation to Lambda
- Use AWS WAF to protect the frontend


---

##  Future Improvements

- Add Cognito user authentication
- Add Stripe/PayPal payment gateway
- Order history and tracking
- CI/CD pipeline with CodePipeline

---







