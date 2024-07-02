import os

os.system("cls")

print("calculadora simples")
print("--------------------")

#1 Passo - Entrada
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

#2 Passo - Processamento / saida
operacao = int(input("Digite 2 para somar /n" "Digite 3 para subtrair /n" "Digite 4 para dividir /n" "Digite 5 para multiplicar /n"))

if operacao == 2:
    resultado = (n1 + n2)
    print("O resultado da Soma: ", resultado)

elif operacao == 3:
    resultado = (n1 - n2)
    print("O resultado da Subtração: ", resultado)

elif operacao == 4:
    resultado = (n1 / n2)
    print("O resultado da Divisão: ", resultado)

elif operacao == 5:
    resultado = (n1 * n2)
    print("O resultado da Multplicação: ", resultado)

else:
    print("Operação invalida")


input("Pressione <ENTER> para continuar...")