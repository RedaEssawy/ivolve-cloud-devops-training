FROM python:3.15.0a3-slim-bookworm

WORKDIR /app

COPY hello.py .

ENV APP_MODE=production APP_REGION=canada-west

COPY Requirements.txt .

RUN pip install -r Requirements.txt

EXPOSE 5000

CMD ["python", "hello.py"]


