nota = 75

if nota >= 90: 
    conceito = "A"
elif nota >= 70:
    conceito = "B"
elif nota >= 50:
    conceito = "C"
else:
    conceito = "D-"

print(f"Sua nota foi {nota}, seu nível de conceito é {conceito}")

numero = -4

if numero > 0:
    resposta = "Positivo +"
elif numero < 0:
    resposta = "Negativo -"
else:
    resposta = "Nulo 0"
    
print(resposta)

testePar = 8

if testePar % 2 == 0:
    answer = "Par"
else:
    answer = "Impar"    
    
print(answer)