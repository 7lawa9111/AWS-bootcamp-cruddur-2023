# Week 5 — DynamoDB and Serverless Caching

## How to access DynamoDB

![dynamodb](https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/b90b1e71-0605-4843-9340-dd4cb38e9b5f)

![accessdb](https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/131ba8c0-b756-43d3-81c0-d753d6872a2c)


### communication with dyanomodb within aws private network

![awsvpn](https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/93c83806-8cd4-4975-b9a3-8d5d4f98412c)

## Data Modelling

For the messaging part, we will implement a single table data modelling using Dynamo DB. Below you will see the pattern for CRUDDUR

1- Pattern A: Shows the messages. Users can see the list of the messages that belong to a message group.
2- Pattern B: Shows the message group conversation with a specific user.
3- Pattern C: Create a new message in a new message group.
4- Pattern D: Create a new message in an exisintg group.

![message pattern](https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/c6d91853-dd8d-4c00-a495-99e03e00210e)

## Implementations

### DynamoDB Scripts

<img width="152" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/99cbefd1-0f56-4e63-bdd4-4eabd02c739f">

## Implementation of Messages with the local DynamoDB

<img width="549" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/4501f3a3-b7b5-436f-ba26-882e95077bab">

<img width="927" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/d6da2a5c-7de3-4de5-89f7-a9f80ed26bfb">

<img width="1312" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/700761c8-1e27-4a60-bb4b-d61363b494a9">

## Implementation DynamoDB Data Stream to update message groups

<img width="1312" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/9c74f604-86c7-4267-94b8-3d23aba991f6">

