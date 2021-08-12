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
"""
Plik do migania diodą podłączoną do wybranego GPIO
"""
# Pobranie biblioteki do sterowania GPIO oraz sys
import RPi.GPIO as GPIO
import sys
import time

# Używamy numeracji GPIO, a nie fizycznych pinów
GPIO.setmode(GPIO.BCM)
# Wyłączenie ostrzeżeń, które mogłby pojawić się przy ponownym otwieraniu pliku bez czyszczenia GPIO
GPIO.setwarnings(False)
# Definiujemy pod, który GPIO podłączona jest dioda

while True:
    try:
        PIN = input("Podaj port GPIO pod który podłączona jest dioda (domyślnie: 6): ")
        if len(PIN) == 0:
            PIN = 6
            break
        else:
            PIN = int(PIN)
            break
    except ValueError:
        print("Podaj poprawną liczbę!")
    else:
        break




# Użycie u jako wyjściowy
GPIO.setup(PIN, GPIO.OUT)
# Podajemy okres jednego mignięcia zgodnie z preferencją użytkownika

while True:
    try:
        okres = float(input("Podaj okres jednego mignięcia (w sekundach): "))
    except ValueError:
        print("Podaj poprawną liczbę!")
        continue
    else:
        break

print("Aby zakończyć działanie programu, naciśnij Ctrl + C")

while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(okres / 2)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(okres / 2)

GPIO.cleanup()
sys.exit(0)
