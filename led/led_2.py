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
Plik do sterowania diodą podłączoną do wybranego GPIO
"""
# Pobranie biblioteki do sterowania GPIO oraz sys
import RPi.GPIO as GPIO
import sys

# Używamy numeracji GPIO, a nie fizycznych pinów
GPIO.setmode(GPIO.BCM)
# Wyłączenie ostrzeżeń, które mogłby pojawić się przy ponownym otwieraniu pliku bez czyszczenia GPIO
GPIO.setwarnings(False)
# Definiujemy pod, który GPIO podłączona jest dioda
PIN = int(input("Podaj port GPIO pod który podłączona jest dioda (domyślnie: 5): "))
# Użycie u jako wyjściowy
GPIO.setup(PIN, GPIO.OUT)
# Podajemy zgodnie z preferencją użytkownika na wcześniej zdefiniowany PIN
print("""
Wybierz czynność:
- Y - Włącz diodę
- N - Wyłącz diodę
- Q - Wyjdź z programu
""")
while True:
    print()
    operacja = input("Czynność: ")
    if operacja in ["Y", "y"]:
        GPIO.output(PIN, GPIO.HIGH)
        continue
    elif operacja in ["N", "n"]:
        GPIO.output(PIN, GPIO.LOW)
        continue
    elif operacja in ["Q", "q"]:
        GPIO.cleanup()
        break
    else:
        input("Błędna komenda! Wybierz jeszcze raz! (Naciśnij, aby kontynuować): ")
        # Czekaj na reakcję użytkownika
        continue
sys.exit(0)
