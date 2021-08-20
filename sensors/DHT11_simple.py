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
# https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

import Adafruit_DHT

# Initial the dht device, with data pin connected to:
sensor = Adafruit_DHT.DHT11
PIN = 13
humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)


def reading(unit="C"):
    if unit == "C":
        return(temperature, humidity)
    elif unit == "F":
        return(temperature * (9 / 5) + 32, humidity)
    else:
        return(print("Unknown unit"))


def humid():
    return(humidity)


def temp(unit="C"):
    if unit == "C":
        return(temperature)
    elif unit == "F":
        return(temperature * (9 / 5) + 32)
    else:
        return(print("Unknown unit"))
