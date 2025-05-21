import apiClient from '../../infrastructure/api/apiClient';
import { Vehicle } from '../../domain/entities/vehicle';

export const vehicleService = {
  createVehicle: async (vehicle) => {
    const response = await apiClient.post('/vehicles/', vehicle);
    return new Vehicle(response.data);
  },
  getVehicle: async (id) => {
    const response = await apiClient.get(`/vehicles/${id}`);
    return new Vehicle(response.data);
  },
  updateVehicle: async (id, vehicle) => {
    const response = await apiClient.put(`/vehicles/${id}`, vehicle);
    return new Vehicle(response.data);
  },
  deleteVehicle: async (id) => {
    await apiClient.delete(`/vehicles/${id}`);
  },
};