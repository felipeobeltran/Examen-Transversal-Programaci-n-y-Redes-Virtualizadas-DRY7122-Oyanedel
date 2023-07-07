integrantes = [
    {"nombre": "Cristian", "apellido": "Cáceres"},
    {"nombre": "Cristobal", "apellido": "Illanes"},
    {"nombre": "Felipe", "apellido": "Oyanedel"},
    {"nombre": "Nicolas", "apellido": "Vásquez"}
]

lista_nombres_apellidos = []

for integrante in integrantes:
    nombre_apellido = integrante["nombre"] + " " + integrante["apellido"]
    lista_nombres_apellidos.append(nombre_apellido)

print(lista_nombres_apellidos)
