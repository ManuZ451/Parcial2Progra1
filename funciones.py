import json
import csv
import os

ARCHIVO_JSON = "productos.json"

def cargar_productos():
    if not os.path.exists(ARCHIVO_JSON):
        return []
    with open (ARCHIVO_JSON, "r", encoding="utf-8-sig") as f:
        return json.load (f)
    
def guardar_productos (productos):
    with open (ARCHIVO_JSON, "w", encoding= "utf-8") as f:
        json.dump (productos, f, ensure_ascii= False, indent=4)

def obtener_siguiente_id (productos):
    if not productos:
        return 1
    return max (p["id"] for p in productos) + 1

def validar_entero (mensaje):
    while True:
        valor = input (mensaje)
        return int (valor)
    
def validar_flotante (mensaje):
    while True:
        valor = input (mensaje).strip()
        if valor.count (".") <= 1 and valor.replace (",", "", 1).lstrip ("+-").isdigit ():
            numero = float (valor)
            if numero < 0:
                print ("Error, el valor no spuede ser negativo.")
                continue
            return numero
        print ("Error, debe ingresar un numero valido.")

def validar_cadena (mensaje):
    while True:
        valor = input (mensaje). strip ()
        if valor:
            return valor
        print ("Error, el campo no puede estar vacio.")

def listar_productos (productos):
    if not productos:
        print ("No hay productos cargados.")
        return
    print (f"\n {'ID':<5} {'Nombre':<25} {'Categoria':<15} {'Precio':>10} {'Stock':>8}")
    print ("-" * 65)
    for p in productos:
        print (f"{p['id']:<5} {p['nombre']:<25} {p['categoria']:<15} ${p['precio']:>9.2f} {p['stock']:>8}")
    print (f"\nTotal: {len(productos)} productos\n")

def agregar_productos (productos):

    id_nuevo = obtener_siguiente_id (productos)
    nombre = validar_cadena ("Nombre: ")
    for p in productos:
        if p ["nombre"].lower() == nombre.lower():
            print ("Error, ya existe un producto con ese nombre.")
            return
    categoria = validar_cadena ("Categoria: ")
    precio = validar_flotante ("Precio: ")
    stock = validar_entero ("Stock: ")
    
    if stock < 0:
        print ("Error, el stock no puede ser negativo.")
        return
    productos.append({
        "id": id_nuevo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    })
    print (f"Producto '{nombre}' agregado con ID {id_nuevo}.")

def buscar_productos (productos):
    termino = validar_cadena("Buscar (nombre o parte): "). lower()
    resultados = [p for p in productos if termino in p["nombre"].lower()]
    if not resultados:
        print ("No se encontraron productos.")
        return
    print (f"\n{'ID':<5} {'Nombre':<25} {'Categoria': <15} {'Precio': >10} {'Stock': >8}")
    print ("-" * 65)
    for p in resultados:
        print (f"{p['id']:<5} {p['nombre']:<25} {p['categoria']:<15} ${p['precio']:>9.2f} {p['stock']:>8}")

def modificar_stock (productos):
    id_prod = validar_entero ("ID del producto a modificar: ")
    for p in productos:
        if p["id"] == id_prod:
            print (f"Producto: {p['nombre']} - Stock actual: {p['stock']}")
            nuevo_stock = validar_entero ("Nuevo stock: ")
            if nuevo_stock < 0:
                print ("Error, el stock no puede ser negativo")
                return
            p ["stock"] = nuevo_stock
            print (f"Stock actualizado a {nuevo_stock}.")
            return
    print ("Error, no se encontró un producto con ese ID")

def eliminar_producto (productos):
    id_prod = validar_entero ("ID del producto a eliminar: ")
    for i, p in enumerate (productos):
        if p ["id"] == id_prod:            
            confirmacion  = input (f"Eliminar '{p['nombre']}'? (S/N): ").strip().lower()
            if confirmacion == "S":
                productos.pop(i)
                print ("Producto eliminado.")
            else:
                print ("Operacion cancelada.")
            return
    print ("Error, no se encontro un producto con ese ID.")

def mostrar_por_categoria(productos):
    if not productos:
        print ("No hay productos cargados.")
        return
    categorias = {}
    for p in productos:
        cat = p["categoria"]
        if cat not in categorias:
            categorias [cat] = []
        categorias[cat].append (p)
    for cat, prods in sorted (categorias.items()):
        print(f"\n---{cat}---")
        for p in prods:
            print (f"{p['id']:<5} {p['nombre']:<25} ${p['precio']:>9.2f} Stock: {p['stock']}")

def mostrar_estadisticas(productos):
    if not productos:
        print ("No hay productos cargados.")
        return
    total_productos = len (productos)
    stock_total = sum (p["stock"] for p in productos)
    valor_inventario = sum (p["precio"] * p ["stock"] for p in productos)
    sin_stock = [p for p in productos if p ["stock"] == 0]
    categorias = set (p["categoria"] for p in productos)

    print ("\n --- Estadisticas del supermercado.---")
    print (f"Total de productos: {total_productos}")
    print (f"Categorias: {len(categorias)} ({', '.join(sorted(categorias))})")
    print (f"Stock total: {stock_total} unidades.")
    print (f"Valor total del inventario: ${valor_inventario:.2f}")
    if sin_stock:
        print (f"Productos sin stock: {len(sin_stock)}")
        for p in sin_stock:
            print (f" - {p['nombre']}")
    else:
        print ("Todos los productos tienen stock.")

def exportar_csv(productos):
    if not productos:
        print ("No hay productos para exportar.")
        return
    nombre_csv = "reporte_productos.csv"
    with open (nombre_csv, "w", newline="", encoding= "utf-8") as f:
        campo = ["id", "nombre", "categoria", "precio", "stock"]
        escritor = csv.DictWriter (f, fieldnames=campo)
        escritor.writeheader()
        escritor.writerows (productos)
    print (f"Reporte exportado a '{nombre_csv}' ({len(productos)} productos).")