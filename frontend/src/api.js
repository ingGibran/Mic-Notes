import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
});

export const login = async (username, password) => {
    const response = await api.post('/usuarios/iniciar_sesion', { username, password });
    return response.data;
};

export const register = async (username, password) => {
    const response = await api.post('/usuarios/crear', { username, password });
    return response.data;
};

export const getNotes = async (userId) => {
    const response = await api.get(`/notas/?id_usuario=${userId}`);
    return response.data;
};

export const createNote = async (noteData) => {
    const response = await api.post('/notas/', noteData);
    return response.data;
};

export const updateNote = async (noteData) => {
    const response = await api.patch('/notas/', noteData);
    return response.data;
};

export const deleteNote = async (noteId) => {
    const response = await api.delete(`/notas/?id_nota=${noteId}`);
    return response.data;
};

export default api;
