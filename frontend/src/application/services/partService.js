import apiClient from '../../infrastructure/api/apiClient';
import { Part } from '../../domain/entities/part';

export const partService = {
  createPart: async (part) => {
    const response = await apiClient.post('/parts/', part);
    return new Part(response.data);
  },
  getPart: async (id) => {
    const response = await apiClient.get(`/parts/${id}`);
    return new Part(response.data);
  },
  updatePart: async (id, part) => {
    const response = await apiClient.put(`/parts/${id}`, part);
    return new Part(response.data);
  },
  deletePart: async (id) => {
    await apiClient.delete(`/parts/${id}`);
  },
  getAllParts: async () => {
    const response = await apiClient.get('/parts/');
    return response.data.map(part => new Part(part));
  },
};