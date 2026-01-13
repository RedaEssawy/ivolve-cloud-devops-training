# fist stage

FROM maven:3.9.12-amazoncorretto-17-alpine as build

WORKDIR /lab5

COPY . . 

RUN mvn package


# second stage

FROM eclipse-temurin:17.0.17_10-jre-alpine-3.23

WORKDIR /final

COPY --from=build  lab5/target/demo-0.0.1-SNAPSHOT.jar  .

CMD [ "java", "-jar","demo-0.0.1-SNAPSHOT.jar" ]

EXPOSE 8080