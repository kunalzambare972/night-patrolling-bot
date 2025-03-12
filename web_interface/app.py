from flask import Flask, render_template, Response, jsonify
import cv2
import threading
from hardware.motor_control import move_forward, stop_motors

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Open webcam

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control/<action>')
def control_robot(action):
    if action == "forward":
        move_forward(60)
        return jsonify({"status": "Moving Forward"})
    elif action == "stop":
        stop_motors()
        return jsonify({"status": "Stopping"})
    return jsonify({"status": "Invalid Action"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
