# Week 10 — CloudFormation Part 1

## Network and Cluster layers CloudTrail event logs:

| Event time            | Event source                   | Event name                 | AWS region | Source IP address      | User agent                                                     | Error code | Resources                                                                                                                                                                                                                          |
|-----------------------|--------------------------------|----------------------------|------------|------------------------|----------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2023-07-12T06:44:23Z | ec2.amazonaws.com              | CreateNetworkInterface     | us-east-1  | elasticloadbalancing.amazonaws.com | elasticloadbalancing.amazonaws.com |            | [{"resourceType":"AWS::EC2::VPC","resourceName":"vpc-0b3c8f1fd1e78f7d2"},{"resourceType":"AWS::EC2::NetworkInterface","resourceName":"eni-0a99a73dd0161a0f9"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"CrdClusterALBSecurityGroup"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"sg-05b792394f30d5c59"},{"resourceType":"AWS::EC2::Subnet","resourceName":"subnet-018064942529c638d"}] |
| 2023-07-12T06:44:21Z | ec2.amazonaws.com              | CreateNetworkInterface     | us-east-1  | elasticloadbalancing.amazonaws.com | elasticloadbalancing.amazonaws.com |            | [{"resourceType":"AWS::EC2::VPC","resourceName":"vpc-0b3c8f1fd1e78f7d2"},{"resourceType":"AWS::EC2::NetworkInterface","resourceName":"eni-05dc2ef1230b6e184"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"CrdClusterALBSecurityGroup"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"sg-05b792394f30d5c59"},{"resourceType":"AWS::EC2::Subnet","resourceName":"subnet-0db5c978782c987c2"}] |
| 2023-07-12T06:44:02Z | elasticloadbalancing.amazonaws.com | CreateRule                 | us-east-1  | cloudformation.amazonaws.com      | AWS Internal                                                  |            | [{"resourceType":"AWS::ElasticLoadBalancingV2::ListenerRule","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:listener-rule/app/CrdClusterALB/cd10f1f8dfd72d5d/1534f131df25de37/34c4e5927334ea49"},{"resourceType":"AWS::ElasticLoadBalancingV2::Listener","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:listener/app/CrdClusterALB/cd10f1f8dfd72d5d/1534f131df25de37"},{"resourceType":"AWS::ElasticLoadBalancingV2::TargetGroup","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:targetgroup/CrdClu-Backe-CZ7FGOCHFKFG/bafefead5603c73b"}] |
| 2023-07-12T06:43:59Z | kms.amazonaws.com               | CreateGrant                | us-east-1  | acm.amazonaws.com               | AWS Internal                                                  |            | [{"resourceType":"AWS::KMS::Key","resourceName":"3c281122-91d2-45b7-bd30-daa7f830482f"},{"resourceType":"AWS::KMS::Key","resourceName":"arn:aws:kms:us-east-1:470836252788:key/3c281122-91d2-45b7-bd30-daa7f830482f"}] |
| 2023-07-12T06:43:59Z | elasticloadbalancing.amazonaws.com | CreateListener             | us-east-1  | cloudformation.amazonaws.com      | AWS Internal                                                  |            | [{"resourceType":"AWS::ElasticLoadBalancingV2::LoadBalancer","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:loadbalancer/app/CrdClusterALB/cd10f1f8dfd72d5d"},{"resourceType":"AWS::ElasticLoadBalancingV2::Listener","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:listener/app/CrdClusterALB/cd10f1f8dfd72d5d/1534f131df25de37"},{"resourceType":"AWS::ElasticLoadBalancingV2::TargetGroup","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:targetgroup/CrdClu-Front-EZDGLYZWWWTI/7156c8006343de15"}] |
| 2023-07-12T06:43:58Z | elasticloadbalancing.amazonaws.com | CreateListener             | us-east-1  | cloudformation.amazonaws.com      | AWS Internal                                                  |            | [{"resourceType":"AWS::ElasticLoadBalancingV2::LoadBalancer","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:loadbalancer/app/CrdClusterALB/cd10f1f8dfd72d5d"},{"resourceType":"AWS::ElasticLoadBalancingV2::Listener","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:listener/app/CrdClusterALB/cd10f1f8dfd72d5d/f9264a18e1090ebd"}] |
| 2023-07-12T06:43:56Z | elasticloadbalancing.amazonaws.com | ModifyLoadBalancerAttributes | us-east-1  | cloudformation.amazonaws.com      | AWS Internal                                                  |            | [{"resourceType":"AWS::ElasticLoadBalancingV2::LoadBalancer","resourceName":"arn:aws:elasticloadbalancing:us-east-1:470836252788:loadbalancer/app/CrdClusterALB/cd10f1f8dfd72d5d"}] |
| 2023-07-12T06:42:09Z | ec2.amazonaws.com              | CreateNetworkInterface     | us-east-1  | elasticloadbalancing.amazonaws.com | elasticloadbalancing.amazonaws.com |            | [{"resourceType":"AWS::EC2::VPC","resourceName":"vpc-0b3c8f1fd1e78f7d2"},{"resourceType":"AWS::EC2::NetworkInterface","resourceName":"eni-0751658d4e1ae329d"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"CrdClusterALBSecurityGroup"},{"resourceType":"AWS::EC2::SecurityGroup","resourceName":"sg-05b792394f30d5c59"},{"resourceType":"AWS::EC2::Subnet","resourceName":"subnet-036777


### CFN Network POC:

<img width="1440" alt="Screenshot 2023-07-12 at 10 33 38 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/026e8deb-78fa-44bb-809d-aa337a815df1">

<img width="1372" alt="Screenshot 2023-07-12 at 11 24 13 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/af304e28-e8b9-4cbe-8788-870c67e53388">



### CFN Cluster POC:
<img width="1440" alt="Screenshot 2023-07-12 at 10 48 03 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/83cb0953-74c1-4931-8dad-0ed7f0b3e7bc">

<img width="854" alt="Screenshot 2023-07-12 at 11 22 52 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/deb19daf-2601-4ca7-a96e-0ca895c2e5e8">

<img width="1372" alt="Screenshot 2023-07-12 at 11 24 01 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/7e1d12ad-7459-4a5d-b361-c4192a15905e">

### CFN Backend service POC:

<img width="1426" alt="Screenshot 2023-07-12 at 12 30 00 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/078dd925-f646-412a-8c43-293923f0052a">

<img width="1151" alt="Screenshot 2023-07-12 at 12 31 48 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/762ad506-10c5-440c-ab5e-d9c0a4011bc9">

<img width="1119" alt="Screenshot 2023-07-12 at 12 32 01 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/9fd9c412-4d52-4e8e-b948-f405685611cf">


### CFN RDS POC:

<img width="1360" alt="Screenshot 2023-07-12 at 5 59 34 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/959c434f-2824-4a36-9a88-632f90384641">



### CFN DDB POC:

<img width="1185" alt="Screenshot 2023-07-30 at 10 35 18 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/efb2250e-a00f-4d06-984b-4e8d9fbf1f1c">

<img width="929" alt="Screenshot 2023-07-30 at 10 36 00 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/74cb0880-1aa9-47c0-b847-a9de8345d255">

#### CFN DDB lambda POC:

<img width="1047" alt="Screenshot 2023-07-31 at 9 53 37 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/35591f90-b17a-4873-90df-3128ebd8167d">

<img width="1044" alt="Screenshot 2023-07-31 at 9 54 34 AM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/dfac2dbc-3f26-472a-b995-8fcdf5cb73fc">



### CFN Frontend service POC:

<img width="1153" alt="Screenshot 2023-07-31 at 5 44 47 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/467ca737-25c0-4934-8a9f-3d364a7bf43c">

<img width="1123" alt="Screenshot 2023-07-31 at 5 45 38 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/19848a2a-f0ec-421a-9df7-b85b19215364">
