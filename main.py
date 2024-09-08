from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import analizador

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Modelo de datos para recibir el código C del cliente
class CodigoC(BaseModel):
    codigo: str

# Ruta para analizar el código C
@app.post("/analizar")
async def analizar_codigo(codigo: CodigoC):
    # Aquí llamas a tu analizador léxico para analizar el código recibido
    _, resultados = analizador.analisis(codigo.codigo)

    # Devolver los resultados del análisis
    return {"resultados": resultados}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Cambia a la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)