#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor2 = [float(input(f"Digite o {i+1}º número inteiro: ")) for i in range(10)]

print("Os números reais inseridos na ordem inversa são:", end=" ")
for numero in reversed(vetor2):
    print(numero, end=" ")