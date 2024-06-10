#Faça um programa para imprimir:
#1
#1 2
#1 2 3
#.....
#1 2 3 ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
n1 = int(input("Insira um numero: "))
def exercicio2(n1):
    for i in range(1, n1 + 1): #loop externo que contabiliza todos os numeros, ate n (incluido por n1+1)
        for j in range(1, i + 1): #loop interno que imprime a sequencia para cada valor de i (incluido por i+1)
            print(j, end=" ") #end para ajeitar a formatação padrão de quebra de linha de print()
        print() #quebra de linha

exercicio2(n1)