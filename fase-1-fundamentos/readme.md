# Fundamentos de Python
 
---
 
## 1. Variáveis e tipos de dados
 
Uma variável é um nome que aponta para um valor guardado na memória. Em Python você não declara o tipo, ele é inferido:
 
```python
nome = "Carlos"       # str (texto)
idade = 25             # int (inteiro)
altura = 1.78          # float (decimal)
estudante = True       # bool (verdadeiro/falso)  

print(type(nome))
print(idade)
```

**Conversão entre tipos** é comum e necessária, principalmente quando você recebe algo do usuário (que sempre vem como texto):
 
```python
idade_texto = "25"
idade_numero = int(idade_texto) 
print(idade_numero + 1)            
 
numero = 10
texto = str(numero)                # "10"
```
 
**Erro comum:** tentar somar string com número direto (`"25" + 1`) gera erro. Python não converte automaticamente entre tipos incompatíveis.
 
**Exercício:** crie três variáveis (seu nome, sua idade, se você é estudante) e imprima uma frase usando as três, com o tipo de cada uma abaixo.

---

## 2. Operadores
 
**Aritméticos:**
```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333... (sempre retorna float)
print(10 // 3)  # 3  (divisão inteira, descarta o resto)
print(10 % 3)   # 1  (resto da divisão)
print(10 ** 2)  # 100 (potência)
```
 
**Comparação** (sempre retornam true ou false):
```python
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 >= 5)   # True
```
 
**Lógicos:**
```python
idade = 20
tem_carteira = True
 
print(idade >= 18 and tem_carteira)   
print(idade >= 18 or tem_carteira)    
print(not tem_carteira)                
```
 
**Exercício:** sem rodar o código, suponha oque cada uma dessas linhas retorna, depois confira:
```python
print(7 % 2)
print(3 == 3.0)
print(10 > 5 and 3 > 5)
print(not (10 > 5))
```
 
---

## 3. Estruturas condicionais
 
```python
nota = 50
 
if nota >= 90:
    conceito = "A"
elif nota >= 70:
    conceito = "B"
elif nota >= 50:
    conceito = "C"
else:
    conceito = "D"
 
print(f"Seu conceito é {conceito}")
```
 
Pontos que importam:
- A indentação (espaços no início da linha) **não é estética, é sintaxe**. Python usa ela para saber o que está dentro do `if`. Erro de indentação quebra o programa.
- `elif` só é avaliado se o `if` anterior for falso — a ordem das condições importa (por isso `>= 90` vem antes de `>= 70`, senão nunca seria alcançado).
- Nem todo `if` precisa de `else`.
**Exercício:** escreva um programa que recebe um número e imprime se ele é positivo, negativo ou zero. Depois, um segundo que recebe um número e diz se é par ou ímpar.

```python
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
```
 
---

## 4. Input e output
 
```python
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))  # input() sempre retorna string.
 
print(f"Olá, {nome}! Você tem {idade} anos.")
```
 
`f-strings` (o `f` antes das aspas) são a forma moderna de formatar texto com variáveis dentro — evite concatenar com `+`, fica mais difícil de ler.
 
**Erro comum:** esquecer de converter o `input()` para número antes de fazer conta com ele. Se você tentar `idade + 1` sem o `int()`, o Python vai tentar "somar" string com número e vai quebrar.
 
---
 
 ## 5. Loops: for e while
 
**`for`** — use quando você sabe quantas vezes vai iterar:
```python
for i in range(5):   # 0, 1, 2, 3, 4
    print(i)
 
nome = "Ana"
for letra in nome:
    print(letra)     # imprime cada letra
```
 
**`while`** — use quando a repetição depende de uma condição que pode mudar, sem número fixo de repetições:
```python
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
 
print("Acesso liberado")
```
 
**Regra prática:** se você já sabe de antemão quantas vezes vai repetir (ou tem uma lista/sequência para percorrer), use `for`. Se depende de uma condição que só se resolve durante a execução, use `while`. Essa é a dúvida mais comum de quem está começando — e a resposta é sempre essa lógica, não decoreba.
 
---

## 6. Controle de fluxo em loops
 
```python
# break: interrompe o loop imediatamente
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break
    print(f"Você digitou: {comando}")
 
# continue: pula para a próxima iteração, sem executar o resto do bloco
for numero in range(10):
    if numero % 2 != 0:
        continue        # pula números ímpares
    print(numero)       
```
 
`while True` combinado com `break` é o padrão usado para criar menus que rodam até o usuário decidir sair.
 
---

## Projeto da semana: Calculadora com menu
 
Requisitos — construa sozinho antes de olhar qualquer solução pronta:
 
1. O programa mostra um menu: soma, subtração, multiplicação, divisão, sair
2. Roda em loop até o usuário escolher "sair"
3. Pede dois números ao usuário para cada operação
4. Trata o caso de divisão por zero sem quebrar o programa
5. Trata o caso do usuário digitar uma opção inválida no menu

```python
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
```

---