from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Ubah dengan URL masing-masing service yang ter-deploy di Cloud Run
AUTHFITUR_SERVICE_URL = "https://be-budaya-592544960467.asia-southeast2.run.app"
PREDICTION_SERVICE_URL = "https://prediksi-budaya-592544960467.asia-southeast2.run.app"
# Endpoint untuk mengirim OTP
@app.route('/send-otp', methods=['POST'])
def send_otp():
    try:
        response = requests.post(f"{AUTHFITUR_SERVICE_URL}/send-otp", json=request.get_json())
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk verifikasi OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    try:
        response = requests.post(f"{AUTHFITUR_SERVICE_URL}/verify-otp", json=request.get_json())
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk login
@app.route('/login', methods=['POST'])
def login():
    try:
        response = requests.post(f"{AUTHFITUR_SERVICE_URL}/login", json=request.get_json())
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk memproses gambar dan mendapatkan prediksi
@app.route('/predict-image', methods=['POST'])
def predict_image():
    try:
        response = requests.post(f"{PREDICTION_SERVICE_URL}/predict-image", files=request.files, data=request.form)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mendapatkan riwayat prediksi
@app.route('/prediction-history', methods=['GET'])
def prediction_history():
    try:
        user_id = request.args.get('user_id')
        response = requests.get(f"{PREDICTION_SERVICE_URL}/prediction-history", params={"user_id": user_id})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mendapatkan semua data budaya
@app.route('/getall_budaya', methods=['GET'])
def get_all_budaya():
    try:
        response = requests.get(f"{AUTHFITUR_SERVICE_URL}/getall_budaya")
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mendapatkan detail dari budaya berdasarkan file_name
@app.route('/details', methods=['GET'])
def get_details():
    try:
        file_name = request.args.get('file_name', '')
        if not file_name:
            return jsonify({"error": "Parameter 'file_name' is required"}), 400

        response = requests.get(f"{AUTHFITUR_SERVICE_URL}/details", params={"file_name": file_name})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Menjalankan aplikasi pada port yang ditentukan (default 8080)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  
    app.run(host="0.0.0.0", port=port)