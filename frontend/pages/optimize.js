import { useState, useEffect } from 'react';
import { optimizationService } from '../src/application/services/optimizationService';
import OptimizationResults from '../src/presentation/components/OptimizationResults';

export default function Optimize() {
  const [orders, setOrders] = useState([]);

  const handleOptimize = async () => {
    const optimizedOrders = await optimizationService.optimizeRepairOrders();
    setOrders(optimizedOrders);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Optimize Repair Orders</h1>
      <button
        onClick={handleOptimize}
        className="bg-green-500 text-white px-4 py-2 rounded mb-4"
      >
        Run Optimization
      </button>
      <OptimizationResults orders={orders} />
    </div>
  );
}