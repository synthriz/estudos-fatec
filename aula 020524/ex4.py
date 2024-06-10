#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#  O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores 
# para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir 
# outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e 
# o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
# mais 0,1% de juros por dia de atraso.
def valorPagamento(valorPrestacao, diasAtraso): #funcao que calcula o valor a ser pago, considerando os valores da prestaçao e dias atrasados
  multa = valorPrestacao * 0.03 #multa de 3% sobre o valor da prestaçao
  juros = valorPrestacao * (0.001 * diasAtraso) #juros de 0,1% por dias de atraso sobre o valor da prestaçao
  valorAPagar = valorPrestacao + multa + juros
  return valorAPagar

#variaveis para inicializar o relatorio do dia
totalPrestacoes = 0
valorTotalPago = 0

#inicia um loop pra solicitar repetidamente os valores de prestaçao/dias de atraso
while True:
  valorPrestacao = float(input("Digite o valor da prestação, ou encerre o dia digitando 0: "))

  if valorPrestacao == 0: #se o valor da prestaçao for 0, para o loop. nao pede mais os inputs, e mostra o relatorio do dia
    print("📜 Relatorio do dia: ")
    print("Total de prestações pagas hoje:", totalPrestacoes)
    print("Valor total pago: R$", valorTotalPago)
    break
#se o valor das prestacoes nao for 0, pede os dias com atraso e mostra o valor a ser pago com base nisso
  diasAtraso = int(input("Digite o número de dias em atraso: "))
  valorAPagar = valorPagamento(valorPrestacao, diasAtraso)

  print("Valor a ser pago: R$", valorAPagar)

#adiciona prestaçoes e os valores as variaveis antes 0, para mostrar no relatorio do dia
  totalPrestacoes += 1
  valorTotalPago += valorAPagar
