from infrastructure.database.models.order_detail_model import OrderDetailModel
from domain.entities.order_detail import OrderDetail
from domain.repositories.order_detail_repository import OrderDetailRepository
from sqlalchemy.orm import Session
from typing import List

class SQLOrderDetailRepository(OrderDetailRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, detail: OrderDetail) -> OrderDetail:
        model = OrderDetailModel(
            id_orden=detail.id_orden,
            id_parte=detail.id_parte,
            cantidad=detail.cantidad
        )
        self.session.add(model)
        self.session.commit()
        detail.id = model.id_detalle
        return detail

    def get_by_id(self, id: int) -> OrderDetail:
        model = self.session.query(OrderDetailModel).filter_by(id_detalle=id).first()
        if model:
            return OrderDetail(
                id=model.id_detalle,
                id_orden=model.id_orden,
                id_parte=model.id_parte,
                cantidad=model.cantidad
            )
        return None

    def update(self, detail: OrderDetail) -> OrderDetail:
        model = self.session.query(OrderDetailModel).filter_by(id_detalle=detail.id).first()
        if model:
            model.id_orden = detail.id_orden
            model.id_parte = detail.id_parte
            model.cantidad = detail.cantidad
            self.session.commit()
            return detail
        return None

    def delete(self, id: int) -> None:
        model = self.session.query(OrderDetailModel).filter_by(id_detalle=id).first()
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_by_order_id(self, order_id: int) -> List[OrderDetail]:
        models = self.session.query(OrderDetailModel).filter_by(id_orden=order_id).all()
        return [OrderDetail(
            id=model.id_detalle,
            id_orden=model.id_orden,
            id_parte=model.id_parte,
            cantidad=model.cantidad
        ) for model in models]