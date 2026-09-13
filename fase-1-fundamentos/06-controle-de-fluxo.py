while True:
    acao = input("Digite 'sair' para sair do programa")
    if acao == "sair":
        break
    print(f"Você digitou {acao} e saiu")
    
for i in range(14):
    if i % 2 != 0:
        continue
    print(i)
    