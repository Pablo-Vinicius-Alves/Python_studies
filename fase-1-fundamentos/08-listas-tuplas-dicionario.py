# Listas

paises = ["Japão", "Canadá", "Itália"]

paises.append("USA")
print(paises)
paises.insert(1, "Mongólia")
print(paises)
paises.remove("USA")
paises.pop()
paises.pop(0)
print(paises)

paises.append("Austrália")
print(paises[0])
print(paises[-1])
print(paises[0:2])
print(len(paises))
print("USA" in paises)

paises.sort()
print(paises)
paises.reverse()
print(paises)

# Tuplas

coordernadas = (10, 20)
print(coordernadas[0])

x, y = coordernadas
print(f"Posição: {x, y}")

# Dicionário

mochila = {
    "espada": "Samehada",
    "pocao": "ForçaV",
    "moedas": 79
}

print(mochila["espada"])
mochila["moedas"] += 10
print(mochila["moedas"])
mochila["escudo"] = "Madeira"
print(mochila)

print(mochila.get("espada"))
print(mochila.get("moedas", "Vázio"))

print(mochila.keys())
print(mochila.values())

for chave, valor in mochila.items():
    print(chave, ":", valor)
    
# Sets

info = {1,1,1,3,2,3,4,2,4,3,2}
print(info)

listaTotal = [1,1,3,2,3,4,2,4,3,]
listaUnicas = list(set(listaTotal))

print(listaUnicas)

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)
print(a | b)
print(a - b)