import DHT11_simple

print(DHT11_simple.reading(unit="C"))
print(DHT11_simple.humid())
print(DHT11_simple.temp("C"))
print(DHT11_simple.temp("F"))

