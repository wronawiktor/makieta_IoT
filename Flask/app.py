
from flask import Flask, render_template, request, url_for, redirect
import RPi.GPIO as GPIO
import Adafruit_DHT
from camera_pi import Camera
app = Flask(__name__)
import sys
sys.path.insert(1, '/home/pi/makieta_IoT')
from lcd import drivers

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

R1 = 26
R2 = 19
L1 = 5
L2 = 6
B1 = 21
B2 = 20

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(B1, GPIO.IN)
GPIO.setup(B2, GPIO.IN)

R1_Sts = 0
R2_Sts = 0
L1_Sts = 0
L2_Sts = 0
B1_Sts = 0
B2_Sts = 0
temperature_C = 0
temperature_F = 0
humidity = 0
progress_temp = 0

GPIO.output(R1, GPIO.LOW)
GPIO.output(R2, GPIO.LOW)
GPIO.output(L1, GPIO.LOW)
GPIO.output(L2, GPIO.LOW)


def gen(camera):
   """Video streaming generator function."""
   while True:
      frame = camera.get_frame()
      yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/", methods=['GET', 'POST'])
def main():
   # Read GPIO Status
   R1_Sts = GPIO.input(R1)
   R2_Sts = GPIO.input(R2)
   L1_Sts = GPIO.input(L1)
   L2_Sts = GPIO.input(L2)
   B1_Sts = GPIO.input(B1)
   B2_Sts = GPIO.input(B2)

# First html, second python
   templateData = {
      'Relay_1': R1_Sts,
      'Relay_2': R2_Sts,
      'led1': L1_Sts,
      'led2': L2_Sts,
      'temp_c': temperature_C,
      'temp_f': temperature_F,
      'prog_C': progress_temp,
      'hum': humidity,
      'b1': B1_Sts,
      'b2': B2_Sts,
   }

   def gen(camera):
      """Video streaming generator function."""
      while True:
         frame = camera.get_frame()
         yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

   return render_template('main.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
   if deviceName == 'Relay_1':
      relay = R1
      led = L1
   if deviceName == 'Relay_2':
      relay = R2
      led = L2

   if action == "on":
      GPIO.output(relay, GPIO.HIGH)
      GPIO.output(led, GPIO.HIGH)
   if action == "off":
      GPIO.output(relay, GPIO.LOW)
      GPIO.output(led, GPIO.LOW)

#   return render_template('main.html', **templateData)
   return redirect(url_for('main'))


@app.route("/display", methods=['POST'])
def display():
   display = drivers.Lcd()
   display.lcd_clear()

   Line1="No data"
   if "L1" in request.form:
      Line1 = request.form["L1"]
   Line2 = "No data"
   if "L2" in request.form:
      Line2 = request.form["L2"]

   display.lcd_display_string("{}".format(Line1), 1)
   display.lcd_display_string("{}".format(Line2), 2)

   return redirect(url_for('main'))


@app.route("/dht", methods=['POST'])
def dht():
   global humidity
   global temperature_C
   global temperature_F
   global progress_temp

   humidity, temperature_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 13)
   temperature_F = temperature_C * (9 / 5) + 32
   progress_temp = temperature_C * 2

   return redirect(url_for('main'))

@app.route("/disp_clear")
def disp_clear():
   display = drivers.Lcd()
   display.lcd_clear()

   return redirect(url_for('main'))


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
