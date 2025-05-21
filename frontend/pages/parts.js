import { useState, useEffect } from 'react';
import { partService } from '../src/application/services/partService';
import EntityTable from '../src/presentation/components/EntityTable';
import EntityForm from '../src/presentation/components/EntityForm';

export default function Parts() {
  const [parts, setParts] = useState([]);
  const [editingPart, setEditingPart] = useState(null);

  useEffect(() => {
    partService.getAllParts().then(setParts).catch(() => setParts([]));
  }, []);

  const handleCreateOrUpdate = async (data) => {
    if (editingPart) {
      await partService.updatePart(editingPart.id, data);
      setParts(parts.map(p => (p.id === editingPart.id ? { ...p, ...data } : p)));
      setEditingPart(null);
    } else {
      const newPart = await partService.createPart(data);
      setParts([...parts, newPart]);
    }
  };

  const handleDelete = async (id) => {
    await partService.deletePart(id);
    setParts(parts.filter(p => p.id !== id));
  };

  const fields = [
    { name: 'numero_parte', label: 'Part Number', required: true },
    { name: 'descripcion', label: 'Description', required: true },
    { name: 'stock_actual', label: 'Stock', type: 'number', required: true },
    { name: 'costo', label: 'Cost', type: 'number', required: true },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Manage Parts</h1>
      <div className="mb-8">
      <EntityForm
        onSubmit={handleCreateOrUpdate}
        fields={fields}
        initialData={editingPart || {}}
      />
      </div>
      <EntityTable
        entities={parts}
        fields={['id', 'numero_parte', 'descripcion', 'stock_actual', 'costo']}
        onDelete={handleDelete}
      />
    </div>
  );
}