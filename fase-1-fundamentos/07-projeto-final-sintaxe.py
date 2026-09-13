print("Calculadora")

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
        print(num1 + num2)
    elif escolha == 2:
        print(num1 - num2)
    elif escolha == 3 and num2 == 0:
        print("Erro! Divisão por 0")
    elif escolha == 3:
        print(num1 / num2)
    elif escolha == 4:
        print(num1 * num2)
    
    


