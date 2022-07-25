def saudacao(saudacao, nome):
    print(saudacao, nome)


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


def aumento(valor, percentual):
    return valor + (valor * (percentual/100))


def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 5 == 0:
        return "Buzz"
    elif numero % 3 == 0:
        return "Fizz"
    else:
        return numero


nome = input("Digte seu nome: ")
saudando = "Olá"
saudacao(saudando, nome)

###########################
print()

while True:
    n1 = input("Soma de 3 números - Digite n1: ")
    n2 = input("Digite n2: ")
    n3 = input("Digite n3: ")
    if not n1.isdigit() or not n2.isdigit() or not n3.isdigit():
        print("Erro: você não digitou números.")
        continue
    else:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        soma(n1, n2, n3)
        break

###########################
print()

while True:
    valor = input("Aumento do valor em % - Digite o valor: ")
    porcentagem = input("Digite o aumento percentual: ")
    caractere = "%"
    for x in range(len(porcentagem)):
        if caractere == porcentagem[x]:
            porcentagem = porcentagem.replace(caractere,"")
            break

    if not valor.isdigit() or not porcentagem.isdigit():
        print("Erro: você não digitou números.")
        continue
    else:
        valor = int(valor)
        porcentagem = int(porcentagem)
        print(aumento(valor, porcentagem))
        break

###########################
print()
while True:
    number = input("FizzBuzz - Digite um numero: ")

    if not number.isdigit():
        print("Erro: você não digitou corretamente.")
        continue
    else:
        number = int(number)
        print(fizzbuzz(number))
        break
