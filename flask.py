from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"]}})

@app.route("/uploadCTSACN", methods=["POST"])
def upload():
    try:
        file = request.files['file']

        # Process the file (you can implement your machine learning code here)
        # For now, we'll just return a success message
        return jsonify({"result": "Image uploaded successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(port=8080, debug=True, use_reloader=True)
