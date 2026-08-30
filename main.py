from pydantic import BaseModel, Field, ValidationError

class OpcionInput(BaseModel):
    # Valida entero estrictamente en el rango 1 a 4
    opcion: int = Field(..., ge=1, le=4)

def validar_opcion(entrada: str) -> int | None:
    # Pydantic coerciona el string de input() a int y valida el rango [1, 4]
    datos = OpcionInput(opcion=entrada)
    return datos.opcion

def solicitar_opcion() -> int | None:
    """Muestra el menú y retorna la opción validada o None si falló."""
    print("\n--- Sistema de Restaurante ---")
    print("1. Agregar comida")
    print("2. Ver comidas")
    print("3. Eliminar comida")
    print("4. Salir")
    
    entrada = input("\nIngrese una opción (1-4): ")
    
    try:
        entrada_validada = validar_opcion(entrada)
    except ValidationError:
        print("\nError: Debe ingresar un número entero entre 1 y 4.")

    return entrada_validada

if __name__ == "__main__":
    while True:
        opcion = solicitar_opcion()
        
        if opcion is None:
            continue  # Reintenta el menú
        
        if opcion == 1:
            print("-> Ejecutando: Agregar comida...")
        elif opcion == 2:
            print("-> Ejecutando: Ver comidas...")
        elif opcion == 3:
            print("-> Ejecutando: Eliminar comida...")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break  # Rompe el bucle while True y finaliza