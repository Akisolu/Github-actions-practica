import sys
import subprocess
from pathlib import Path

# Ruta al archivo ejecutable main.py
MAIN_SCRIPT = Path(__file__).resolve().parents[2] / "main.py"

def run_cli_session(inputs: list[str]) -> subprocess.CompletedProcess:
    """Ejecuta main.py pasando una lista de entradas simuladas por stdin."""
    user_input = "\n".join(inputs) + "\n"
    
    process = subprocess.run(
        [sys.executable, str(MAIN_SCRIPT)],
        input=user_input,
        capture_output=True,
        text=True,
        timeout=5
    )
    return process

def test_e2e_flujo_agregar_y_salir(tmp_path, monkeypatch):
    # Opciones ingresadas por el usuario secuencialmente:
    # 1 (Agregar comida) -> ID: 1, Nombre: "Pizza E2E", Precio: 12.5 -> 4 (Salir)
    inputs = ["1", "1", "Pizza E2E", "12.5", "4"]
    
    result = run_cli_session(inputs)

    # Verificaciones E2E
    assert result.returncode == 0
    assert "Comida agregada exitosamente" in result.stdout
    assert "Saliendo del sistema..." in result.stdout

def test_e2e_menu_opcion_invalida_y_recuperacion():
    # Intenta opción '9' (inválida), luego '4' (Salir)
    inputs = ["9", "4"]
    
    result = run_cli_session(inputs)

    assert result.returncode == 0
    assert "Error: Debe ingresar un número entero entre 1 y 4." in result.stdout
    assert "Saliendo del sistema..." in result.stdout