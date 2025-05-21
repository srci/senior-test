# presentation/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importa CORSMiddleware
from presentation.api import customer_controller, vehicle_controller, part_controller, repair_order_controller, order_detail_controller, optimization_controller

app = FastAPI()

# --- Configuración de CORS ---
# Define los orígenes (dominios/puertos) que tienen permitido acceder a tu API.
# Es crucial incluir el origen de tu aplicación Next.js.
origins = [
    "http://localhost",
    "http://localhost:3000",  # <--- Este es el puerto donde Next.js suele correr
    # Si tu Next.js corre en otro puerto (ej. 3001), añádelo aquí:
    # "http://localhost:3001",
    # Cuando despliegues tu frontend, también deberás añadir su dominio aquí:
    # "https://tu-dominio-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Permite los orígenes especificados
    allow_credentials=True,         # Permite el envío de cookies y credenciales
    allow_methods=["*"],            # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Permite todas las cabeceras en las solicitudes
)
# --- Fin de la configuración de CORS ---

app.include_router(customer_controller.router)
app.include_router(vehicle_controller.router)
app.include_router(part_controller.router)
app.include_router(repair_order_controller.router)
app.include_router(order_detail_controller.router)
app.include_router(optimization_controller.router)