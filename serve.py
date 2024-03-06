from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

# Initialize S3 client
s3 = boto3.client('s3', region_name='us-east-1') # or your preferred region

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    file_path = '/path/to/save/image/' + file.filename
    file.save(file_path)

    # Upload file to S3
    bucket_name = 'your-bucket-name'
    s3.upload_file(file_path, bucket_name, file.filename)

    # Delete the local file
    os.remove(file_path)

    result = call_ml_model(file.filename)

    return jsonify({'message': 'File uploaded successfully', 'result': result}), 200

def call_ml_model(file_name):
    return 'ML model response'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
