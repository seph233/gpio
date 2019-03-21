from flask import Flask
import RPi.GPIO as GPIO #import the GPIO library
import datetime
from time import sleep

app = Flask(__name__)

def logmsg(message):
    print(message)
    with open("logfile", "a") as f:
        f.write(str(datetime.datetime.now()) + " - " + message)

@app.route("/getgpiostatus/<pin>")
def getgpiostatus(pin):
    response = GPIO.input(int(pin))

    if response:
      result = "1"
    elif response == False:
      result = "0"
    else:
      result = "unknown"

    #logmsg("gpio status for pin " + pin + ": " + result + "\n")
    return result

def setup_app():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

setup_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12002)
    while(1==1):
        print(getgpiostatus("11"))
        sleep(2)
