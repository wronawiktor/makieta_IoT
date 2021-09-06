
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
import sys
sys.path.insert(1, '/home/pi/makieta_IoT/relays')
import relay_control

relays = {
   26: {"name": "Relay 1", "state": "off"},
   19: {"name": "Relay 2", "state": "off"}
   }

for rel in relays:
   relay_control.off(rel)


@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for relay in relays:
      if relays[relay]['state'] == "on":
         relay_control.on(relay)
      else:
         relay_control.off(relay)

   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'relays' : relays
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   global relays
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      relay_control.on(changePin)
      relays[changePin]['state'] = "on"

   if action == "off":
      relay_control.off(changePin)
      relays[changePin]['state'] = "off"

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'relays' : relays
   }

   return render_template('main.html', **templateData)
   #return redirect(url_for('main', **templateData))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
