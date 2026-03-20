import math

ang = float(input("Digite o angulo: "))

rad = math.radians(ang)

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f"O seno é: {seno:.2f}")
print(f"O cosseno é: {cosseno:.2f}")
print(f"A tangente é : {tangente:.2f}")
