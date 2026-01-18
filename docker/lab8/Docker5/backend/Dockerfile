FROM  python:3.15.0a5-alpine3.22

WORKDIR /app

RUN pip install flask

COPY app.py .

EXPOSE 5000

CMD [ "python", "app.py" ]