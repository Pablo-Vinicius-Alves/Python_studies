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