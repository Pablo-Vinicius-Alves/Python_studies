message = " Aprendendo Python "

print(message.strip())
print(message.lower())
print(message.upper())
print(message.replace("Python", "JavaScript"))
print(message.split())

texto = "Manhã,Tarde,Noite"
periodos = texto.split(",")
print(periodos)

hifen = "-"
print(hifen.join(periodos))