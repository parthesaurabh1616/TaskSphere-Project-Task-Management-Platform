package com.tasksphere.controller;

import com.tasksphere.model.Task;
import com.tasksphere.model.User;
import com.tasksphere.service.TaskService;
import com.tasksphere.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/tasks")
@CrossOrigin(origins = "*")
public class TaskController {
    
    @Autowired
    private TaskService taskService;
    
    @Autowired
    private UserService userService;
    
    @PostMapping
    public ResponseEntity<Task> createTask(@RequestBody Task task, Authentication authentication) {
        String username = authentication.getName();
        User user = userService.getUserByUsername(username).orElse(null);
        if (user != null) {
            task.setCreatedBy(user);
            Task savedTask = taskService.createTask(task);
            return ResponseEntity.ok(savedTask);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @GetMapping
    public ResponseEntity<List<Task>> getAllTasks() {
        List<Task> tasks = taskService.getAllTasks();
        return ResponseEntity.ok(tasks);
    }
    
    @GetMapping("/my-tasks")
    public ResponseEntity<List<Task>> getMyTasks(Authentication authentication) {
        String username = authentication.getName();
        User user = userService.getUserByUsername(username).orElse(null);
        if (user != null) {
            List<Task> tasks = taskService.getTasksByUser(user);
            return ResponseEntity.ok(tasks);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @GetMapping("/assigned-to-me")
    public ResponseEntity<List<Task>> getTasksAssignedToMe(Authentication authentication) {
        String username = authentication.getName();
        User user = userService.getUserByUsername(username).orElse(null);
        if (user != null) {
            List<Task> tasks = taskService.getTasksByAssignee(user);
            return ResponseEntity.ok(tasks);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Task> getTaskById(@PathVariable Long id) {
        Optional<Task> task = taskService.getTaskById(id);
        return task.map(ResponseEntity::ok).orElse(ResponseEntity.notFound().build());
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<Task> updateTask(@PathVariable Long id, @RequestBody Task taskDetails) {
        Optional<Task> task = taskService.getTaskById(id);
        if (task.isPresent()) {
            Task existingTask = task.get();
            existingTask.setTitle(taskDetails.getTitle());
            existingTask.setDescription(taskDetails.getDescription());
            existingTask.setStatus(taskDetails.getStatus());
            existingTask.setPriority(taskDetails.getPriority());
            existingTask.setDueDate(taskDetails.getDueDate());
            existingTask.setAssignee(taskDetails.getAssignee());
            
            Task updatedTask = taskService.updateTask(existingTask);
            return ResponseEntity.ok(updatedTask);
        }
        return ResponseEntity.notFound().build();
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteTask(@PathVariable Long id) {
        taskService.deleteTask(id);
        return ResponseEntity.ok("Task deleted successfully");
    }
    
    @GetMapping("/search")
    public ResponseEntity<List<Task>> searchTasks(@RequestParam String searchTerm) {
        List<Task> tasks = taskService.searchTasks(searchTerm);
        return ResponseEntity.ok(tasks);
    }
    
    @GetMapping("/status/{status}")
    public ResponseEntity<List<Task>> getTasksByStatus(@PathVariable String status) {
        try {
            Task.TaskStatus taskStatus = Task.TaskStatus.valueOf(status.toUpperCase());
            List<Task> tasks = taskService.getTasksByStatus(taskStatus);
            return ResponseEntity.ok(tasks);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    @GetMapping("/priority/{priority}")
    public ResponseEntity<List<Task>> getTasksByPriority(@PathVariable String priority) {
        try {
            Task.Priority taskPriority = Task.Priority.valueOf(priority.toUpperCase());
            List<Task> tasks = taskService.getTasksByPriority(taskPriority);
            return ResponseEntity.ok(tasks);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    @GetMapping("/assignee/{assigneeId}")
    public ResponseEntity<List<Task>> getTasksByAssignee(@PathVariable Long assigneeId) {
        List<Task> tasks = taskService.getTasksByAssigneeId(assigneeId);
        return ResponseEntity.ok(tasks);
    }
    
    @GetMapping("/project/{projectId}")
    public ResponseEntity<List<Task>> getTasksByProject(@PathVariable Long projectId) {
        List<Task> tasks = taskService.getTasksByProjectId(projectId);
        return ResponseEntity.ok(tasks);
    }
}
