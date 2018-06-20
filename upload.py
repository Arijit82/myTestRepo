from datetime import datetime
import os
from flask import Flask, request, session, render_template, send_file
from werkzeug import secure_filename
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from io import BytesIO

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)
client = MongoClient('localhost')
db = client.app     #database
files = db.files   #objects in database

@app.route('/upload', methods=["GET"])
def upload_file():
    return render_template('uploads.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files: #no images uploaded
            f = request.files['file']
            f.save(secure_filename(f.filename))
            db.files.insert_one({"file": str(f)})
            return jsonify({'status': True, 'message': 'File Uploaded Successfully.....!!'})
        return  jsonify({'status': False, 'message': 'File Upload Failed.....!!'})

@app.route('/getupload', methods=['GET', 'POST'])
def getupload():#mimetypes
    file_data= db.files.find_one({})
    return send_file(BytesIO(file_data.data),attachment_filename='arijit.jpg', as_attachment=True)

if __name__ == '__main__':
   app.run('localhost',5000)