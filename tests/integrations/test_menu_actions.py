import pytest
import main as app

def test_agregar_comida_exito(monkeypatch, capsys):
    """Flujo exitoso: 3 inputs correspondientes a id, nombre y precio."""
    # Aseguramos entradas válidas para Pydantic
    respuestas = iter(["1", "Pizza Pepperoni", "12.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    resultado = app.agregar_comida()

    assert resultado.id == 1
    assert resultado.nombre == "Pizza Pepperoni"
    assert resultado.precio == 12.5

    captured = capsys.readouterr()
    assert "Comida agregada exitosamente" in captured.out


def test_agregar_comida_reintento_por_error(monkeypatch, capsys):
    """Prueba que ante un error se consuman 6 entradas (3 del intento fallido + 3 del exitoso)."""
    respuestas = iter([
        "-1", "Pizza", "10.0",   # Intento 1: ID -1 invalida Pydantic (3 inputs)
        "1", "Pizza", "10.0"     # Intento 2: Datos válidos (3 inputs)
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    resultado = app.agregar_comida()

    assert resultado.id == 1
    captured = capsys.readouterr()
    assert "Datos inválidos. Por favor, intente de nuevo." in captured.out
    assert "Comida agregada exitosamente" in captured.out