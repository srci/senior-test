from infrastructure.database.models.customer_model import CustomerModel
from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository
from sqlalchemy.orm import Session

class SQLCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, customer: Customer) -> Customer:
        model = CustomerModel(
            nombre=customer.nombre,
            apellido=customer.apellido,
            direccion=customer.direccion,
            telefono=customer.telefono,
            email=customer.email
        )
        self.session.add(model)
        self.session.commit()
        customer.id = model.id_cliente
        return customer

    def get_by_id(self, id: int) -> Customer:
        model = self.session.query(CustomerModel).filter_by(id_cliente=id).first()
        if model:
            return Customer(
                id=model.id_cliente,
                nombre=model.nombre,
                apellido=model.apellido,
                direccion=model.direccion,
                telefono=model.telefono,
                email=model.email
            )
        return None

    def update(self, customer: Customer) -> Customer:
        model = self.session.query(CustomerModel).filter_by(id_cliente=customer.id).first()
        if model:
            model.nombre = customer.nombre
            model.apellido = customer.apellido
            model.direccion = customer.direccion
            model.telefono = customer.telefono
            model.email = customer.email
            self.session.commit()
            return customer
        return None

    def delete(self, id: int) -> None:
        model = self.session.query(CustomerModel).filter_by(id_cliente=id).first()
        if model:
            self.session.delete(model)
            self.session.commit()