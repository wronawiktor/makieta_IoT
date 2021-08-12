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

#Pobranie biblioteki do sterowania GPIO
import RPi.GPIO as GPIO
import time

#Definiujemy PIN GPIO do ktorego podlaczona jest dioda
PIN = 5

print("Enable LED connected to PIN ", PIN)

#Uzywamy numeracji GPIO, a nie fizycznych pinow
GPIO.setmode(GPIO.BCM)

#Wylaczenie ostrzezen, ktore moglby pojawic sie przy ponownym otwieraniu pliku bez czyszczenia GPIO
GPIO.setwarnings(False)

GPIO.setup(PIN, GPIO.OUT)

#Podajemy stan wysoki na wczesniej zdefiniowany pin
GPIO.output(PIN, GPIO.HIGH)

time.sleep(10)

GPIO.cleanup(PIN)
