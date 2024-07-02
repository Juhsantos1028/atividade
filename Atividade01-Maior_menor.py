import os

os.system("cls")

print("Maior e Menor")
print("-------------")


#1 Passo - Entrada
valor01 = int(input("Digite o primero valor: "))
valor02 = int(input("Digite o segundo valor: "))


#2 Passo - Processamento / saida
if valor01 > valor02:
    print("O maior valor é: ", valor01, "e menor é: ", valor02)

elif valor02 > valor01:
    print("O maior valor é: ", valor02, "e menor é: ", valor01)

else:
    print("Os valores são iguais")

input("Pressione <ENTER> para continuar...")