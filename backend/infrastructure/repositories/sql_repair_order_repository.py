from infrastructure.database.models.repair_order_model import RepairOrderModel
from infrastructure.database.models.order_detail_model import OrderDetailModel
from domain.entities.repair_order import RepairOrder
from domain.entities.order_detail import OrderDetail
from domain.repositories.repair_order_repository import RepairOrderRepository
from sqlalchemy.orm import Session
from typing import List

class SQLRepairOrderRepository(RepairOrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, order: RepairOrder) -> RepairOrder:
        model = RepairOrderModel(
            id_vehiculo=order.id_vehiculo,
            fecha_inicio=order.fecha_inicio,
            fecha_fin=order.fecha_fin,
            estado=order.estado,
            mano_de_obra=order.mano_de_obra,
            prioridad=order.prioridad
        )
        self.session.add(model)
        self.session.commit()
        order.id = model.id_orden
        if order.details:
            for detail in order.details:
                detail_model = OrderDetailModel(
                    id_orden=order.id,
                    id_parte=detail.id_parte,
                    cantidad=detail.cantidad
                )
                self.session.add(detail_model)
            self.session.commit()
            for detail, detail_model in zip(order.details, self.session.query(OrderDetailModel).filter_by(id_orden=order.id).all()):
                detail.id = detail_model.id_detalle
        return order

    def get_by_id(self, id: int) -> RepairOrder:
        model = self.session.query(RepairOrderModel).filter_by(id_orden=id).first()
        if model:
            order = RepairOrder(
                id=model.id_orden,
                id_vehiculo=model.id_vehiculo,
                fecha_inicio=model.fecha_inicio,
                fecha_fin=model.fecha_fin,
                estado=model.estado,
                mano_de_obra=model.mano_de_obra,
                prioridad=model.prioridad,
                details=[]
            )
            details = self.session.query(OrderDetailModel).filter_by(id_orden=id).all()
            for detail_model in details:
                detail = OrderDetail(
                    id=detail_model.id_detalle,
                    id_orden=detail_model.id_orden,
                    id_parte=detail_model.id_parte,
                    cantidad=detail_model.cantidad
                )
                order.details.append(detail)
            return order
        return None

    def update(self, order: RepairOrder) -> RepairOrder:
        model = self.session.query(RepairOrderModel).filter_by(id_orden=order.id).first()
        if model:
            model.id_vehiculo = order.id_vehiculo
            model.fecha_inicio = order.fecha_inicio
            model.fecha_fin = order.fecha_fin
            model.estado = order.estado
            model.mano_de_obra = order.mano_de_obra
            model.prioridad = order.prioridad
            self.session.commit()
            # Los detalles se gestionan por separado
            return order
        return None

    def delete(self, id: int) -> None:
        self.session.query(OrderDetailModel).filter_by(id_orden=id).delete()
        model = self.session.query(RepairOrderModel).filter_by(id_orden=id).first()
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_pending_orders(self) -> List[RepairOrder]:
        models = self.session.query(RepairOrderModel).filter_by(estado='pendiente').all()
        orders = []
        for model in models:
            order = RepairOrder(
                id=model.id_orden,
                id_vehiculo=model.id_vehiculo,
                fecha_inicio=model.fecha_inicio,
                fecha_fin=model.fecha_fin,
                estado=model.estado,
                mano_de_obra=model.mano_de_obra,
                prioridad=model.prioridad,
                details=[]
            )
            details = self.session.query(OrderDetailModel).filter_by(id_orden=model.id_orden).all()
            for detail_model in details:
                detail = OrderDetail(
                    id=detail_model.id_detalle,
                    id_orden=detail_model.id_orden,
                    id_parte=detail_model.id_parte,
                    cantidad=detail_model.cantidad
                )
                order.details.append(detail)
            orders.append(order)
        return orders