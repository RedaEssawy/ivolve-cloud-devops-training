# lab instractions 

![Alt Text](assets/images/lab_instractions.png)

# Clone the App code 
# $ git clone https://github.com/Ibrahim-Adel15/Docker-1.git
![Alt Text](assets/images/clone_app_code.png)

# the app code tree after clonning
![Alt Text](assets/images/tree.png)

# build the app locally
# $ mvn package
# the last snapshot from output that show the success of building process
![Alt Text](assets/images/build.png)


# tree command after building the application, notice that appearing of .jar file that used in the container
![Alt Text](assets/images/tree_after_build_app.png)


# build the lab4 image from Dockerfile with notice the size of the image
# $ docker build -t lab4 .

![Alt Text](assets/images/build_image.png)

# note that the size of this image is half of the size of the previos image as the Dockerfile copy .jar file only
![Alt Text](assets/images/images_size.png)

# build a lab4 container from lab4 image
# $ docker run -d --name lab4 -p 8099:8080 lab4
# $ docker ps -a 
![Alt Text](assets/images/container.png)

# listen on 8099 port from the browser
![Alt Text](assets/images/listen-from-browser.png)