"""
Plik do włączania diody podłączonej do GPIO
"""
print("hello!")
#Pobranie biblioteki do sterowania GPIO
import RPi.GPIO as GPIO
#Używamy numeracji GPIO, a nie fizycznych pinów
GPIO.setmode(GPIO.BCM)
#Wyłączenie ostrzeżeń, które mogłby pojawić się przy ponownym otwieraniu pliku bez czyszczenia GPIO
GPIO.setwarnings(False)
#Definiujemy pod, który pin GPIO podłączona jest dioda
pin = 5
#Podajemy stan wysoki na wcześniej zdefiniowany pin
GPIO.output(pin, GPIO.HIGH)