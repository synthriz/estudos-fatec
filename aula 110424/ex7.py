#A prefeitura de Carapicuíba abriu uma linha de crédito para os funcionários estatutários. 
# Valor máximo da prestação não poderá ultrapassar 30% do salário bruto. 
# Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação 
# e informar se o empréstimo pode ou não ser concedido
valorSalario = int(input("Escreva o valor do salário bruto: "))
valorPrestacao = int(input("Escreva o valor da prestação: "))

percentualMaximo = valorSalario * 0.3

if valorPrestacao <= percentualMaximo:
    print("O empréstimo pode ser concedido")
else:
    print("O empréstimo não pode ser concedido")