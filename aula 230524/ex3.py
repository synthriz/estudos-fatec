#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []

for i in range(4):
  nota = float(input(f"Digite a {1+i}º nota: "))
  notas.append(nota)

media = sum(notas)/len(notas)

print("As notas digitadas são: ", notas)
print("A média é: ", media)