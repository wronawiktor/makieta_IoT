# -*- coding: utf-8 -*-
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

import RPi.GPIO as GPIO
import time
import sys
sys.path.insert(1, '/home/pi/makieta_IoT/led')
sys.path.insert(1, '/home/pi/makieta_IoT/relays')
import relay_control
import led_control
import os

def import_pin_num(relay, default_pin):
    while True:
        try:
            pin = input("Enter GPIO port where the relay no.{} is connected (by default: {}): ".format(relay, default_pin))
            if len(pin) == 0:
                pin = default_pin
                break
            else:
                pin = int(pin)
                break
        except ValueError:
            print("Please enter correct number! ")
    return(pin)


# Pin definition of where relays, switches and diodes are connected
R1 = import_pin_num(1, 26)
R2 = import_pin_num(2, 19)
S1 = 21
S2 = 20
D1 = 6
D2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(S1, GPIO.IN)
GPIO.setup(S2, GPIO.IN)

while True:
    while (GPIO.input(S1) == GPIO.LOW and GPIO.input(S2) == GPIO.LOW):
        os.system('clear')
        print("""
        ================
        Menu
        1. Switch on relay no. 1 
        2. Turn off relay no. 1 
        3. Switch on relay no. 2
        4. Turn off relay no. 2
        5. Turn off the program 
        ================""")
        while True:
            try:
                action = int(input("Action: "))
                if action not in range(1, 6):
                    raise IndexError
                else:
                    break
            except ValueError:
                print("Please enter correct number! ")
            except IndexError:
                print("Please enter a number within the range! ")

        if action == 1:
            relay_control.on(R1)
            led_control.on(D1)

        elif action == 2:
            relay_control.off(R1)
            led_control.off(D1)

        elif action == 3:
            relay_control.on(R2)
            led_control.on(D2)

        elif action == 4:
            relay_control.off(R2)
            led_control.off(D2)

        elif action == 5:
            relay_control.off(R1)
            led_control.off(D1)
            relay_control.off(R2)
            led_control.off(D2)
            GPIO.cleanup()
            sys.exit(0)

        os.system('clear')
        print("Action no.:{} carried out successfully! ".format(action))
        input("Press, to continue")

    if GPIO.input(S1) == GPIO.HIGH:
        os.system('clear')
        print("Relay 1 alarm")
        relay_control.off(R1)
        led_control.blink(D1, 1)
        GPIO.wait_for_edge(S1, GPIO.RISING)

    elif GPIO.input(S2) == GPIO.HIGH:
        os.system('clear')
        print("Relay 2 alarm")
        relay_control.off(R1)
        led_control.blink(D1, 1)
        GPIO.wait_for_edge(S2, GPIO.RISING)
