salario = float(input("Digite o salário do funcionário: R$"))

aumento = salario * 0.15
salario_final = salario + aumento

print("O funcionário deixará de receber R${:.2f}, para receber R${:.2f}.".format(salario, salario_final))
