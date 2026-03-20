from math import hypot

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hypotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"O comprimeito da hipotenusa é: {hypotenusa:.2f}")
