# -*- coding: utf-8 -*-
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

# Definiujemy pod, który pin GPIO podłączona jest dioda
pin = int(input("Podaj port GPIO pod który podłączona jest dioda (domyślnie: 5): "))

# Podajemy zgodnie z preferencją użytkownika na wcześniej zdefiniowany pin
print("""
Wybierz czynność:
- Y - Włącz diodę
- N - Wyłącz diodę
- Q - Wyjdź z programu
""")
while True:
    print()
    operacja = input("Czynność: ")
    if operacja == ("Y" or "y"):
        GPIO.output(pin, GPIO.HIGH)
        continue
    elif operacja == ("N" or "n"):
        GPIO.output(pin, GPIO.LOW)
        continue
    elif operacja == ("Q" or "q"):
        GPIO.cleanup()
        break
    else:
        input("Błędna komenda! Wybierz jeszcze raz! (Naciśnij, aby kontynuować): ")
        # Czekaj na reakcję użytkownika
        continue

sys.exit(0)
