import os

os.system("cls")

print("Atividade Salário do Professor")
print("------------------------------")

# 1 Entrada
nivel_professor = int(input("Digite o nivel do professor: "))
qtd_de_aulas = int(input("Digite a Quantidade de aulas por semana: "))

# 2 Processamento / Saida
if nivel_professor == 1:
    salario = qtd_de_aulas * 12

elif nivel_professor == 2:
    salario = qtd_de_aulas * 17

elif nivel_professor == 3:
    salario = qtd_de_aulas * 25

else:
    print("O nivel digitado é inválido")

input("Pressione <ENTER> para continuar...")