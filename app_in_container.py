from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json.get("message")
    res = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": data,
            "stream": False
        }
    ).json()

    return jsonify({"reply": res["response"]})
