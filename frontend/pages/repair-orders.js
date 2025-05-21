import { useState, useEffect } from 'react';
import { repairOrderService } from '../src/application/services/repairOrderService';
import EntityTable from '../src/presentation/components/EntityTable';
import EntityForm from '../src/presentation/components/EntityForm';

export default function RepairOrders() {
  const [orders, setOrders] = useState([]);
  const [editingOrder, setEditingOrder] = useState(null);

  useEffect(() => {
    repairOrderService.getPendingRepairOrders().then(setOrders).catch(() => setOrders([]));
  }, []);

  const handleCreateOrUpdate = async (data) => {
    if (editingOrder) {
      await repairOrderService.updateRepairOrder(editingOrder.id, data);
      setOrders(orders.map(o => (o.id === editingOrder.id ? { ...o, ...data } : o)));
      setEditingOrder(null);
    } else {
      const newOrder = await repairOrderService.createRepairOrder(data);
      setOrders([...orders, newOrder]);
    }
  };

  const handleDelete = async (id) => {
    await repairOrderService.deleteRepairOrder(id);
    setOrders(orders.filter(o => o.id !== id));
  };

  const fields = [
    { name: 'id_vehiculo', label: 'Vehicle ID', type: 'number', required: true },
    { name: 'fecha_inicio', label: 'Start Date', type: 'date', required: true },
    { name: 'fecha_fin', label: 'End Date', type: 'date' },
    { name: 'estado', label: 'Status', required: true },
    { name: 'mano_de_obra', label: 'Labor Cost', type: 'number', required: true },
    { name: 'prioridad', label: 'Priority', type: 'number', required: true },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Manage Repair Orders</h1>
      <div className="mb-8">
      <EntityForm
        onSubmit={handleCreateOrUpdate}
        fields={fields}
        initialData={editingOrder || {}}
      />
      </div>
      <EntityTable
        entities={orders}
        fields={['id', 'id_vehiculo', 'fecha_inicio', 'estado', 'mano_de_obra', 'prioridad']}
        onDelete={handleDelete}
      />
    </div>
  );
}