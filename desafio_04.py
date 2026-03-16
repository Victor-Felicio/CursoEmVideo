valor = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(valor))

print("Só tem espaços?", valor.isspace())
print("É um número?", valor.isnumeric())
print("É decimal?", valor.isdecimal())
print("É dígito?", valor.isdigit())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Está capitalizada?", valor.istitle())
