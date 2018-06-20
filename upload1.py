import os
import time
from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_from_directory


UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = os.urandom(24)


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    try:
        if request.method == 'POST':
            files = request.files.getlist("file")

            PATHS = []

            for _f in files:
                FilePath = secure_filename(str( int( time.time() ) ) + "_" + _f.filename )
                _f.save(os.path.join(app.config['UPLOAD_FOLDER'],FilePath ))
                PATHS.append(os.path.join(app.config['UPLOAD_FOLDER'], _f.filename))
            return jsonify( {"status": True , "data":PATHS , "message": "Uploaded Successully" } )


    except Exception as e:
        print(e)
        return jsonify({"status": False, "message": "Upload Failed"})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

#
# if __name__ == '__main__':
#     app.run('0.0.0.0', 80)
#     #'0.0.0.0', 80