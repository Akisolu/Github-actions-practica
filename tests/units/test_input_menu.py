import pytest
from pydantic import ValidationError
from src.utils.input_menu import OpcionInput


# ==========================================
# 1. CASOS VÁLIDOS (Límite 1 a 4)
# ==========================================

@pytest.mark.parametrize("input_val, esperado", [
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
])
def test_opcion_input_valida(input_val, esperado):
    # Instanciación directa del modelo ubicado en src/utils/input.py
    validador = OpcionInput(opcion=input_val)
    assert validador.opcion == esperado


# ==========================================
# 2. CASOS INVÁLIDOS (Lanza ValidationError)
# ==========================================

@pytest.mark.parametrize("input_val", [
    "abc",    # Texto no numérico
    "-1",     # Fuera de rango inferior
    "0",      # Fuera de rango inferior
    "5",      # Fuera de rango superior
    "99",     # Fuera de rango
    "1.5",    # Float
    "True",   # Booleano como string
    "",       # String vacío
])
def test_opcion_input_invalida(input_val):
    with pytest.raises(ValidationError):
        OpcionInput(opcion=input_val)