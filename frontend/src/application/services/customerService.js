import apiClient from '../../infrastructure/api/apiClient';
import { Customer } from '../../domain/entities/customer';

export const customerService = {
  createCustomer: async (customer) => {
    const response = await apiClient.post('/customers/', customer);
    return new Customer(response.data);
  },
  getCustomer: async (id) => {
    const response = await apiClient.get(`/customers/${id}`);
    return new Customer(response.data);
  },
  updateCustomer: async (id, customer) => {
    const response = await apiClient.put(`/customers/${id}`, customer);
    return new Customer(response.data);
  },
  deleteCustomer: async (id) => {
    await apiClient.delete(`/customers/${id}`);
  },
};