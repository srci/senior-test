from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository

class CreateCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, nombre, apellido, direccion, telefono, email):
        customer = Customer(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, email=email)
        return self.repository.create(customer)

class GetCustomerByIdUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)

class UpdateCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer: Customer):
        return self.repository.update(customer)

class DeleteCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)