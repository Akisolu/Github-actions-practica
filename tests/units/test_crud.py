import json
from unittest.mock import patch, mock_open
import pytest

from src import crud
from src.utils.comida import Comida

COMIDAS_MOCK = [
    {"id": 1, "nombre": "Pizza", "precio": 10.99},
    {"id": 2, "nombre": "Hamburguesa", "precio": 8.50}
]

# ==========================================
# 1. PRUEBAS DE LECTURA
# ==========================================

@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_obtener_todas_exito(mock_file, mock_exists):
    resultado = crud.obtener_todas()
    assert len(resultado) == 2
    assert resultado[0]["nombre"] == "Pizza"


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_obtener_por_id_existente(mock_file, mock_exists):
    resultado = crud.obtener_por_id(1)
    assert resultado is not None
    assert resultado["id"] == 1
    assert resultado["nombre"] == "Pizza"


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_obtener_por_id_inexistente(mock_file, mock_exists):
    resultado = crud.obtener_por_id(99)
    assert resultado is None


@patch("pathlib.Path.exists", return_value=False)
def test_cargar_datos_archivo_no_existe(mock_exists):
    resultado = crud._cargar_datos()
    assert resultado == []


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="JSON_INVALIDO{{{")
def test_cargar_datos_json_corrupto(mock_file, mock_exists):
    resultado = crud._cargar_datos()
    assert resultado == []


# ==========================================
# 2. PRUEBAS DE CREACIÓN
# ==========================================

@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[])
def test_crear_comida_sin_id(mock_cargar, mock_guardar):
    nueva_comida = Comida(nombre="Tacos", precio=5.0)
    resultado = crud.crear_comida(nueva_comida)
    
    assert resultado["id"] == 1
    assert resultado["nombre"] == "Tacos"
    mock_guardar.assert_called_once()


@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_crear_comida_incrementa_id(mock_cargar, mock_guardar):
    nueva_comida = Comida(nombre="Sushi", precio=15.0)
    resultado = crud.crear_comida(nueva_comida)
    
    assert resultado["id"] == 2
    mock_guardar.assert_called_once()


# ==========================================
# 3. PRUEBAS DE ELIMINACIÓN
# ==========================================

@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_eliminar_comida_exito(mock_cargar, mock_guardar):
    exito = crud.eliminar_comida(1)
    assert exito is True
    mock_guardar.assert_called_once_with([])


@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_eliminar_comida_inexistente(mock_cargar, mock_guardar):
    exito = crud.eliminar_comida(99)
    assert exito is False
    mock_guardar.assert_not_called()