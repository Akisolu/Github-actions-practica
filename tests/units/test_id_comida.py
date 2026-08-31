import pytest
from pydantic import ValidationError
from src.utils.id_comida import IdInput

@pytest.mark.parametrize("input_val, esperado", [
    ("1", 1),
    ("100", 100),
    ("9999", 9999),
])
def test_id_input_valido(input_val, esperado):
    validador = IdInput(id_comida=input_val)
    assert validador.id_comida == esperado

@pytest.mark.parametrize("input_val", [
    "abc",    # Texto no numérico
    "0",      # Fuera de rango (debe ser > 0)
    "-1",     # Entero negativo
    "1.5",    # Flotante
    "",       # Cadena vacía
])
def test_id_input_invalido(input_val):
    with pytest.raises(ValidationError):
        IdInput(id_comida=input_val)