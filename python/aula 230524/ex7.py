#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça:

#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada; 7. 
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

notas2 = []
valor = 0

while True:
    valor = float(input("Digite a nota (-1 para encerrar): "))
    if valor == -1:
        break
    notas2.append(valor)

# 1. qtidade de valores lidos
quantidade = len(notas2)
print("1. Quantidade de valores lidos:", quantidade)

# 2. todos os valores na ordem que foram informados
print("2. Todos os valores na ordem que foram informados:", end=" ")
for nota in notas2:
    print(nota, end=" ")

# 3. todos os valores na ordem inversa
print("\n3. Todos os valores na ordem inversa:")
for nota in reversed(notas2):
    print(nota)

# 4. soma dos valores
soma = sum(notas2)
print("4. Soma dos valores:", soma)

# 5. media dos valores
media = soma / quantidade if quantidade != 0 else 0
print("5. Média dos valores:", media)

# 6. qtidade de valores acima da média
acima_da_media = sum(nota > media for nota in notas2)
print("6. Quantidade de valores acima da média:", acima_da_media)

# 7. qtidade de valores abaixo de sete
abaixo_de_sete = sum(nota < 7 for nota in notas2)
print("7. Quantidade de valores abaixo de sete:", abaixo_de_sete)

# 8. encerramento do programa
print("Programa encerrado.")