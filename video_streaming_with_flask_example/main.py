from flask import Flask, render_template, Response
from camera import VideoCamera
import cv2 as cv

import socket

addr_stream = ("127.0.0.1", 3000)
addr_model = ("127.0.0.1", 7000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buff = 512

app = Flask(__name__)

cap = cv.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        _, frame = cap.read()
        # frame is sending as a string
        data = frame.tostring()

        ret, jpeg = cv.imencode(".jpg", frame)
        img = jpeg.tobytes()

        for i in range(0, len(data), buff):
            # send chunks to model and stream
            s.sendto(data[i : i + buff], addr_model)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)