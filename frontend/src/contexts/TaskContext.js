import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const TaskContext = createContext();

export const useTasks = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTasks must be used within a TaskProvider');
  }
  return context;
};

export const TaskProvider = ({ children }) => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchTasks = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/tasks');
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchMyTasks = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/tasks/my-tasks');
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching my tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchAssignedTasks = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/tasks/assigned-to-me');
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching assigned tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (taskData) => {
    try {
      const response = await axios.post('/api/tasks', taskData);
      setTasks(prev => [...prev, response.data]);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to create task' };
    }
  };

  const updateTask = async (id, taskData) => {
    try {
      const response = await axios.put(`/api/tasks/${id}`, taskData);
      setTasks(prev => prev.map(task => task.id === id ? response.data : task));
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to update task' };
    }
  };

  const deleteTask = async (id) => {
    try {
      await axios.delete(`/api/tasks/${id}`);
      setTasks(prev => prev.filter(task => task.id !== id));
      return { success: true };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to delete task' };
    }
  };

  const searchTasks = async (searchTerm) => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/tasks/search?searchTerm=${searchTerm}`);
      setTasks(response.data);
    } catch (error) {
      console.error('Error searching tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const filterTasksByStatus = async (status) => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/tasks/status/${status}`);
      setTasks(response.data);
    } catch (error) {
      console.error('Error filtering tasks by status:', error);
    } finally {
      setLoading(false);
    }
  };

  const filterTasksByPriority = async (priority) => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/tasks/priority/${priority}`);
      setTasks(response.data);
    } catch (error) {
      console.error('Error filtering tasks by priority:', error);
    } finally {
      setLoading(false);
    }
  };

  const value = {
    tasks,
    loading,
    fetchTasks,
    fetchMyTasks,
    fetchAssignedTasks,
    createTask,
    updateTask,
    deleteTask,
    searchTasks,
    filterTasksByStatus,
    filterTasksByPriority
  };

  return (
    <TaskContext.Provider value={value}>
      {children}
    </TaskContext.Provider>
  );
};
