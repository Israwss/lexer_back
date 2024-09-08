# Lexer C - Backend (FastAPI)

Este es el backend de la aplicación Lexer C, construido con FastAPI. Procesa el código en C que se envía desde el frontend y devuelve el resultado del análisis léxico.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-repositorio/lexer-c-backend.git
2. Ve al directorio del proyecto:
   ```bash

   cd lexer-c-backend
3. Crea un entorno virtual (opcional pero recomendado):
   ```bash

   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
4. Instala las dependencias:
   ```bash

   pip install -r requirements.txt

5. Si no tienes el archivo requirements.txt, puedes crear uno con el siguiente contenido:
   ```bash

   fastapi
   uvicorn
   pydantic

6. Uso

Inicia el servidor FastAPI con Uvicorn:
    ```bash
    
    uvicorn main:app --reload

El servidor estará corriendo en http://127.0.0.1:8000. Puedes ver la documentación de la API en http://127.0.0.1:8000/docs.

Estructura del proyecto

    main.py: Archivo principal que contiene las rutas de la API y la lógica para procesar el código en C.
    lexer.py: Contiene el código del analizador léxico que procesa el código en C.
    requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.

Conectar con el Frontend

Asegúrate de que el frontend (Next.js) esté corriendo en http://localhost:3000 y que haga solicitudes al backend en http://127.0.0.1:8000.

