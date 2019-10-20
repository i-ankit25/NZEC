from flask import Flask, render_template, Response, request, jsonify

import os

app = Flask(__name__)

locations = []

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

  
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
    return jsonify("text", "got it")

def toggleRunMode():
    file = open('../mode.txt', 'r')
    s = file.read()
    file.close()
    print(s)
    print(type(s))
    if s != 'human':
        # print('here')
        file = open('../mode.txt', 'w')
        file.truncate(0)
        file.write('human')
    else:
        # print('there')
        file = open('../mode.txt', 'w')
        file.truncate(0)
        file.write('model')

    file.close()

@app.route('/audio', methods=['GET'])
def getaudio():
    file = open('../audio.txt', 'r')
    lines = file.readlines()
    return jsonify(lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
