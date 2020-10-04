import random
import time

ladodeabajo = "Cara"
ladodearriba = "Cruz"


# explicacion
print("juego de la moneda")
print()
time.sleep(2)
print('para jugar el juego de la moneda se necesitan dos jugadores el sistema lansara una moneda y aleatoriamente eligira entre "Cara" o "Cruz"')
print('eligan de que lado van cara o cruz')
print()
print('la moneda se lansara en 5 segundos')
time.sleep(5)

# proseso de lansado de moneda

print('a salido ' + random.choice((ladodeabajo, ladodearriba)))