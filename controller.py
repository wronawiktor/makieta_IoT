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

import multiprocessing
import os
import sys
import time

import RPi.GPIO as GPIO

from relays import led_control
from led import relay_control
from relays import led_control


# Pin definition of where relays, switches and diodes are connected
R1 = import_pin_num(1, 26)
R2 = import_pin_num(2, 19)
S1 = 21
S2 = 20
D1 = 6
D2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(S1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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


def my_callback_one(S1):
    button_pressed = False

    global button_pressed
    button_pressed = not button_pressed
    if button_pressed:
        global blink1
        os.system('clear')
        print("Relay 1 alarm")
        relay_control.off(R1)
        GPIO.cleanup(R1)
        blink1 = multiprocessing.Process(target=led_control.blink, args=(D1, 0.5))
        blink1.daemon = True
        blink1.start()
    else:
        os.system('clear')
        blink1.terminate()
        GPIO.cleanup(D1)
        print("Relay 1 alarm - disabled")
    time.sleep(0.01)


def my_callback_two(S2):
    button_pressed_2 = False
    
    global button_pressed_2
    button_pressed_2 = not button_pressed_2
    if button_pressed_2:
        global blink2
        os.system('clear')
        print("Relay 2 alarm")
        relay_control.off(R2)
        GPIO.cleanup(R2)
        blink2 = multiprocessing.Process(target=led_control.blink, args=(D2, 0.5))
        blink2.daemon = True
        blink2.start()
    else:
        os.system('clear')
        blink2.terminate()
        GPIO.cleanup(D2)
        print("Relay 2 alarm - disabled")
    time.sleep(0.01)


GPIO.add_event_detect(S1, GPIO.RISING, callback=my_callback_one, bouncetime=800)
GPIO.add_event_detect(S2, GPIO.RISING, callback=my_callback_two, bouncetime=800)


if __name__ == '__main__':
    
    while True:
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
            if not button_pressed:
                relay_control.on(R1)
                led_control.on(D1)
            else:
                print("Cannot turn on relay! Lock is on. Press S1 to unlock.")
        elif action == 2:
            relay_control.off(R1)
            led_control.off(D1)
        elif action == 3:
            if not button_pressed_2:
                relay_control.on(R2)
                led_control.on(D2)
            else:
                print("Cannot turn on relay! Lock is on. Press S2 to unlock.")
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

        # print("Action no.:{} carried out successfully! ".format(action))
        input("Press, to continue\n")
        os.system('clear')
