# Week 4 — Postgres and RDS

## Best practice in AWS and application

* Make sure to create the database in the region as it should be compliant with the local law. For example, due to the GDPR, database can not be outside the EU
* Another best practice is to set the encryption on your database.
* The database should not be publicly accessible.
* Must enable deletion protection for unintentional deletion.
* Must be available amazon organization with the SCP put in place.
* Active cloudtrail for auditing purposes and guard duty
* Set on the SG only to the ip for dev/admin so they can access the instance. Do not put 0.0.0.0/0
* Delete the database if not in use.
* Use a secret manager to manage the user/password access for the db
* Encryption in transit and at rest
* Limit the operation of the users.
* Authentication using IAM or Kerberos.

## Create RDS

<img width="967" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/a19541c6-8d2a-4101-8d6a-6dc57a5d3ab1">

## create local database

<img width="486" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/a54ef43a-48f6-418a-9d4d-7634469518d1">

<img width="611" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/e9085a4f-17ff-4428-9dbf-3ab8702cae44">

## Creation connection with RDS

<img width="508" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/4b94f8db-c13a-4bf9-b6f9-c1c6c6cae5e5">

<img width="506" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/04228883-daf8-47e9-9ab3-c977a568507e">


## Create Lambda

<img width="1312" alt="Screenshot 2023-06-08 at 10 18 11 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/33ae73f0-7338-49fd-aa96-ee3c49c6be82">

<img width="868" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/0d5fac86-c73d-430b-a8a3-02de017b90ab">

<img width="1046" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/bbdd0b12-a51f-48f5-998e-76bfb9d044d8">


