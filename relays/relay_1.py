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
import relay_control
from led import led_control
import os


def import_pin_num(relay, default_pin):
    while True:
        try:
            pin = input("Podaj port GPIO pod który podłączony jest przekaźnik nr {} (domyślnie: {}): ".format(relay, default_pin))
            if len(pin) == 0:
                pin = default_pin
                break
            else:
                pin = int(pin)
                break
        except ValueError:
            print("Podaj poprawną liczbę!")
    return(pin)


# Pin definition of where relays, switches and diodes are connected
R1 = import_pin_num(1, 26)
R2 = import_pin_num(2, 19)
S1 = 21
S2 = 20
D1 = 6
D2 = 5

while True:
    while (GPIO.input(S1) == GPIO.LOW and GPIO.input(S2) == GPIO.LOW):
        os.system('cls')
        print("""
        ================
        Menu
        1. Włącz przekaźnik nr. 1
        2. Wyłącz przekaźnik nr. 1
        3. Włącz przekaźnik nr. 2
        4. Wyłącz przekaźnik nr. 2
        ================""")
        while True:
            try:
                action = int(input("Akcja: "))
                if action not in range(1, 5):
                    raise IndexError
                else:
                    break
            except ValueError:
                print("Podaj poprawną liczbę! ")
            except IndexError:
                print("Podaj liczbę mieszczącą się w zakresie! ")

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
            led_control.on(D2)

        os.system('cls')
        print("Akcja nr:{} przeprowadzona pomyślnie! ".format(action))
        input("Nacisnij, aby kontynuować")

    if GPIO.input(S1) == GPIO.HIGH:
        os.system('cls')
        print("Alarm przekaźnika 1")
        relay_control.off(R1)
        led_control.blink(D1, 1)
        GPIO.wait_for_edge(S1, GPIO.RISING)

    elif GPIO.input(S2) == GPIO.HIGH:
        os.system('cls')
        print("Alarm przekaźnika 2")
        relay_control.off(R1)
        led_control.blink(D1, 1)
        GPIO.wait_for_edge(S2, GPIO.RISING)
