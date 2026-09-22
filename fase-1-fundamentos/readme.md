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

# Estruturas de Dados Nativas
 
## 1. Listas
 
Coleção ordenada e **mutável** (você pode alterar depois de criada).
 
```python
frutas = ["maçã", "banana", "uva"]
 
frutas.append("laranja")       # adiciona no final
frutas.insert(0, "morango")    # insere em posição específica
frutas.remove("banana")        # remove pelo valor
frutas.pop()                    # remove e retorna o último item
frutas.pop(0)                    # remove e retorna o item no índice 0
 
print(frutas[0])                # acessa pelo índice (começa em 0)
print(frutas[-1])               # índice negativo = a partir do final
print(frutas[1:3])              # slicing: itens do índice 1 até o 2 (exclui o 3)
print(len(frutas))              # tamanho da lista
print("uva" in frutas)          # True/False — verifica se existe
 
frutas.sort()                   # ordena a lista (altera a original)
frutas.reverse()                # inverte a ordem
```
 
**Erro comum:** tentar acessar um índice que não existe (`frutas[10]` numa lista de 3 itens) gera `IndexError`. Sempre confira o tamanho antes se não tiver certeza.
 
---

## 2. Tuplas
 
Igual à lista, mas **imutável** — depois de criada, não muda. Use quando os dados não devem ser alterados (coordenadas, dias da semana, etc.):
 
```python
coordenada = (10, 20)
print(coordenada[0])    # 10
 
# isso gera erro:
# coordenada[0] = 5     # TypeError
 
# desempacotamento — muito usado
x, y = coordenada
print(x, y)              # 10 20
```
 
Por que usar tupla em vez de lista? Performance um pouco melhor e, principalmente, **intenção**: sinaliza no código que aquele dado não deve mudar.
 
---

## 3. Dicionários
 
Coleção de pares chave-valor. Pense em uma ficha de cadastro:
 
```python
pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo"
}
 
print(pessoa["nome"])           # acessa pelo valor da chave
pessoa["idade"] = 29             # altera um valor
pessoa["profissao"] = "Analista" # adiciona uma nova chave
 
print(pessoa.get("nome"))                    # forma segura de acessar
print(pessoa.get("salario", "não informado")) # retorna um padrão se a chave não existir
 
for chave, valor in pessoa.items():
    print(chave, ":", valor)
 
print(pessoa.keys())      # todas as chaves
print(pessoa.values())    # todos os valores
```
 
**Diferença entre `pessoa["chave"]` e `pessoa.get("chave")`:** o primeiro gera erro (`KeyError`) se a chave não existir; o segundo retorna `None` (ou o valor padrão que você definir). Use `.get()` sempre que não tiver certeza se a chave existe.
 
---

## 4. Sets
 
Coleção **não ordenada** de itens **únicos** — útil para eliminar duplicados ou verificar pertencimento rapidamente:
 
```python
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)              # {1, 2, 3} — duplicados somem sozinhos
 
lista_com_duplicados = [1, 2, 2, 3, 3, 3, 4]
sem_duplicados = list(set(lista_com_duplicados))
print(sem_duplicados)       # [1, 2, 3, 4]
 
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # interseção: {2, 3}
print(a | b)    # união: {1, 2, 3, 4}
print(a - b)    # diferença: {1}
```
 
Sets não têm ordem garantida e não permitem acessar por índice (`numeros[0]` não funciona).
 
---

## 5. Compreensão de listas e dicionários
 
Forma compacta de criar uma lista/dicionário a partir de outra, aplicando uma operação ou filtro:
 
```python
# forma tradicional
quadrados = []
for n in range(10):
    quadrados.append(n ** 2)
 
# com list comprehension — mesma coisa, uma linha
quadrados = [n ** 2 for n in range(10)]
 
# com filtro (só os pares)
pares = [n for n in range(10) if n % 2 == 0]
 
# dict comprehension
quadrados_dict = {n: n ** 2 for n in range(5)}
print(quadrados_dict)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
 
Não force o uso disso — se a lógica for complexa, um `for` tradicional é mais legível. Compreensão é para casos simples e diretos.
 
---

## 6. Manipulação de strings
 
```python
texto = "  Python é ótimo  "
 
