pre = float(input("Digite o preço do produto: R$"))
desc = pre - (pre * 5 / 100)

print("O produto vale R${:.2f}, e será cobrado R${:.2f} com 5% de desconto.".format(pre, desc))
