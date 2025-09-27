from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

# 🔑 Tu API Key de DeepSeek (guárdala en variable de entorno si puedes)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_KEY", "sk-0f0f942ff2a546e5a05745b2d285a262")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }

    r = requests.post("https://api.deepseek.com/v1/chat/completions",
                      headers=headers, json=payload)

    if r.status_code == 200:
        ai_reply = r.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": ai_reply})
    else:
        return jsonify({"error": r.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
