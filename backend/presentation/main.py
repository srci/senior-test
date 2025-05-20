# presentation/main.py
from fastapi import FastAPI
from presentation.api import customer_controller, vehicle_controller, part_controller, repair_order_controller, order_detail_controller, optimization_controller

app = FastAPI()
app.include_router(customer_controller.router)
app.include_router(vehicle_controller.router)
app.include_router(part_controller.router)
app.include_router(repair_order_controller.router)
app.include_router(order_detail_controller.router)
app.include_router(optimization_controller.router)