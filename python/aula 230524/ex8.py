#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e 
# depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

while True:
    nomeAtleta = input("Digite o nome do atleta (ou deixe em branco para encerrar): ")
    if nomeAtleta == "":
        break

    saltos = []
    for i in range(1, 6):
        salto = float(input(f"Digite a distância alcançada no {i}º salto (em metros): "))
        saltos.append(salto)

    mediaSaltos = sum(saltos) / len(saltos)

    print("* Atleta:", nomeAtleta)
    print("* Detalhes dos saltos:")
    print("Primeiro Salto:", saltos[0], "m")
    print("Segundo Salto:", saltos[1], "m")
    print("Terceiro Salto:", saltos[2], "m")
    print("Quarto Salto:", saltos[3], "m")
    print("Quinto Salto:", saltos[4], "m")
    print("\n* Resultado final:")
    print("* Saltos:", " - ".join(map(str, saltos)), "(em metros)")
    print(f"* Média dos saltos: {mediaSaltos:.1f} m\n") #.1f para colocar apenas uma casa apos a virgula