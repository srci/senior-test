import { useState, useEffect } from 'react';
import { vehicleService } from '../src/application/services/vehicleService';
import EntityTable from '../src/presentation/components/EntityTable';
import EntityForm from '../src/presentation/components/EntityForm';

export default function Vehicles() {
  const [vehicles, setVehicles] = useState([]);
  const [editingVehicle, setEditingVehicle] = useState(null);

  useEffect(() => {
    vehicleService.getVehicle(1).then(vehicle => {
      if (vehicle) setVehicles([vehicle]);
    }).catch(() => setVehicles([]));
  }, []);

  const handleCreateOrUpdate = async (data) => {
    if (editingVehicle) {
      await vehicleService.updateVehicle(editingVehicle.id, data);
      setVehicles(vehicles.map(v => (v.id === editingVehicle.id ? { ...v, ...data } : v)));
      setEditingVehicle(null);
    } else {
      const newVehicle = await vehicleService.createVehicle(data);
      setVehicles([...vehicles, newVehicle]);
    }
  };

  const handleDelete = async (id) => {
    await vehicleService.deleteVehicle(id);
    setVehicles(vehicles.filter(v => v.id !== id));
  };

  const fields = [
    { name: 'id_cliente', label: 'Customer ID', type: 'number', required: true },
    { name: 'marca', label: 'Brand', required: true },
    { name: 'modelo', label: 'Model', required: true },
    { name: 'año', label: 'Year', type: 'number' },
    { name: 'vin', label: 'VIN' },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Manage Vehicles</h1>
      <div className="mb-8">
      <EntityForm
        onSubmit={handleCreateOrUpdate}
        fields={fields}
        initialData={editingVehicle || {}}
      />
      </div>
      <EntityTable
        entities={vehicles}
        fields={['id', 'id_cliente', 'marca', 'modelo', 'año', 'vin']}
        onDelete={handleDelete}
      />
    </div>
  );
}