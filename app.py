from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    verify_token = "medict"
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == verify_token:
        return challenge
    return "Invalid verify token", 403

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Webhook nhận được:", data)
    return "ok", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
