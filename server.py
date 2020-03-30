from flask import Flask, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/on/<int:pin>')
def getOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    state = GPIO.input(pin)
    GPIO.output(pin,GPIO.HIGH)
    return jsonify({'status':'HIGH', 'pin_no':pin})

@app.route('/off/<int:pin>')
def getOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    state = GPIO.input(pin)
    GPIO.output(pin,GPIO.LOW)
    return jsonify({'status':'LOW', 'pin_no':pin})


@app.route('/status/<int:pin>')
def getStatus(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    state = GPIO.input(pin)
    
    if state == 0:
        GPIO.output(pin,GPIO.HIGH)
        return jsonify({'status':'LOW', 'pin_no':pin})
    
    else:
        GPIO.output(pin,GPIO.LOW)
        return jsonify({'status':'HIGH', 'pin_no':pin})

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)

