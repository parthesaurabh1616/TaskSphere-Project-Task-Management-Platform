package com.tasksphere.controller;

import com.tasksphere.model.Project;
import com.tasksphere.model.User;
import com.tasksphere.service.ProjectService;
import com.tasksphere.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/projects")
@CrossOrigin(origins = "*")
public class ProjectController {
    
    @Autowired
    private ProjectService projectService;
    
    @Autowired
    private UserService userService;
    
    @PostMapping
    public ResponseEntity<Project> createProject(@RequestBody Project project, Authentication authentication) {
        String username = authentication.getName();
        User user = userService.getUserByUsername(username).orElse(null);
        if (user != null) {
            project.setCreatedBy(user);
            Project savedProject = projectService.createProject(project);
            return ResponseEntity.ok(savedProject);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @GetMapping
    public ResponseEntity<List<Project>> getAllProjects() {
        List<Project> projects = projectService.getAllProjects();
        return ResponseEntity.ok(projects);
    }
    
    @GetMapping("/my-projects")
    public ResponseEntity<List<Project>> getMyProjects(Authentication authentication) {
        String username = authentication.getName();
        User user = userService.getUserByUsername(username).orElse(null);
        if (user != null) {
            List<Project> projects = projectService.getProjectsByUser(user);
            return ResponseEntity.ok(projects);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Project> getProjectById(@PathVariable Long id) {
        Optional<Project> project = projectService.getProjectById(id);
        return project.map(ResponseEntity::ok).orElse(ResponseEntity.notFound().build());
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<Project> updateProject(@PathVariable Long id, @RequestBody Project projectDetails) {
        Optional<Project> project = projectService.getProjectById(id);
        if (project.isPresent()) {
            Project existingProject = project.get();
            existingProject.setName(projectDetails.getName());
            existingProject.setDescription(projectDetails.getDescription());
            existingProject.setStatus(projectDetails.getStatus());
            existingProject.setStartDate(projectDetails.getStartDate());
            existingProject.setEndDate(projectDetails.getEndDate());
            
            Project updatedProject = projectService.updateProject(existingProject);
            return ResponseEntity.ok(updatedProject);
        }
        return ResponseEntity.notFound().build();
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteProject(@PathVariable Long id) {
        projectService.deleteProject(id);
        return ResponseEntity.ok("Project deleted successfully");
    }
    
    @GetMapping("/search")
    public ResponseEntity<List<Project>> searchProjects(@RequestParam String name) {
        List<Project> projects = projectService.searchProjectsByName(name);
        return ResponseEntity.ok(projects);
    }
    
    @GetMapping("/status/{status}")
    public ResponseEntity<List<Project>> getProjectsByStatus(@PathVariable String status) {
        try {
            Project.ProjectStatus projectStatus = Project.ProjectStatus.valueOf(status.toUpperCase());
            List<Project> projects = projectService.getProjectsByStatus(projectStatus);
            return ResponseEntity.ok(projects);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().build();
        }
    }
}
