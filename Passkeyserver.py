from flask import Flask, request, jsonify

app = Flask(__name__)

license_keys = {"VALID-KEY-123": True, "VALID-KEY-456": True}

@app.route('/validate_key', methods=['GET'])
def validate_key():
    key = request.args.get('license_key')
    if license_keys.get(key, False):
        return jsonify({"status": "valid"}), 200
    return jsonify({"status": "invalid"}), 403

@app.route('/deactivate_key', methods=['POST'])
def deactivate_key():
    data = request.json
    key = data.get('license_key')
    if key in license_keys:
        license_keys[key] = False
        return jsonify({"status": "deactivated"}), 200
    return jsonify({"status": "key not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)