#Faça um programa para imprimir:
#1
#2 2
#3 3 3
#.....
#n n n n n n ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
n = int(input("Insira um numero: "))

def exercicio1(n):
    for i in range(1, n + 1): #loop para o intervalo de 1 ate n (incluido por n+1)
        print(*([str(i)] * i)) #transforma o input numerico em string para imprimir a lista

exercicio1(n)