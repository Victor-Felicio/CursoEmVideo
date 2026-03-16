lar = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = lar * alt
tin = area / 2

print("São necessários {} litros de tinta, para pintar uma parede de {} m².".format(tin, area))
