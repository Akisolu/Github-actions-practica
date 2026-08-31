from unittest.mock import patch
import pytest
import main as app
from src.utils.comida import Comida


@patch("main.crud.crear_comida")
def test_agregar_comida_exito(mock_crear_comida, monkeypatch, capsys):
    """Flujo exitoso: simula la entrada del usuario y verifica el llamado al CRUD."""
    # Configurar el retorno simulado que devolvería crud.crear_comida
    mock_crear_comida.return_value = {
        "id": 1,
        "nombre": "Pizza Pepperoni",
        "precio": 12.5
    }

    # Entradas de consola: ID, Nombre, Precio
    respuestas = iter(["1", "Pizza Pepperoni", "12.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    resultado = app.agregar_comida()

    # 1. Validar el retorno de la función
    assert resultado.id == 1
    assert resultado.nombre == "Pizza Pepperoni"
    assert resultado.precio == 12.5

    # 2. Verificar que se llamó a crud.crear_comida exactamente una vez con el objeto Comida
    mock_crear_comida.assert_called_once()
    args, _ = mock_crear_comida.call_args
    assert isinstance(args[0], Comida)
    assert args[0].id == 1
    assert args[0].nombre == "Pizza Pepperoni"

    # 3. Validar salida por consola
    captured = capsys.readouterr()
    assert "Comida agregada exitosamente" in captured.out


@patch("main.crud.crear_comida")
def test_agregar_comida_reintento_por_error(mock_crear_comida, monkeypatch, capsys):
    """Verifica que el CRUD no se ejecute en el intento fallido y solo se llame tras validar."""
    mock_crear_comida.return_value = {
        "id": 1,
        "nombre": "Pizza",
        "precio": 10.0
    }

    respuestas = iter([
        "-1", "Pizza", "10.0",   # Intento 1: ID -1 lanza ValidationError
        "1", "Pizza", "10.0"     # Intento 2: Datos válidos
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    resultado = app.agregar_comida()

    assert resultado.id == 1

    # Verificar que el CRUD se llamó solo 1 vez (después del reintento exitoso)
    mock_crear_comida.assert_called_once()

    captured = capsys.readouterr()
    assert "Datos inválidos. Por favor, intente de nuevo." in captured.out
    assert "Comida agregada exitosamente" in captured.out

@patch("main.crud.obtener_todas")
def test_ver_comidas(mock_obtener_todas, capsys):
    mock_obtener_todas.return_value = [
        {"id": 1, "nombre": "Pizza", "precio": 10.0},
        {"id": 2, "nombre": "Tacos", "precio": 5.0}
    ]

    app.ver_comidas()

    captured = capsys.readouterr()
    assert "ID: 1, Nombre: Pizza, Precio: 10.0" in captured.out
    assert "ID: 2, Nombre: Tacos, Precio: 5.0" in captured.out
    mock_obtener_todas.assert_called_once()


@patch("main.crud.eliminar_comida")
def test_eliminar_comida_exito(mock_eliminar_comida, monkeypatch, capsys):
    mock_eliminar_comida.return_value = True
    monkeypatch.setattr("builtins.input", lambda _: "1")

    resultado = app.eliminar_comida()

    assert resultado == 1
    mock_eliminar_comida.assert_called_once_with(1)
    captured = capsys.readouterr()
    assert "Comida eliminada exitosamente: 1" in captured.out