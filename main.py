from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
# CORS(app, origins=["http://lsv03244.swis.in-blr01.nxp.com:4001", "http://127.0.0.1:5500/"], supports_credentials=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'result': 'No file part'})

    file = request.files['file']

    # Perform your machine learning code here
    # For demonstration, let's assume it's a placeholder function
    result = process_file(file)

    return jsonify({'result': result})

def process_file(file):
    # Placeholder function for processing the file
    # Replace this with your actual machine learning code
    return 'Processed: ' + file.filename



if __name__ == "__main__":
    app.run(port=8080, debug=True, use_reloader=True)