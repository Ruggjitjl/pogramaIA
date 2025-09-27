from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Tu API Key de DeepSeek (ponla aquí)
API_KEY = "sk-0f0f942ff2a546e5a05745b2d285a262"
API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        ai_reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": ai_reply})
    else:
        return jsonify({"error": response.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

