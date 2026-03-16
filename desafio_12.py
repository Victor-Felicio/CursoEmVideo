pre = float(input("Digite o preço do produto: R$"))
desc = pre * 0.05

pre_final = pre - desc

print("O produto vale R${:.2f}, e será cobrado R${:.2f} com desconto.".format(pre, pre_final))
