# Proyecto de pruebas y automatización CI/CD

![CI/CD Build Status](https://github.com/Akisolu/python-cli-ci-cd-showcase/actions/workflows/build.yml/badge.svg)

Este repositorio está orientado a demostrar buenas prácticas de testing y automatización en un proyecto Python. El foco principal no es la funcionalidad del restaurante en sí, sino la forma en que se valida el código, se protege la calidad y se automatiza la entrega mediante GitHub Actions.

La app funciona como una pequeña CLI para gestionar comidas, pero en este proyecto la parte más importante es la infraestructura de calidad: pruebas, validaciones y pipeline de integración continua / despliegue continuo.

## Objetivo del repositorio

Este proyecto sirve como ejemplo práctico de:

- diseño de pruebas automatizadas con `pytest`
- organización por capas de prueba: unitarias, de integración y end-to-end
- validación de lógica y comportamiento del sistema
- automatización de ejecución en GitHub Actions
- compilación de artefactos ejecutables con PyInstaller
- publicación automática de releases en GitHub

## Enfoque del proyecto

La prioridad del repositorio es demostrar cómo se garantiza la calidad del software antes de publicar una versión:

- se prueban funciones de negocio
- se validan flujos de usuario
- se comprueban errores y reintentos
- se ejecutan las pruebas en cada cambio
- se compila el binario solo si el pipeline pasa

## Descarga y Ejecución

Si deseas probar la aplicación sin instalar Python:

1. Ve a la pestaña de **Releases** en GitHub y descarga la última versión para tu sistema operativo.
2. **Windows:** Ejecuta `restaurante_cli_windows.exe`.
3. **Linux:** Otorga permisos de ejecución `chmod +x restaurante_cli_linux` y ejecuta `./restaurante_cli_linux`.

## Estructura del proyecto

```text
├── .github/
│   └── workflows/
│       └── build.yml                 # Pipeline principal de CI/CD
├── src/
│   ├── crud.py                       # Lógica de persistencia de datos
│   └── utils/
│       ├── comida.py                 # Modelo Pydantic para una comida
│       ├── id_comida.py              # Validación de IDs
│       └── input_menu.py             # Validación de opciones del menú
├── tests/
│   ├── units/                        # Pruebas unitarias
│   ├── integrations/                 # Pruebas de integración
│   └── end-to-end/                   # Pruebas del flujo real de la CLI
├── main.py                           # Punto de entrada de la aplicación
├── conftest.py                       # Configuración de pytest
├── requirements.txt                  # Dependencias del proyecto
├── version                           # Versión del proyecto
└── README.md                         # Documentación del repositorio
```

## Tests

La carpeta `tests/` es el corazón del proyecto. Aquí se valida la calidad del software en distintos niveles.

### 1. Tests unitarios
Ubicados en `tests/units/`.

Estos tests verifican:

- lectura y escritura del almacenamiento JSON
- creación y eliminación de registros
- validaciones con Pydantic
- manejo de entradas inválidas
- comportamiento esperado de funciones aisladas

Ejemplos de validación:

- `_cargar_datos()` devuelve lista vacía si el archivo no existe
- `crear_comida()` genera IDs correctamente
- `eliminar_comida()` responde según el resultado real

### 2. Tests de integración
Ubicados en `tests/integrations/`.

Estos tests comprueban que la lógica principal de la app funciona en conjunto con la capa de acceso a datos y la interacción con la consola.

Se validan casos como:

- agregar una comida desde la lógica principal
- mostrar comidas
- eliminar una comida
- reintentos cuando los datos ingresados son inválidos

### 3. Tests end-to-end
Ubicados en `tests/end-to-end/`.

Estos tests simulan la ejecución real del programa desde la terminal y verifican el comportamiento de la CLI de extremo a extremo.

Se prueban flujos como:

- agregar una comida y salir
- ingresar una opción inválida y continuar con un flujo correcto
- validar que la salida por consola sea la esperada

## Ejecución de pruebas

Para correr la suite completa:

```bash
python -m pytest tests/ -v
```

O con el entorno virtual del proyecto:

```bash
.\.venv\Scripts\python.exe -m pytest tests/ -q
```

## Estado verificado

La suite actual de pruebas ha sido validada exitosamente:

```text
64 passed in 1.68s
```

Esto es una evidencia clara de que el proyecto está funcionando correctamente desde la perspectiva de calidad y automatización.

## Pipeline de CI/CD

La automatización está definida en `.github/workflows/build.yml` y representa una parte clave del proyecto.

### Trigger del workflow

El pipeline se dispara cuando ocurre alguno de estos eventos:

- `push` a la rama `main`
- `pull_request` hacia `main`
- creación de tags con formato `v*`

### Jobs del pipeline

#### 1. Job de pruebas

Este job ejecuta:

- checkout del repositorio
- instalación de Python 3.11
- instalación de dependencias
- ejecución de la suite completa de tests

La intención es impedir que cambios no validados lleguen a la siguiente etapa.

#### 2. Job de build

Solo se ejecuta si las pruebas pasan correctamente.

En esta etapa se:

- compila la aplicación con PyInstaller
- genera el ejecutable desde Windows y Ubuntu
- sube los binarios como artefactos de GitHub Actions

#### 3. Job de release

Se activa únicamente cuando se crea un tag de versión.

Su objetivo es:

- descargar los artefactos generados
- crear un GitHub Release
- publicar los binarios de la versión

## Relación entre tests y CI/CD

Este proyecto demuestra una buena práctica de desarrollo moderno:

- primero se prueban los cambios
- luego se compila el software
- después se genera el artefacto final
- finalmente se publica la versión si el proceso completo fue exitoso

De esta manera, la automatización no es solo un detalle adicional, sino una capa de seguridad que valida la calidad del proyecto antes de entregarlo.

## Tecnologías utilizadas

- Python
- Pytest
- Pydantic
- PyInstaller
- GitHub Actions

## Resumen

Este repositorio está pensado como una práctica enfocada en QA automatizada y pipeline de despliegue. Aunque la app demuestra una funcionalidad básica de restaurante, su verdadero valor está en la estructura del proyecto para garantizar calidad con pruebas y automatización continua.

El foco principal es este flujo:

```text
código -> pruebas -> validación -> build -> release
```

Y eso es precisamente lo que este proyecto busca enseñar y demostrar.
