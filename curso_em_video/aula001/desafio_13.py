salario = float(input("Digite o salário do funcionário: R$"))

aumento = salario + (salario * 15 / 100)

print("O funcionário deixará de receber R${:.2f}, para receber R${:.2f} com 15% de aumento.".format(salario, aumento))
