from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask container is running 🚀  Reda Eissawy"

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        container=os.getenv("HOSTNAME", "unknown")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
