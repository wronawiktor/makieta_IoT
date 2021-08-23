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

import Adafruit_DHT
import os
import sys
import RPi.GPIO as GPIO
from led import led_control
from lcd import drivers
from relays import relay_control
from time import sleep


# Config
D1 = 6
R1 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
display = drivers.Lcd()


if __name__ == '__main__':

    def choose_unit():
        global unit
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
        sleep(1)
        os.system('clear')
        return unit


    def max_temp():
        global T_max
        # Enter max temperature
        while True:
            try:
                T_max = int(input("Enter max temperature in {} degrees : ".format(unit)))
                break

            except ValueError:
                print("Enter correct number!")

        print("Max temperature set to {}".format(T_max))
        sleep(1)
        os.system('clear')
        return T_max


    def min_temp():
        global T_min
        # Enter min temperature
        while True:
            try:
                T_min = int(input("Enter minimal temperature in {} degrees : ".format(unit)))
                if T_min >= T_max:
                    print("Minimal temperature cannot be higher or equal to max temperature!")
                    print("Please enter temperature lower than: {} {} degrees.".format(T_max, unit))
                    continue
                else:
                    break

            except ValueError:
                print("Please enter number!")

        print("Min temperature set to {}".format(T_min))
        sleep(1)
        os.system('clear')
        return T_min


    unit = choose_unit()
    T_max = max_temp()
    T_min = min_temp()

    print("T_min: {}".format(T_min))
    print("T_max: {}".format(T_max))
    print("Program running...")

    led_control.off(D1)
    relay_control.off(R1)
    display.lcd_display_string("Relay = OFF", 2)

    try:
        while True:

            if unit == "Celcius":
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 13)
                unit_letter = "C"
            elif unit == "Farenheit":
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 13)
                temperature = temperature * (9 / 5) + 32
                unit_letter = "F"

            display.lcd_display_string("Temp = {} {} ".format(temperature, unit_letter), 1)

            if temperature <= T_min:
                led_control.on(D1)
                relay_control.on(R1)
                display.lcd_display_string("Relay = ON ", 2)

            elif temperature >= T_max:
                led_control.off(D1)
                relay_control.off(R1)
                display.lcd_display_string("Relay = OFF", 2)

            sleep(2)

    except KeyboardInterrupt:
        print("Exiting")
        display.lcd_clear()
        GPIO.cleanup()
        sys.exit(0)
