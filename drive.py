#imports all relevant libraries
import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

#socketio setup
sio = socketio.Server()

#flask app setup
app = Flask(__name__) #'__main__'

#speed limit of simulator
speed_limit = 10

#image processing function
def img_preprocess(img): 
    img = img[60:135, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)#rgb to yuv for nvidia model
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255#normalize
    return img

#telemetry setup for simulator
@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    throttle = 1.0 - speed/speed_limit
    print('{} {} {}'.format(steering_angle, throttle, speed))
    send_control(steering_angle, throttle)

#initial connection
@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0,0)#initial car position

#sending control of angle and throttle to simulator
def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

#generate webserver gateway and apply socketio middleware 
if __name__ == '__main__':
    model = load_model('model.h5')#loads the generated model
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
