# Week 1 — App Containerization

Run the dockerfile CMD as an external script:

Coded the python command to run flask in shell script and then call it within the image build:

<img width="606" alt="image" src="https://user-images.githubusercontent.com/110344576/221351586-dda1dc82-146a-482e-bfaa-77e4e104a8b6.png">

<img width="309" alt="image" src="https://user-images.githubusercontent.com/110344576/221351907-c40b4a17-cb26-4ad2-a422-5a9d8f4a7402.png">


<img width="840" alt="image" src="https://user-images.githubusercontent.com/110344576/221351510-4954e9c9-54a4-4a83-905d-b285b694b4c8.png">

Push and tag a image to DockerHub

logged in to my Docker account:

<img width="917" alt="image" src="https://user-images.githubusercontent.com/110344576/221352004-1dd00c08-18bf-48e6-a7ac-8f506b079369.png">

Pushed tagged image to my Dockerhub repo:

<img width="868" alt="image" src="https://user-images.githubusercontent.com/110344576/221352292-f4cfe274-0e83-455b-afe7-22fcd003486f.png">

<img width="951" alt="image" src="https://user-images.githubusercontent.com/110344576/221352324-53fd7c66-58d4-43be-bf69-ebdcace57610.png">

Best Practices for writing Dockerfiles:

Use a .dockerignore file
Containers should be immutable & ephemeral
Minimize the number of layers / Consolidate instructions
Avoid installing unnecessary packages

Installed Docker desktop on my machine and pulled backend-flask image from my repo:

<img width="1268" alt="image" src="https://user-images.githubusercontent.com/110344576/221352457-61bbd07b-1e1d-4b37-8435-8b3a92f0423d.png">

Container is running locally:

<img width="1268" alt="image" src="https://user-images.githubusercontent.com/110344576/221352747-f1057910-2508-46ae-a9e1-32e469a2ef38.png">


Launched an EC2 instance and installed docker on it and ran an image of backend-flask:

<img width="1426" alt="image" src="https://user-images.githubusercontent.com/110344576/221363224-5fe400f5-61d7-4138-ae8c-b535cf6bea57.png">
