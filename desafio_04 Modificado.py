valor = input("AB3c")

print(len(valor))
print(f"{valor[1]} primeiro caractere.")

if valor.isalnum():
    print(f"{valor} é Alfanumérico!")
    if valor[0].isnumeric():
        print(f"0 {valor[0]} é um número.")
    if valor[1].isnumeric():
        print(f"1 {valor[1]} é um número.")
    if valor[2].isnumeric():
        print(f"A casa 2 é {valor[2]} um número.")
    if valor[3].isnumeric():
        print(f"3 {valor[3]} é um número.")
else:
    print(f"{valor} não é Alfanumérico!")
