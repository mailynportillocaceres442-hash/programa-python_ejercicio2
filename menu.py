# Matriz de productos: [nombre, categoria, precio_base]
productos = [
    ["Hamburguesa", "Comida", 25000],
    ["Pizza", "Comida", 40000],
    ["Ensalada", "Saludable", 18000],
    ["Jugo Natural", "Bebidas", 12000],
    ["Café", "Bebidas", 8000],
    ["Pasta", "Comida", 35000]
]

# Parámetros de la promoción
categoria_objetivo = "Comida"
umbral_precio = 30000
descuento = 0.15

# Función para calcular precio final
def calcular_precio_final(producto):
    nombre, categoria, precio = producto

    if categoria == categoria_objetivo and precio > umbral_precio:
        precio_final = int(precio -(precio * descuento))
    else:
        precio_final = precio

    return precio_final

# Mostrar resultados
print("LISTA DE PRODUCTOS CON PROMOCIÓN\n")

for producto in productos:
    nombre, categoria, precio = producto
    precio_final = calcular_precio_final(producto)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio base:", precio)
    print("Precio final:", precio_final)
    print("------------------------")
