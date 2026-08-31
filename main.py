from pydantic import BaseModel, Field, ValidationError
from src.utils.comida import Comida
from src.utils.input_menu import OpcionInput
from src.utils.id_comida import IdInput

def validar_opcion_menu(entrada: str) -> int:
    # Pydantic coerciona el string de input() a int y valida el rango [1, 4]
    datos = OpcionInput(opcion=entrada)
    return datos.opcion

def validar_comida(numero: str, nombre: str, precio: str) -> Comida:
    comida_validada = Comida(
        id=int(numero) if numero else None,
        nombre=nombre,
        precio=float(precio)  # Convierte la cadena del input() a float explícitamente
    )
    return comida_validada

def validar_id_comida(id: str) -> int:
    resultado = IdInput(id_comida=id)
    return resultado.id_comida

def solicitar_opcion() -> int | None:
    """Muestra el menú y retorna la opción validada o None si falló."""
    print("\n--- Sistema de Restaurante ---")
    print("1. Agregar comida")
    print("2. Ver comidas")
    print("3. Eliminar comida")
    print("4. Salir")
    
    entrada = input("\nIngrese una opción (1-4): ")
    
    try:
        return validar_opcion_menu(entrada)
    except ValidationError:
        print("\nError: Debe ingresar un número entero entre 1 y 4.")
        return None

def agregar_comida():
    """Función para agregar comida con reintento ante errores de validación."""
    while True:
        print("\n--- Registrar nueva comida ---")
        numero_comida = input("Ingrese el número de comida: ")
        nombre_comida = input("Ingrese el nombre de la comida: ")
        precio_comida = input("Ingrese el precio de la comida: ")

        try: 
            comida = validar_comida(numero_comida, nombre_comida, precio_comida)
            print(f"\nComida agregada exitosamente: {comida}") # Simulado
            return comida  # Sale de la función y del bucle
        except ValidationError as e:
            print("\nDatos inválidos. Por favor, intente de nuevo.")

def ver_comidas():
    """Función para ver comidas (simulada)."""
    print("\nMostrando todas las comidas (simulado)...")

def eliminar_comida():
    """Función para eliminar comida (simulada)."""
    while True:
        id_comida = input("Ingrese el ID de la comida a eliminar: ")

        try: 
            id_validado = validar_id_comida(id_comida)
            print(f"\nComida eliminada exitosamente: {id_validado}") # Simulado
            return id_validado # Sale de la funcion y del bucle
        except ValidationError as e:
            print("\nID inválido. Por favor, intente de nuevo.")

def main():
    while True:
        opcion = solicitar_opcion()
        
        if opcion is None:
            continue  # Reintenta el menú
        
        if opcion == 1:
            agregar_comida()
        elif opcion == 2:
            ver_comidas()
        elif opcion == 3:
            eliminar_comida()  # <-- Reemplaza el print por la llamada a la función
        elif opcion == 4:
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()