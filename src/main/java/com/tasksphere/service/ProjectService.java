package com.tasksphere.service;

import com.tasksphere.model.Project;
import com.tasksphere.model.User;
import com.tasksphere.repository.ProjectRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProjectService {
    
    @Autowired
    private ProjectRepository projectRepository;
    
    public Project createProject(Project project) {
        return projectRepository.save(project);
    }
    
    public List<Project> getAllProjects() {
        return projectRepository.findAll();
    }
    
    public List<Project> getProjectsByUser(User user) {
        return projectRepository.findByCreatedBy(user);
    }
    
    public Optional<Project> getProjectById(Long id) {
        return projectRepository.findById(id);
    }
    
    public Project updateProject(Project project) {
        return projectRepository.save(project);
    }
    
    public void deleteProject(Long id) {
        projectRepository.deleteById(id);
    }
    
    public List<Project> searchProjectsByName(String name) {
        return projectRepository.findByNameContaining(name);
    }
    
    public List<Project> getProjectsByStatus(Project.ProjectStatus status) {
        return projectRepository.findByStatus(status);
    }
}
