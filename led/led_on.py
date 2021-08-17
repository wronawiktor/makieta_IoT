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


def on(pin):
    # Use of GPIO numbering, not physical pins
    GPIO.setmode(GPIO.BCM)

    # Disabling warnings
    GPIO.setwarnings(False)

    # Set GPIO PIN as output
    GPIO.setup(pin, GPIO.OUT)

    # High state to the pin
    GPIO.output(pin, GPIO.HIGH)
