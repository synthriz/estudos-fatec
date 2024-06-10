senhaCerta = "desire"
tentativas = 0

def leia():
    senha = input("Digite a senha: ")
    return senha # precisa retornar pra conseguir usar o valor onde chamar a função

def imprima(mensagem):
    print(mensagem)

while tentativas < 3:
    handleSenha = leia()
    if handleSenha == senhaCerta:
        imprima("Acesso confirmado")
        break
    else:
        tentativas += 1
        imprima("Senha incorreta, tente novamente")

if tentativas == 3:
    imprima("Voce excedeu o limite de tentativas.")