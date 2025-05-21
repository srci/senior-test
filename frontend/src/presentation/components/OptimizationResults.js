export default function OptimizationResults({ orders }) {
    return (
      <div>
        <h2 className="text-xl font-bold mb-4">Optimized Repair Orders</h2>
        <table className="w-full border-collapse border">
          <thead>
            <tr>
              <th className="border p-2">ID</th>
              <th className="border p-2">Vehicle ID</th>
              <th className="border p-2">Start Date</th>
              <th className="border p-2">Status</th>
              <th className="border p-2">Labor Cost</th>
              <th className="border p-2">Priority</th>
            </tr>
          </thead>
          <tbody>
            {orders.map(order => (
              <tr key={order.id}>
                <td className="border p-2">{order.id}</td>
                <td className="border p-2">{order.id_vehiculo}</td>
                <td className="border p-2">{order.fecha_inicio}</td>
                <td className="border p-2">{order.estado}</td>
                <td className="border p-2">{order.mano_de_obra}</td>
                <td className="border p-2">{order.prioridad}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }