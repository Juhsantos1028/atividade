import os

os.system("cls")

print("Calcule o desconto")
print("------------------")

#1 Entrada
descricao_produto = input("Digite o nome do produto: ")
quantidade_produto = input("Digite a quantidade: ")
preco = float(input("Digite o preço: "))

#2 Processamento 
total = quantidade_produto * preco

#3 Saida
if quantidade_produto <=5:
    desconto = total * 0.02
    total_com_desconto = total - desconto 
    print("O seu desconto foi: ",total_com_desconto)

elif quantidade_produto >5 and quantidade_produto <= 10:
    desconto = total * 0.03
    total_com_desconto = total - desconto 
    print("O total sera: ",total_com_desconto)

elif quantidade_produto >10:
    desconto = total * 0.05
    total_com_desconto = total - desconto
    print("O total sera: ", total_com_desconto)