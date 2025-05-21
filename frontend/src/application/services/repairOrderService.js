import apiClient from '../../infrastructure/api/apiClient';
import { RepairOrder } from '../../domain/entities/repairOrder';

export const repairOrderService = {
  createRepairOrder: async (order) => {
    const response = await apiClient.post('/repair-orders/', order);
    return new RepairOrder(response.data);
  },
  getRepairOrder: async (id) => {
    const response = await apiClient.get(`/repair-orders/${id}`);
    return new RepairOrder(response.data);
  },
  updateRepairOrder: async (id, order) => {
    const response = await apiClient.put(`/repair-orders/${id}`, order);
    return new RepairOrder(response.data);
  },
  deleteRepairOrder: async (id) => {
    await apiClient.delete(`/repair-orders/${id}`);
  },
  getPendingRepairOrders: async () => {
    const response = await apiClient.get('/repair-orders/pending/');
    return response.data.map(order => new RepairOrder(order));
  },
};