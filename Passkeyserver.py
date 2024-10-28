from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Dictionary of valid license keys
license_keys = {"VALID-KEY-123": True, "VALID-KEY-456": True}

# Root route for a simple home page
@app.route("/")
def home():
    return "Welcome to the Passkey Server!"

# Route to validate a license key
@app.route('/validate_key', methods=['GET'])
def validate_key():
    key = request.args.get('license_key')
    if license_keys.get(key, False):
        return jsonify({"status": "valid"}), 200
    return jsonify({"status": "invalid"}), 403

# Route to deactivate a license key
@app.route('/deactivate_key', methods=['POST'])
def deactivate_key():
    data = request.json
    key = data.get('license_key')
    if key in license_keys:
        license_keys[key] = False
        return jsonify({"status": "deactivated"}), 200
    return jsonify({"status": "key not found"}), 404

# Set the server to listen on all interfaces and the correct port for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
