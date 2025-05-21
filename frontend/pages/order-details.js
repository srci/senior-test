import { useState, useEffect } from 'react';
import { orderDetailService } from '../src/application/services/orderDetailService';
import EntityTable from '../src/presentation/components/EntityTable';
import EntityForm from '../src/presentation/components/EntityForm';

export default function OrderDetails() {
  const [details, setDetails] = useState([]);
  const [editingDetail, setEditingDetail] = useState(null);

  useEffect(() => {
    // Fetch details for a specific order (e.g., order ID 1)
    orderDetailService.getOrderDetailsByOrderId(1).then(setDetails).catch(() => setDetails([]));
  }, []);

  const handleCreateOrUpdate = async (data) => {
    if (editingDetail) {
      await orderDetailService.updateOrderDetail(editingDetail.id, data);
      setDetails(details.map(d => (d.id === editingDetail.id ? { ...d, ...data } : d)));
      setEditingDetail(null);
    } else {
      const newDetail = await orderDetailService.createOrderDetail(data);
      setDetails([...details, newDetail]);
    }
  };

  const handleDelete = async (id) => {
    await orderDetailService.deleteOrderDetail(id);
    setDetails(details.filter(d => d.id !== id));
  };

  const fields = [
    { name: 'id_orden', label: 'Order ID', type: 'number', required: true },
    { name: 'id_parte', label: 'Part ID', type: 'number', required: true },
    { name: 'cantidad', label: 'Quantity', type: 'number', required: true },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Manage Order Details</h1>
      <div className="mb-8">
      <EntityForm
        onSubmit={handleCreateOrUpdate}
        fields={fields}
        initialData={editingDetail || {}}
      />
      </div>
      <EntityTable
        entities={details}
        fields={['id', 'id_orden', 'id_parte', 'cantidad']}
        onDelete={handleDelete}
      />
    </div>
  );
}