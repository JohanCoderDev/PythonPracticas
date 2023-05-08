def suma(x,y):
    return x+y

datos = [2, True, "Luis", 4.5]

for n in datos:
    print(n)

print("------------")

datos.insert(2, 4.2)
print(datos[2])

datos.pop(2)
print(datos[2])

datos.remove("Luis")
print(datos[2])

print("-------------")

for n in datos:
    print(n)


PoblacionPaises = {
        'Colombia': 50,
        'Argentina': 44,
        'Brasil': 210,
    }

print(PoblacionPaises)

PoblacionPaises.items()





