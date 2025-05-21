import apiClient from '../../infrastructure/api/apiClient';
import { OrderDetail } from '../../domain/entities/orderDetail';

export const orderDetailService = {
  createOrderDetail: async (detail) => {
    const response = await apiClient.post('/order-details/', detail);
    return new OrderDetail(response.data);
  },
  getOrderDetail: async (id) => {
    const response = await apiClient.get(`/order-details/${id}`);
    return new OrderDetail(response.data);
  },
  updateOrderDetail: async (id, detail) => {
    const response = await apiClient.put(`/order-details/${id}`, detail);
    return new OrderDetail(response.data);
  },
  deleteOrderDetail: async (id) => {
    await apiClient.delete(`/order-details/${id}`);
  },
  getOrderDetailsByOrderId: async (orderId) => {
    const response = await apiClient.get(`/order-details/order/${orderId}`);
    return response.data.map(detail => new OrderDetail(detail));
  },
};