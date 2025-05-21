import { useState, useEffect } from 'react';
import { customerService } from '../src/application/services/customerService';
import EntityTable from '../src/presentation/components/EntityTable';
import EntityForm from '../src/presentation/components/EntityForm';

export default function Customers() {
  const [customers, setCustomers] = useState([]);
  const [editingCustomer, setEditingCustomer] = useState(null);

  useEffect(() => {
    // Fetch customers (simplified, assuming a getAll endpoint exists)
    // For simplicity, we'll fetch one customer as an example
    customerService.getCustomer(1).then(customer => {
      if (customer) setCustomers([customer]);
    }).catch(() => setCustomers([]));
  }, []);

  const handleCreateOrUpdate = async (data) => {
    if (editingCustomer) {
      await customerService.updateCustomer(editingCustomer.id, data);
      setCustomers(customers.map(c => (c.id === editingCustomer.id ? { ...c, ...data } : c)));
      setEditingCustomer(null);
    } else {
      const newCustomer = await customerService.createCustomer(data);
      setCustomers([...customers, newCustomer]);
    }
  };

  const handleDelete = async (id) => {
    await customerService.deleteCustomer(id);
    setCustomers(customers.filter(c => c.id !== id));
  };

  const fields = [
    { name: 'nombre', label: 'Name', required: true },
    { name: 'apellido', label: 'Last Name', required: true },
    { name: 'direccion', label: 'Address' },
    { name: 'telefono', label: 'Phone' },
    { name: 'email', label: 'Email' },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Manage Customers</h1>
      <div className="mb-8">
      <EntityForm
        onSubmit={handleCreateOrUpdate}
        fields={fields}
        initialData={editingCustomer || {}}
      />
    </div>

      <EntityTable
        entities={customers}
        fields={['id', 'nombre', 'apellido', 'direccion', 'telefono', 'email']}
        onDelete={handleDelete}
      />
    </div>
  );
}