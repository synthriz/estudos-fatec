#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetor3 = []
def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return caractere in consoantes #true ou false

for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ")
    vetor3.append(caractere)

contadorConsoantes = 0
print("Consoantes lidas:")
for caractere in vetor3:
    if eh_consoante(caractere): #verifica todos os caracteres
        contadorConsoantes += 1
        print(caractere, end=" ")

print(f"\n Total de consoantes lidas:", contadorConsoantes)