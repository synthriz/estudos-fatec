#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre: a. O modelo do carro mais econômico; b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próximo possível ao exemplo.
#Os dados são fictícios e podem mudar a cada execução do programa.

#Comparativo de Consumo de Combustível

#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5
#Relatório Final
#1 - fusca - 7.0 - 142.9 litros - R$ 321.43
#2 - gol - 10.0 - 100.0 litros - R$ 225.00
#3 - uno - 12.5 - 80.0 litros - R$ 180.00
#4 - vectra - 9.0 - 111.1 litros - R$ 250.00
#5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
#O menor consumo é do peugeout

modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeot"]

# consumo em km/L
consumo = [7, 10, 12.5, 9, 14.5]

preco_gasolina_litro = 2.25
distancia = 1000
consumo_total = []
custo_total = []

# calculo p percorrer 1000km e o custo
for i in range(len(modelos)):
    consumo_carro = distancia / consumo[i]
    custo_carro = consumo_carro * preco_gasolina_litro
    consumo_total.append(consumo_carro)
    custo_total.append(custo_carro)

# encontra o modelo mais economico pelo metodo index() que busca o menor numero de consumo total
indice_mais_economico = consumo_total.index(min(consumo_total))

print("Comparativo de Consumo de Combustível")
for i in range(len(modelos)):
    print(f"* Veículo {i+1}")
    print(f"  * Nome: {modelos[i]}")
    print(f"  * Km por litro: {consumo[i]}")
    print(f"  * Consumo para 1000 km: {consumo_total[i]:.1f} litros - R$ {custo_total[i]:.2f}")
print("* Relatório Final")
for i in range(len(modelos)):
    print(f"{i+1} - {modelos[i]:<10} - {consumo[i]:>5.1f} - {consumo_total[i]:>5.1f} litros - R$ {custo_total[i]:.2f}")
print(f"* O menor consumo é do {modelos[indice_mais_economico]}")