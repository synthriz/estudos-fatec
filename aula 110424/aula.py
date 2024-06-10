def validar():
  try:
    num1 = int(input("Entre com o primeiro número: "))
    print ("✔️ O número digitado foi" , num1 )
    num2 = int(input("Entre com o segundo número: "))
    print ("✔️ O número digitado foi" , num2 )
    print("➡️ O valor da soma é", num1 + num2)
  except ValueError:
    print ("❌ Inválido, tente novamente")
    validar()

validar()