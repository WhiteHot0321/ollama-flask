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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
