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