import os

os.system("cls")

print("Positivo, negativo ou zero")
print("--------------------------")

#1 Passo - Entrada
numero = int(input("Digite um número: "))

#2 Passo - Processamento / saida
if numero > 0:
    print("O Número e positivo")

elif numero < 0:
    print("O Número e negativo")

else:
    print("O Número é ZERO")

input("Pressione <ENTER> para continuar...")      