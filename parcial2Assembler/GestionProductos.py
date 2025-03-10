import csv

# Función para cargar los productos desde un archivo CSV
def cargar_productos(nombre_archivo):
    productos = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                try:
                    producto = {
                        "nombre": fila["nombre_producto"],  # Corregido
                        "precio": float(fila["precio"]),  # Convertir a float
                        "descuento": float(fila["porcentaje_descuento"])  # Convertir a float
                    }
                    productos.append(producto)
                except ValueError as e:
                    print(f"Error en los datos de la fila {fila}: {e}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    return productos

# Función para calcular el precio promedio de los productos
def calcular_precio_promedio(productos):
    if not productos:
        return 0
    total_precio = sum(p["precio"] for p in productos)
    return total_precio / len(productos)

# Aplicar descuento con lambda
def aplicar_descuento(productos):
    aplicar_descuento_lambda = lambda p: {**p, "precio_final": round(p["precio"] * (1 - p["descuento"] / 100), 2)}
    return list(map(aplicar_descuento_lambda, productos))

# Main
if __name__ == "__main__":
    archivo = "productos.csv"
    productos = cargar_productos(archivo)

    if productos:
        print("\nLista de productos cargados:")
        for p in productos:
            print(p)

        precio_promedio = calcular_precio_promedio(productos)
        print(f"\nPrecio promedio de los productos: ${precio_promedio:.2f}")

        productos_descuento = aplicar_descuento(productos)

        print("\nLista de productos con descuento aplicado:")
        for p in productos_descuento:
            print(p)
