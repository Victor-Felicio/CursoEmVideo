#Aluguel de carros

d = int(input("Dias alugados: "))
k = float(input("Quantos Km: "))
p = (d * 60) + (k * 0.15)

print(f"O total a pagar é de R${p:.2f}")
