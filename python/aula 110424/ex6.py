#Ler dois valores numéricos inteiros e efetuar a adição; caso o resultado seja maior que 10, apresentá-lo
n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))

resultado = n1 + n2

if resultado > 10:
  print("O valor da soma é", resultado)
else:
  print("O valor da soma não é maior que 10")