print(texto.strip())          # remove espaços das pontas
print(texto.lower())          # tudo minúsculo
print(texto.upper())          # tudo maiúsculo
print(texto.replace("ótimo", "poderoso"))
print(texto.split())          # divide em lista, por espaço: ['Python', 'é', 'ótimo']
 
frase = "python,java,javascript"
linguagens = frase.split(",")  # ['python', 'java', 'javascript']
 
separador = "-"
print(separador.join(linguagens))   # 'python-java-javascript'
 
print(texto.strip().startswith("Python"))  # False, porque tem espaço — por isso o strip() antes
print("ótimo" in texto)        # True — verifica se a substring existe
```
 
`.split()` e `.join()` são o par mais usado: um quebra texto em lista, o outro junta lista em texto. Vai aparecer o tempo todo quando você trabalhar com arquivos CSV mais pra frente.
 
---

## 7. Funções
 
Bloco de código reutilizável, que você define uma vez e chama quantas vezes precisar.
 
```python
def somar(a, b):
    resultado = a + b
    return resultado
 
print(somar(3, 4))     # 7
```
 
**Parâmetros com valor padrão** — usados quando o argumento é opcional:
 
```python
def saudacao(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"
 
print(saudacao("Ana"))              # Olá, Ana!
print(saudacao("Ana", "Bom dia"))   # Bom dia, Ana!
```
 
**`*args`** — recebe uma quantidade indefinida de argumentos posicionais, como uma tupla:
 
```python
def somar_varios(*numeros):
    return sum(numeros)
 
print(somar_varios(1, 2, 3, 4))   # 10
```
 
**`**kwargs`** — recebe uma quantidade indefinida de argumentos nomeados, como um dicionário:
 
```python
def cadastrar(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
 
cadastrar(nome="Ana", idade=28, cidade="São Paulo")
```
 
**Escopo de variáveis** — variável criada dentro de uma função só existe dentro dela:
 
```python
def teste():
    x = 10
    print(x)
 
teste()
print(x)   # erro: NameError, x não existe fora da função
```
 
Isso evita que funções diferentes "vazem" variáveis umas nas outras sem querer. Se precisar que uma função altere uma variável externa, ela deve **retornar** o valor e você reatribui, em vez de tentar alterar diretamente de dentro (existe a palavra `global` para isso, mas evite usá-la — é fonte comum de bugs difíceis de rastrear).
 
**Erro comum:** esquecer o `return` e esperar que a função "devolva" algo sozinha. Sem `return`, a função sempre retorna `None`:
 
```python
def somar_errado(a, b):
    a + b        # calcula mas não retorna
 
resultado = somar_errado(3, 4)
print(resultado)   # None
```

**Exercício:** reescreva a calculadora da semana 2 usando uma função para cada operação (`somar(a, b)`, `subtrair(a, b)`, etc.), em vez de colocar a conta direto no `print`. Isso é o passo natural antes da agenda de contatos, porque o projeto abaixo pede pelo menos uma função para cada ação do menu.
 
---
 
## Projeto da semana: Agenda de contatos
 
Construa um programa de linha de comando que:
 
1. Guarda contatos em uma lista de dicionários, cada um com `nome`, `telefone` e `email`
2. Tem um menu com opções: adicionar contato, listar todos, buscar por nome, remover por nome, sair
3. Roda em loop até o usuário escolher sair (mesma lógica da calculadora)
4. Na busca, trata o caso do nome não ser encontrado
5. Ao listar, mostra os contatos de forma legível (não a lista/dicionário cru)
6. Cada ação do menu (adicionar, listar, buscar, remover) deve ser uma função separada, chamada de dentro do loop principal
Isso te obriga a combinar listas, dicionários, loops, condicionais e manipulação de string (para a busca, considere usar `.lower()` nos dois lados da comparação, senão "Ana" e "ana" seriam tratados como diferentes). Monte sozinho, trave onde precisar travar, e me manda o código quando tiver algo rodando.