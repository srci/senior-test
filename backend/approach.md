# AutoPartsPro Backend Documentation

## Overview

The AutoPartsPro backend is built with FastAPI and MySQL, following Clean Architecture principles to ensure maintainability and separation of concerns. The system supports CRUD operations for:
- Customers
- Vehicles
- Parts
- Repair Orders
- Order Details

Additionally, it includes an optimization endpoint to select repair orders that maximize priority while respecting inventory constraints. The codebase is organized into layers (domain, application, infrastructure, and presentation) to facilitate testing and future extensions.

## API Documentation

The API is automatically documented using FastAPI's built-in Swagger UI, accessible at `/docs` when the server is running. Below is a detailed description of the endpoints, grouped by entity and functionality, as implemented in the controllers (`presentation/api/`).

## Optimization Approach

The optimization endpoint (`GET /optimize/`) addresses the business challenge of selecting repair orders to maximize value (priority) while respecting inventory constraints. The approach implemented is a greedy algorithm, chosen for its simplicity and effectiveness given the scope of the technical test.

### Objective

Select a subset of pending repair orders to maximize the total priority (a field in `RepairOrder`) while ensuring the required parts are available in the inventory.

### Algorithm

1. **Retrieve Pending Orders**
   - Fetch all repair orders with `estado = 'pendiente'` using `GetPendingRepairOrdersUseCase`
   - Each order includes its associated details (parts and quantities required)

2. **Retrieve Inventory**
   - Fetch all parts from the inventory using `GetAllPartsUseCase`
   - Create a dictionary mapping part IDs to their current stock (`stock_actual`)

3. **Sort Orders by Priority**
   - Sort the pending orders in descending order of their `prioridad` field

4. **Select Orders**
   - Iterate through the sorted orders
   - For each order, check if all required parts (from `OrderDetail`) are available in sufficient quantities (`can_fulfill_order`)
   - If the order can be fulfilled:
     - Add it to the selected list
     - Update the stock by subtracting the used quantities (`update_stock`)
   - If the order cannot be fulfilled due to insufficient stock, skip it

5. **Return Selected Orders**
   - Return the list of selected orders

### Implementation Details

- The logic is encapsulated in `OptimizeRepairOrdersUseCase` (`application/use_cases/optimization_use_case.py`)
- The `can_fulfill_order` method checks if the stock for each part in the order's details is sufficient
- The `update_stock` method simulates inventory reduction (in-memory) to ensure subsequent orders respect the remaining stock
- The algorithm does not modify the actual database stock, as this is typically a decision point for confirmation in a real system

### Assumptions

- The `prioridad` field in `RepairOrder` represents the value to maximize (e.g., profit or urgency)
- All orders are independent, and no additional constraints (e.g., time, labor availability) are considered
- The inventory stock (`stock_actual`) is assumed to be up-to-date and non-negative

### Limitations

- The greedy approach may not guarantee the globally optimal solution (e.g., selecting a low-priority order might allow more orders to be fulfilled overall)
- For a globally optimal solution, a more complex algorithm like dynamic programming or integer linear programming could be used, but it was deemed overkill for this test
- The algorithm assumes sufficient data (pending orders and parts) exist in the database

### Extensibility

- The approach can be extended to consider additional constraints (e.g., labor hours, deadlines) by modifying `can_fulfill_order`
- If a different optimization criterion is needed (e.g., maximize profit instead of priority), the sorting key can be adjusted
- This optimization approach is implemented in `optimization_controller.py` and `optimization_use_case.py`, ensuring modularity and alignment with Clean Architecture

## Notes

- **API Documentation**: The Swagger UI at `/docs` provides an interactive interface to test all endpoints
- This document serves as a static reference for the API and optimization approach