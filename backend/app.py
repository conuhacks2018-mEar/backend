"""
"""

import logging
import os
import uuid

from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename

import redis


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
r = redis.Redis(host='redis', decode_responses=True)

os.makedirs('/data', exist_ok=True)
ALLOWED_EXTENSIONS = set(['wav'])

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_wav', methods=['POST'])
def upload_wav():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'no file part'})
    file = request.files['file']

    # make sure file has filename
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'no filename'})

    # make sure filename is correct
    if file and allowed_file(file.filename):
        filename_uuid = str(uuid.uuid4())
        filename = f'/data/{filename_uuid}.wav'
        file.save(filename)
        r.rpush('wav_id', filename_uuid)
        return jsonify({'status': 'ok', 'message': 'uploaded successfully', 'wav_id': filename_uuid})
