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