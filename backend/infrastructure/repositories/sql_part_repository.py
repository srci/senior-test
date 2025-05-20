from infrastructure.database.models.part_model import PartModel
from domain.entities.part import Part
from domain.repositories.part_repository import PartRepository
from sqlalchemy.orm import Session
from typing import List

class SQLPartRepository(PartRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, part: Part) -> Part:
        model = PartModel(
            numero_parte=part.numero_parte,
            descripcion=part.descripcion,
            stock_actual=part.stock_actual,
            costo=part.costo
        )
        self.session.add(model)
        self.session.commit()
        part.id = model.id_parte
        return part

    def get_by_id(self, id: int) -> Part:
        model = self.session.query(PartModel).filter_by(id_parte=id).first()
        if model:
            return Part(
                id=model.id_parte,
                numero_parte=model.numero_parte,
                descripcion=model.descripcion,
                stock_actual=model.stock_actual,
                costo=model.costo
            )
        return None

    def update(self, part: Part) -> Part:
        model = self.session.query(PartModel).filter_by(id_parte=part.id).first()
        if model:
            model.numero_parte = part.numero_parte
            model.descripcion = part.descripcion
            model.stock_actual = part.stock_actual
            model.costo = part.costo
            self.session.commit()
            return part
        return None

    def delete(self, id: int) -> None:
        model = self.session.query(PartModel).filter_by(id_parte=id).first()
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_all(self) -> List[Part]:
        models = self.session.query(PartModel).all()
        return [Part(
            id=model.id_parte,
            numero_parte=model.numero_parte,
            descripcion=model.descripcion,
            stock_actual=model.stock_actual,
            costo=model.costo
        ) for model in models]