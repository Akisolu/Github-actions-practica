import pytest
from pydantic import ValidationError
import main as m

# ==========================================
# 1. CASOS VÁLIDOS (Límite 1 a 4)
# ==========================================

@pytest.mark.parametrize("input_val, esperado", [
    ("1", 1),  # Límite inferior
    ("2", 2),  # Caso medio
    ("3", 3),  # Caso medio
    ("4", 4),  # Límite superior
])
def test_validar_opcion_valida(input_val, esperado):
    resultado = m.validar_opcion_menu(input_val)
    assert resultado == esperado


# ==========================================
# 2. CASOS INVÁLIDOS (Lanza ValidationError)
# ==========================================

@pytest.mark.parametrize("input_val", [
    "abc",    # String no numérico
    "-1",     # Fuera de rango (menor a 1)
    "0",      # Fuera de rango (menor a 1)
    "5",      # Fuera de rango (mayor a 4)
    "99",     # Fuera de rango
    "1.5",    # Flotante en string
    "True",   # Booleano representado como texto en consola
    "",       # Cadena vacía
])
def test_validar_opcion_invalida(input_val):
    with pytest.raises(ValidationError):
        m.validar_opcion_menu(input_val)