nome = "Pablo"
idade = 16
altura = 1.74
estudante = True


# tipo das variáveis
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'> 

print(str(nome))
print(nome)
print(idade)
# Pablo
# Pablo
# 16

idade_texto = "25"
idade_numero = int(idade_texto) # Converte string pra int
print(idade_numero)
print(idade_numero + 1) 

numero = 10
texto = str(numero) # "10" em string
print(texto)

print(f"Meu nome é {nome}, tenho {idade} sou estudante? {estudante}")

