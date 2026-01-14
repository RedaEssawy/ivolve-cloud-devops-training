# lab instractions
![Alt Text](assets/images/lab-instractions.png)

# clone the app code
# $ git clone https://github.com/Ibrahim-Adel15/Docker-3.git
![Alt Text](assets/images/clone-app-code.png)

# build the image from the Dockerfile
# $ docker build -t lab6 .
![Alt Text](assets/images/build-image1.png)
![Alt Text](assets/images/build-image2.png)

# the image
# $ docker image ls 
![Alt Text](assets/images/image.png)

# run a lab6_i containre from Dockerfile and path variables in command
# docker container run -d --name lab6_i -e APP_MODE=development -e APP_REGION=us-east -p 8098:5000 lab6
![Alt Text](assets/images/lab6_i_container.png)

# test the lab6_iii container on 8098 port on the browser
![Alt Text](assets/images/lab6_i_test.png)


# run a lab6_ii containre from Dockerfile and path variables in command
# docker container run -d --name lab6_ii --env-file=env -p 8098:5000 lab6
![Alt Text](assets/images/lab6_ii_container.png)

# test the lab6_ii container on 8096 port on the browser
![Alt Text](assets/images/lab6_ii_test.png)


# build the lab6_iii image from Dockerfile 
# note 4/8 step of Environment
# $ docker build -t lab6_iii .
![Alt Text](assets/images/lab6_iii_container.png)

# the lab6_iii container
![Alt Text](assets/images/lab6_iii_container.png)

# test the lab6_iii container on 8094 port on the browser
![Alt Text](assets/images/lab6_iii_test.png)





