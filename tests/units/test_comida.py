import pytest
from pydantic import ValidationError
import src.utils.comida as c

# ==========================================
# 1. CASOS FELICES Y EXTREMOS (Parametrizados)
# ==========================================

@pytest.mark.parametrize("id_val, nombre, precio", [
    (5, "Pizza", 10.99),                 # Caso feliz estándar
    (None, "Arroz", 12.00),               # ID opcional/None
    (1, "a", 0.1),                        # Valores mínimos/cortos
    (12345678, "abcdefghijkl", 12345678.90) # Valores grandes
])
def test_comida_creacion_exitosa(id_val, nombre, precio):
    comida = c.Comida(id=id_val, nombre=nombre, precio=precio)
    
    assert comida.id == id_val
    assert comida.nombre == nombre
    assert comida.precio == precio


# ==========================================
# 2. CASOS DE ERROR (ValidationErrors)
# ==========================================

# --- Errores en ID ---
@pytest.mark.parametrize("id_invalido", [
    "abc",   # String no numérico
    -1,      # Entero negativo
    -99,     # Entero negativo grande
    True,    # Booleano
    1.5,     # Float
])
def test_comida_id_invalido(id_invalido):
    with pytest.raises(ValidationError):
        c.Comida(id=id_invalido, nombre="Pizza", precio=10.99)


# --- Errores en Nombre ---
@pytest.mark.parametrize("nombre_invalido", [
    123,     # Número
    "",      # String vacío
    None,    # Sin nombre
    True,    # Booleano
])
def test_comida_nombre_invalido(nombre_invalido):
    with pytest.raises(ValidationError):
        c.Comida(id=1, nombre=nombre_invalido, precio=10.99)


# --- Errores en Precio ---
@pytest.mark.parametrize("precio_invalido", [
    "abc",    # String no convertible a float
    -10.99,   # Precio negativo
    None,     # Sin precio
    True,     # Booleano
])
def test_comida_precio_invalido(precio_invalido):
    with pytest.raises(ValidationError):
        c.Comida(id=1, nombre="Pizza", precio=precio_invalido)