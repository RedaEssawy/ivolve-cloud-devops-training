# lab istractions and overview
![Alt Text](assets/images/lab_instractions.png)

# clone the frontend and backend code
# $ git clone  https://github.com/Ibrahim-Adel15/Docker5.git
![Alt Text](assets/images/clone_repo.png)

# first build frontend image using Dockerfile to use it in frontend1, and frontend2 container
# $ docker build -t frontend-image .
![Alt Text](assets/images/frontend-image.png)
![Alt Text](assets/images/front&back-image.png)


# second build backend image using Dockerfile to use it in backend container# $ docker build -t backent-image .
![Alt Text](assets/images/backend-image.png)     
![Alt Text](assets/images/backend-image-pic2.png)
![Alt Text](assets/images/front&back-image.png)

# run the  backend-container container using backent image in ivolve-network network 
# $ docker container run --name backend-container -d -p 8090:5000 backent-image
![Alt Text](assets/images/backend-container.png)

# run the front-container container using fron-image in ivolve-network network
# $ docker container run --name frontend-container -d --network ivolve-network -p 8095:5000 front-image

![Alt Text](assets/images/front-cont-ivlov-network.png)

# run frontend2 container with the default network using front-image image
# $ docker container run --name frontend2 -d  -p 8098:5000 front-image

