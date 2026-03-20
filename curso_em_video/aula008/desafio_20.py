import random

n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print("Ordem de apresentação dos alunos: ")
for i, n in enumerate(lista, start = 1):
    print(f"{i}º - {n}")
