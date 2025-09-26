import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const ProjectContext = createContext();

export const useProjects = () => {
  const context = useContext(ProjectContext);
  if (!context) {
    throw new Error('useProjects must be used within a ProjectProvider');
  }
  return context;
};

export const ProjectProvider = ({ children }) => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchProjects = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/projects');
      setProjects(response.data);
    } catch (error) {
      console.error('Error fetching projects:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchMyProjects = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/projects/my-projects');
      setProjects(response.data);
    } catch (error) {
      console.error('Error fetching my projects:', error);
    } finally {
      setLoading(false);
    }
  };

  const createProject = async (projectData) => {
    try {
      const response = await axios.post('/api/projects', projectData);
      setProjects(prev => [...prev, response.data]);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to create project' };
    }
  };

  const updateProject = async (id, projectData) => {
    try {
      const response = await axios.put(`/api/projects/${id}`, projectData);
      setProjects(prev => prev.map(project => project.id === id ? response.data : project));
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to update project' };
    }
  };

  const deleteProject = async (id) => {
    try {
      await axios.delete(`/api/projects/${id}`);
      setProjects(prev => prev.filter(project => project.id !== id));
      return { success: true };
    } catch (error) {
      return { success: false, error: error.response?.data || 'Failed to delete project' };
    }
  };

  const searchProjects = async (name) => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/projects/search?name=${name}`);
      setProjects(response.data);
    } catch (error) {
      console.error('Error searching projects:', error);
    } finally {
      setLoading(false);
    }
  };

  const filterProjectsByStatus = async (status) => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/projects/status/${status}`);
      setProjects(response.data);
    } catch (error) {
      console.error('Error filtering projects by status:', error);
    } finally {
      setLoading(false);
    }
  };

  const value = {
    projects,
    loading,
    fetchProjects,
    fetchMyProjects,
    createProject,
    updateProject,
    deleteProject,
    searchProjects,
    filterProjectsByStatus
  };

  return (
    <ProjectContext.Provider value={value}>
      {children}
    </ProjectContext.Provider>
  );
};
