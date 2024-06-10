#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").lower() #.lower pra nao ter distinção entre maiusculas/minusculas
    while resposta not in ['sim', 'não']: #catch error da resposta
        resposta = input("Por favor, responda apenas com 'sim' ou 'não': ").lower()
    respostas.append(resposta)

# contagem dos sim
contador_positivas = respostas.count("sim")

if contador_positivas == 2:
    print("Suspeita")
elif 3 <= contador_positivas <= 4:
    print("Cúmplice")
elif contador_positivas == 5:
    print("Assassino")
else:
    print("Inocente")