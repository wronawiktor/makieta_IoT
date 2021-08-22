# Copyright (c) 2021 Wiktor Wrona Company
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
File to control the relay depending on the temperature
"""

from lcd import drivers
import os
from led import led_control
from relays import relay_control
from sensors import DHT11_simple
from time import sleep
import RPi.GPIO as GPIO

# Choose unit
while True:
    try:
        unit = int(input("Enter unit used in program: 1. Celcius, 2. Farenheit :"))
        if unit not in range(1, 3):
            raise IndexError
        else:
            if unit == 1:
                unit = "Celcius"
                break
            elif unit == 2:
                unit = "Farenheit"
                break

    except ValueError:
        print("Please enter number!")
    except IndexError:
        print("Please enter a number within the range! ")

print("Unit set to {}".format(unit))
sleep(0.5)
os.system('clear')

# Enter max temperature
while True:
    try:
        T_max = input("Enter max temperature in {} degrees : ".format(unit))
        if len(T_max) == 0:
            print("Please enter something")
            continue
        else:
            break

    except ValueError:
        print("Enter correct number!")

print("Max temperature set to {}".format(T_max))
sleep(0.5)
os.system('clear')

# Enter min temperature
while True:
    try:
        T_min = input("Enter minimal temperature in {} degrees : ".format(unit))
        if T_min >= T_max:
            print("Minimal temperature cannot be higher or equal to max temperature!")
            print("Please enter temperature lower than: {} {} degrees.".format(T_max, unit))
            continue
        else:
            break

    except ValueError:
        print("Please enter number!")

print("Min temperature set to {}".format(T_min))
sleep(0.5)
os.system('clear')

# Config
D1 = 6
R1 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
display = drivers.Lcd()


if __name__ == '__main__':
    try:
        while True:

            if unit == "Celcius":
                temperature = DHT11_simple.temp("C")
            elif unit == "Farenheit":
                temperature = DHT11_simple.temp("F")

            display.lcd_display_string("Temp = {}".format(temperature), 1)

            if temperature <= T_min:
                led_control.on(D1)
                relay_control.on(R1)
                display.lcd_display_string("Relay = ON", 2)

            elif temperature >= T_max:
                led_control.off(D1)
                relay_control.off(R1)
                display.lcd_display_string("Relay = OFF", 2)

            else:
                led_control.off(D1)
                relay_control.off(R1)
                display.lcd_display_string("Relay = OFF", 2)

            sleep(2)

    except KeyboardInterrupt:
        print("Exiting")
        display.lcd_clear()
        GPIO.cleanup()
        sys.exit(0)