# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy


In this implementation, our goal is to automate the code deployment process instead of relying on manual steps. To achieve this, we will utilize CodePipeline and CodeBuild services. Once the code is merged from the main branch to the prod branch, the pipeline will automatically trigger the deployment process.

## CodeBuild Project:


<img width="1091" alt="Screenshot 2023-07-03 at 10 12 18 PM" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/cd313bed-41da-468c-9393-c8c493f3e9ca">











## Successfull pipeline logs:
```

[Container] 2023/07/03 18:10:56 Waiting for agent ping
[Container] 2023/07/03 18:10:57 Waiting for DOWNLOAD_SOURCE
[Container] 2023/07/03 18:11:02 Phase is DOWNLOAD_SOURCE
[Container] 2023/07/03 18:11:02 CODEBUILD_SRC_DIR=/codebuild/output/src2544599250/src/github.com/7lawa9111/aws-bootcamp-cruddur-2023
[Container] 2023/07/03 18:11:02 YAML location is /codebuild/output/src2544599250/src/github.com/7lawa9111/aws-bootcamp-cruddur-2023/backend-flask/buildspec.yml
[Container] 2023/07/03 18:11:02 Setting HTTP client timeout to higher timeout for Github and GitHub Enterprise sources
[Container] 2023/07/03 18:11:02 Processing environment variables
[Container] 2023/07/03 18:11:02 No runtime version selected in buildspec.
[Container] 2023/07/03 18:11:02 Moving to directory /codebuild/output/src2544599250/src/github.com/7lawa9111/aws-bootcamp-cruddur-2023
[Container] 2023/07/03 18:11:02 Configuring ssm agent with target id: codebuild:6f20c21c-f4b3-46c6-93ee-1602058f411d
[Container] 2023/07/03 18:11:02 Successfully updated ssm agent configuration
[Container] 2023/07/03 18:11:02 Registering with agent
[Container] 2023/07/03 18:11:02 Phases found in YAML: 3
[Container] 2023/07/03 18:11:02  POST_BUILD: 6 commands
[Container] 2023/07/03 18:11:02  INSTALL: 3 commands
[Container] 2023/07/03 18:11:02  BUILD: 4 commands
[Container] 2023/07/03 18:11:02 Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
[Container] 2023/07/03 18:11:02 Phase context status code:  Message: 
[Container] 2023/07/03 18:11:03 Entering phase INSTALL
[Container] 2023/07/03 18:11:03 Running command echo "cd into $CODEBUILD_SRC_DIR/backend-flask"
cd into /codebuild/output/src2544599250/src/github.com/7lawa9111/aws-bootcamp-cruddur-2023/backend-flask

[Container] 2023/07/03 18:11:03 Running command cd $CODEBUILD_SRC_DIR/backend-flask

[Container] 2023/07/03 18:11:03 Running command aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_URL
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

[Container] 2023/07/03 18:11:13 Phase complete: INSTALL State: SUCCEEDED
[Container] 2023/07/03 18:11:13 Phase context status code:  Message: 
[Container] 2023/07/03 18:11:13 Entering phase PRE_BUILD
[Container] 2023/07/03 18:11:13 Phase complete: PRE_BUILD State: SUCCEEDED
[Container] 2023/07/03 18:11:13 Phase context status code:  Message: 
[Container] 2023/07/03 18:11:13 Entering phase BUILD
[Container] 2023/07/03 18:11:13 Running command echo Build started on `date`
Build started on Mon Jul 3 18:11:13 UTC 2023

[Container] 2023/07/03 18:11:13 Running command echo Building the Docker image...
Building the Docker image...

[Container] 2023/07/03 18:11:13 Running command docker build -f Dockerfile.prod -t backend-flask .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  82.94kB

Step 1/7 : FROM 47xxxxxxx88.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster
3.10-slim-buster: Pulling from cruddur-python
9fbefa337077: Pulling fs layer
a25702e0699e: Pulling fs layer
adf6e8027509: Pulling fs layer
a68430a46d9d: Pulling fs layer
433875ea4139: Pulling fs layer
a68430a46d9d: Waiting
433875ea4139: Waiting
a25702e0699e: Verifying Checksum
a25702e0699e: Download complete
a68430a46d9d: Download complete
adf6e8027509: Verifying Checksum
adf6e8027509: Download complete
433875ea4139: Verifying Checksum
433875ea4139: Download complete
9fbefa337077: Verifying Checksum
9fbefa337077: Download complete
9fbefa337077: Pull complete
a25702e0699e: Pull complete
adf6e8027509: Pull complete
a68430a46d9d: Pull complete
433875ea4139: Pull complete
Digest: sha256:7857e9a198fc4b06818b0e064c13b21485b72c7fdb1f51d3b13c9854ca2fcfa5
Status: Downloaded newer image for 47xxxxxx88.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster
 ---> 6f74f1480ab7
Step 2/7 : WORKDIR /backend-flask
 ---> Running in 9f6f075f5969
Removing intermediate container 9f6f075f5969
 ---> a7e1bc7e9604
Step 3/7 : COPY requirements.txt requirements.txt
 ---> a5afd14fa17d
Step 4/7 : RUN pip3 install -r requirements.txt
 ---> Running in 2a11d80530a7
Collecting flask
  Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 19.2 MB/s eta 0:00:00
Collecting flask-cors
  Downloading Flask_Cors-4.0.0-py2.py3-none-any.whl (14 kB)
Collecting opentelemetry-api
  Downloading opentelemetry_api-1.18.0-py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.3/57.3 kB 17.5 MB/s eta 0:00:00
Collecting opentelemetry-sdk
  Downloading opentelemetry_sdk-1.18.0-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.6/101.6 kB 20.8 MB/s eta 0:00:00
Collecting opentelemetry-exporter-otlp-proto-http
  Downloading opentelemetry_exporter_otlp_proto_http-1.18.0-py3-none-any.whl (17 kB)
Collecting opentelemetry-instrumentation-flask
  Downloading opentelemetry_instrumentation_flask-0.39b0-py3-none-any.whl (13 kB)
Collecting opentelemetry-instrumentation-requests
  Downloading opentelemetry_instrumentation_requests-0.39b0-py3-none-any.whl (11 kB)
Collecting blinker
  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
Collecting rollbar
  Downloading rollbar-0.16.3-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.1/98.1 kB 28.9 MB/s eta 0:00:00
Collecting Flask-AWSCognito
  Downloading Flask_AWSCognito-1.3-py3-none-any.whl (12 kB)
Collecting psycopg[binary]
  Downloading psycopg-3.1.9-py3-none-any.whl (167 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.8/167.8 kB 28.3 MB/s eta 0:00:00
Collecting boto3
  Downloading boto3-1.26.165-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.9/135.9 kB 30.8 MB/s eta 0:00:00
Collecting python-dateutil
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 45.2 MB/s eta 0:00:00
Collecting momento
  Downloading momento-1.6.1-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.6/98.6 kB 24.8 MB/s eta 0:00:00
Collecting Werkzeug>=2.3.3
  Downloading Werkzeug-2.3.6-py3-none-any.whl (242 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 47.9 MB/s eta 0:00:00
Collecting click>=8.1.3
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 29.9 MB/s eta 0:00:00
Collecting Jinja2>=3.1.2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 32.6 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Requirement already satisfied: setuptools>=16.0 in /usr/local/lib/python3.10/site-packages (from opentelemetry-api->-r requirements.txt (line 4)) (65.5.1)
Collecting importlib-metadata~=6.0.0
  Downloading importlib_metadata-6.0.1-py3-none-any.whl (21 kB)
Collecting deprecated>=1.2.6
  Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)
Collecting opentelemetry-semantic-conventions==0.39b0
  Downloading opentelemetry_semantic_conventions-0.39b0-py3-none-any.whl (26 kB)
Collecting typing-extensions>=3.7.4
  Downloading typing_extensions-4.7.1-py3-none-any.whl (33 kB)
Collecting opentelemetry-proto==1.18.0
  Downloading opentelemetry_proto-1.18.0-py3-none-any.whl (52 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.6/52.6 kB 17.0 MB/s eta 0:00:00
Collecting backoff<3.0.0,>=1.10.0
  Downloading backoff-2.2.1-py3-none-any.whl (15 kB)
Collecting opentelemetry-exporter-otlp-proto-common==1.18.0
  Downloading opentelemetry_exporter_otlp_proto_common-1.18.0-py3-none-any.whl (17 kB)
Collecting requests~=2.7
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 1.8 MB/s eta 0:00:00
Collecting googleapis-common-protos~=1.52
  Downloading googleapis_common_protos-1.59.1-py2.py3-none-any.whl (224 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 42.0 MB/s eta 0:00:00
Collecting protobuf<5.0,>=3.19
  Downloading protobuf-4.23.3-cp37-abi3-manylinux2014_x86_64.whl (304 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 304.5/304.5 kB 11.4 MB/s eta 0:00:00
Collecting opentelemetry-instrumentation-wsgi==0.39b0
  Downloading opentelemetry_instrumentation_wsgi-0.39b0-py3-none-any.whl (12 kB)
Collecting opentelemetry-instrumentation==0.39b0
  Downloading opentelemetry_instrumentation-0.39b0-py3-none-any.whl (24 kB)
Collecting opentelemetry-util-http==0.39b0
  Downloading opentelemetry_util_http-0.39b0-py3-none-any.whl (6.7 kB)
Collecting wrapt<2.0.0,>=1.0.0
  Downloading wrapt-1.15.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.4/78.4 kB 24.3 MB/s eta 0:00:00
Collecting six>=1.9.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting python-jose
  Downloading python_jose-3.3.0-py2.py3-none-any.whl (33 kB)
Collecting psycopg-binary==3.1.9
  Downloading psycopg_binary-3.1.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 94.8 MB/s eta 0:00:00
Collecting psycopg-pool
  Downloading psycopg_pool-3.1.7-py3-none-any.whl (30 kB)
Collecting botocore<1.30.0,>=1.29.165
  Downloading botocore-1.29.165-py3-none-any.whl (11.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.0/11.0 MB 111.1 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.7.0,>=0.6.0
  Downloading s3transfer-0.6.1-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.8/79.8 kB 21.4 MB/s eta 0:00:00
Collecting grpcio<2.0.0,>=1.46.0
  Downloading grpcio-1.56.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 120.9 MB/s eta 0:00:00
Collecting momento-wire-types<0.65,>=0.64
  Downloading momento_wire_types-0.64.1-py3-none-any.whl (53 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.6/53.6 kB 17.4 MB/s eta 0:00:00
Collecting pyjwt<3.0.0,>=2.4.0
  Downloading PyJWT-2.7.0-py3-none-any.whl (22 kB)
Collecting urllib3<1.27,>=1.25.4
  Downloading urllib3-1.26.16-py2.py3-none-any.whl (143 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.1/143.1 kB 33.8 MB/s eta 0:00:00
Collecting zipp>=0.5
  Downloading zipp-3.15.0-py3-none-any.whl (6.8 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 18.5 MB/s eta 0:00:00
Collecting charset-normalizer<4,>=2
  Downloading charset_normalizer-3.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (199 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.3/199.3 kB 35.3 MB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2023.5.7-py3-none-any.whl (156 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.0/157.0 kB 39.9 MB/s eta 0:00:00
Collecting rsa
  Downloading rsa-4.9-py3-none-any.whl (34 kB)
Collecting ecdsa!=0.15
  Downloading ecdsa-0.18.0-py2.py3-none-any.whl (142 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 142.9/142.9 kB 15.5 MB/s eta 0:00:00
Collecting pyasn1
  Downloading pyasn1-0.5.0-py2.py3-none-any.whl (83 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.9/83.9 kB 18.8 MB/s eta 0:00:00
Installing collected packages: zipp, wrapt, urllib3, typing-extensions, six, pyjwt, pyasn1, psycopg-binary, protobuf, opentelemetry-util-http, opentelemetry-semantic-conventions, MarkupSafe, jmespath, itsdangerous, idna, grpcio, click, charset-normalizer, certifi, blinker, backoff, Werkzeug, rsa, requests, python-dateutil, psycopg-pool, psycopg, opentelemetry-proto, momento-wire-types, Jinja2, importlib-metadata, googleapis-common-protos, ecdsa, deprecated, rollbar, python-jose, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, momento, flask, botocore, s3transfer, opentelemetry-sdk, opentelemetry-instrumentation, flask-cors, Flask-AWSCognito, opentelemetry-instrumentation-wsgi, opentelemetry-instrumentation-requests, opentelemetry-exporter-otlp-proto-http, boto3, opentelemetry-instrumentation-flask
Successfully installed Flask-AWSCognito-1.3 Jinja2-3.1.2 MarkupSafe-2.1.3 Werkzeug-2.3.6 backoff-2.2.1 blinker-1.6.2 boto3-1.26.165 botocore-1.29.165 certifi-2023.5.7 charset-normalizer-3.1.0 click-8.1.3 deprecated-1.2.14 ecdsa-0.18.0 flask-2.3.2 flask-cors-4.0.0 googleapis-common-protos-1.59.1 grpcio-1.56.0 idna-3.4 importlib-metadata-6.0.1 itsdangerous-2.1.2 jmespath-1.0.1 momento-1.6.1 momento-wire-types-0.64.1 opentelemetry-api-1.18.0 opentelemetry-exporter-otlp-proto-common-1.18.0 opentelemetry-exporter-otlp-proto-http-1.18.0 opentelemetry-instrumentation-0.39b0 opentelemetry-instrumentation-flask-0.39b0 opentelemetry-instrumentation-requests-0.39b0 opentelemetry-instrumentation-wsgi-0.39b0 opentelemetry-proto-1.18.0 opentelemetry-sdk-1.18.0 opentelemetry-semantic-conventions-0.39b0 opentelemetry-util-http-0.39b0 protobuf-4.23.3 psycopg-3.1.9 psycopg-binary-3.1.9 psycopg-pool-3.1.7 pyasn1-0.5.0 pyjwt-2.7.0 python-dateutil-2.8.2 python-jose-3.3.0 requests-2.31.0 rollbar-0.16.3 rsa-4.9 s3transfer-0.6.1 six-1.16.0 typing-extensions-4.7.1 urllib3-1.26.16 wrapt-1.15.0 zipp-3.15.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 23.1.2
[notice] To update, run: pip install --upgrade pip
Removing intermediate container 2a11d80530a7
 ---> 805d0e6ba5d1
Step 5/7 : COPY . .
 ---> 1efcb19ec4d2
Step 6/7 : EXPOSE ${PORT}
 ---> Running in b3f770d46ee2
Removing intermediate container b3f770d46ee2
 ---> 0021c1967adf
Step 7/7 : CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567", "--no-debug", "--no-debugger", "--no-reload"]
 ---> Running in 5db441c427fc
Removing intermediate container 5db441c427fc
 ---> 56aa915c4f85
Successfully built 56aa915c4f85
Successfully tagged backend-flask:latest

[Container] 2023/07/03 18:11:34 Running command docker tag $REPO_NAME $IMAGE_URL/$REPO_NAME

[Container] 2023/07/03 18:11:34 Phase complete: BUILD State: SUCCEEDED
[Container] 2023/07/03 18:11:34 Phase context status code:  Message: 
[Container] 2023/07/03 18:11:35 Entering phase POST_BUILD
[Container] 2023/07/03 18:11:35 Running command echo Build completed on `date`
Build completed on Mon Jul 3 18:11:35 UTC 2023

[Container] 2023/07/03 18:11:35 Running command echo Pushing the Docker image..
Pushing the Docker image..

[Container] 2023/07/03 18:11:35 Running command docker push $IMAGE_URL/$REPO_NAME
The push refers to repository [47xxxxxx88.dkr.ecr.us-east-1.amazonaws.com/backend-flask]
710d02d49795: Preparing
69dbf9c7bf64: Preparing
7c5b563dfc05: Preparing
ba490aba67a1: Preparing
7f2fe4cb548a: Preparing
c7787300a586: Preparing
039e9922562b: Preparing
ccc60df26c61: Preparing
61a5c84a1270: Preparing
039e9922562b: Waiting
ccc60df26c61: Waiting
61a5c84a1270: Waiting
c7787300a586: Waiting
7f2fe4cb548a: Layer already exists
c7787300a586: Layer already exists
039e9922562b: Layer already exists
ccc60df26c61: Layer already exists
61a5c84a1270: Layer already exists
7c5b563dfc05: Pushed
ba490aba67a1: Pushed
710d02d49795: Pushed
69dbf9c7bf64: Pushed
latest: digest: sha256:a13df5ef5fc94e4628bea0c388a8fa0d4616a4bdb53bc4021cc1c9d3c3ad5471 size: 2205

[Container] 2023/07/03 18:11:41 Running command cd $CODEBUILD_SRC_DIR

[Container] 2023/07/03 18:11:41 Running command echo "imagedefinitions.json > [{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json

[Container] 2023/07/03 18:11:41 Running command printf "[{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json

[Container] 2023/07/03 18:11:41 Phase complete: POST_BUILD State: SUCCEEDED
[Container] 2023/07/03 18:11:41 Phase context status code:  Message: 
[Container] 2023/07/03 18:11:41 Phase complete: UPLOAD_ARTIFACTS State: SUCCEEDED
[Container] 2023/07/03 18:11:41 Phase context status code:  Message: 

```



## Backend fargate codepipeline:

<img width="1091" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/bf328e90-617b-4c1d-be6f-577c8b0ac072">


<img width="1089" alt="image" src="https://github.com/7lawa9111/aws-bootcamp-cruddur-2023/assets/110344576/54996401-a8d9-4787-89dc-dea0f2b965e3">
