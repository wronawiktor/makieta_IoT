
from flask import Flask, render_template, request, url_for, redirect
import RPi.GPIO as GPIO
app = Flask(__name__)
import sys
sys.path.insert(1, '/home/pi/makieta_IoT')
from relays import relay_control
from led import led_control
from lcd import drivers

R1 = 26
R2 = 19
Red = 5
Grn = 6

@app.route("/", methods=['GET', 'POST'])
def main():
   # Read GPIO Status
   R1_Sts = GPIO.input(R1)
   R2_Sts = GPIO.input(R2)
   Red_Sts = GPIO.input(Red)
   Grn_Sts = GPIO.input(Grn)

# First html, second python
   templateData = {
      'Relay_1': R1_Sts,
      'Relay_2': R2_Sts,
      'ledRed': Red_Sts,
      'ledGrn': Grn_Sts,
   }
   return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
   if deviceName == 'Relay_1':
      relay = R1
      led = Red
   if deviceName == 'Relay_2':
      relay = R2
      led = Grn

   if action == "on":
      relay_control.on(relay)
      led_control.on(led)
   if action == "off":
      relay_control.off(relay)
      led_control.off(led)

   R1_Sts = GPIO.input(R1)
   R2_Sts = GPIO.input(R2)
   Red_Sts = GPIO.input(Red)
   Grn_Sts = GPIO.input(Grn)

   templateData = {
      'Relay_1': R1_Sts,
      'Relay_2': R2_Sts,
      'ledRed': Red_Sts,
      'ledGrn': Grn_Sts,
   }
   return render_template('index.html', **templateData)

@app.route("/display/<Line1>/<Line2>")
def display(Line1, Line2):
   display = drivers.Lcd()
   display.lcd_clear()
   '''
   Line1="No data"
   if Line1 in request.form:
      Line1 = request.form["Line1"]
   '''
   display.lcd_display_string("{}".format(Line1), 1)
   display.lcd_display_string("{}".format(Line2), 2)

   return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
