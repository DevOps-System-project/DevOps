from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"
SERVICE_NAME = "Campus Help Desk"
SUPPORT_EMAIL = "support@example.com"
SERVICE_HOURS = "Mon-Fri 08:00-17:00"


@app.route("/")
def home():
    return f"""
    <h1>{SERVICE_NAME}</h1>
    <p>Support: {SUPPORT_EMAIL}</p>
    <p>Hours: {SERVICE_HOURS}</p>
    <p>Version: {VERSION}</p>
    """


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

