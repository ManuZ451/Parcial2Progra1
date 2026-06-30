from funciones import (
     cargar_productos, guardar_productos,
     listar_productos, agregar_productos, buscar_productos,
     modificar_stock, eliminar_producto, mostrar_por_categoria, 
     mostrar_estadisticas, exportar_csv
)


def mostrar_menu():
    print ("\n=== Sistema de Gestion de Supermercado")
    print ("1. Listar productos.")
    print ("2. Agregar producto.")
    print ("3. Buscar producto por nombre.")
    print ("4. Modificar stock.")
    print ("5. Eliminar producto.")
    print ("6. Mostrar productos por categoria.")
    print ("7. Mostrar estadisticas.")
    print ("8. Exportar reporte CSV.")
    print ("9. Guardar y salir.")

def main():
    productos = cargar_productos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-9): ").strip()
        if opcion == "1":
            listar_productos(productos)
        elif opcion == "2":
            agregar_productos (productos)
        elif opcion == "3":
            buscar_productos (productos)
        elif opcion == "4":
            modificar_stock (productos)
        elif opcion == "5":
            eliminar_producto (productos)
        elif opcion == "6":
            mostrar_por_categoria  (productos)
        elif opcion == "7":
            mostrar_estadisticas  (productos)
        elif opcion == "8":
            exportar_csv  (productos)
        elif opcion == "9":
            guardar_productos (productos)
            print ("Datos guardados. Muchas gracias.")
            break
        else:
            print ("Opcion invalida, ingrese un numero del 1 al 9")

if  __name__ == "__main__":
    main()
#main ()