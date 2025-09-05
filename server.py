# server.py
from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def run_bot():
    os.system("python3 -m AnnieXMusic")

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()
