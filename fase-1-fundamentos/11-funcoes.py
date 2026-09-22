def soma(a, b):
    result = a + b
    return result

print(soma(6, 7))

def saudacao(nome, frase="Olá"):
    return f"{frase}, {nome}!"

print(saudacao("Carlos"))
print(saudacao("Pablo", "Quentao67"))

def calculoUndefined(*nums):
    return sum(nums)

print(calculoUndefined(1, 2, 4, 2))

def pessoa(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
        
pessoa(nome="Pablo", idade=16, curso="DS")


print("Calculadora")

def soma(a, b):
    result = a + b
    return result
    
def subtracao(a, b):
    result = a - b
    return result

def divisao(a, b):
    result = a / b
    return result
    
def multiplicacao(a, b):
    result = a * b
    return result

while True:
    escolha = int(input("Qual operação vc vai fazer?\n1- Adição \n2- Subtração \n3- Divisão \n4- Multiplicação \n5- sair \n"))
    if escolha == 5:
        break
    
    if escolha not in [1, 2, 3, 4]:
        print("Digite um valor válido")
        continue
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if escolha == 1:
        print(soma(num1, num2))
    elif escolha == 2:
        print(subtracao(num1, num2))
    elif escolha == 3 and num2 == 0:
        print("Erro! Divisão por 0")
    elif escolha == 3:
        print(divisao(num1, num2))
    elif escolha == 4:
        print(multiplicacao(num1, num2))
    
    