from flask import Flask, render_template, Response, request, jsonify
from camera import VideoCamera

import os

app = Flask(__name__)

locations = []

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/location', methods=['GET'])
def getlocations():
    return jsonify(locations)

@app.route('/location', methods=['POST'])
def postlocations():
    if not request.json:
        return
    loc = {
        "lat": request.json['lat'],
        "lon": request.json['lon']
    }

    locations.append(loc)
    print(locations)
    return jsonify("text", "got it")

@app.route('/search', methods=['POST'])
def postsearch():
    if not request.json:
        return
    s = request.json['text']
    print(s)
    keys = s.split(' ')
    for key in keys:
        if CLASSES.__contains__(key):
            print('writing', key, 'to file')
            file = open('../search.txt', 'r+')
            file.truncate(0)
            file.write(key)
            break
    return jsonify("text", "got it")

@app.route('/toggle', methods=['POST'])
def togglemode():
    toggleRunMode()
    return jsonify("var", os.environ['CURRENT'])

def toggleRunMode():
    if os.environ['CURRENT'] == '1':
        os.environ['CURRENT'] = '0'
    else:
        os.environ['CURRENT'] = '1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
