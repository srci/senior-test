import apiClient from '../../infrastructure/api/apiClient';
import { RepairOrder } from '../../domain/entities/repairOrder';

export const optimizationService = {
  optimizeRepairOrders: async () => {
    const response = await apiClient.get('/optimize/');
    return response.data.map(order => new RepairOrder(order));
  },
};