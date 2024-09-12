from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import analizador

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Modelo de datos para recibir el código C del cliente
class CodigoC(BaseModel):
    codigo: str

@app.post("/analizar")
async def analizar_codigo(codigo: CodigoC):
    # Llamar al analizador léxico actualizado para analizar el código recibido
    _, resultados, contador = analizador.analisis(codigo.codigo)

    # Devolver los resultados del análisis
    return {
        "resultados": resultados,
        "tokens_contados": contador
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lexer-back-2.onrender.com/"],  # Cambia a la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
