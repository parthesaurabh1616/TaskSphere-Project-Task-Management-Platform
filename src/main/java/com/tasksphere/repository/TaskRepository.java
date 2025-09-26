package com.tasksphere.repository;

import com.tasksphere.model.Task;
import com.tasksphere.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface TaskRepository extends JpaRepository<Task, Long> {
    List<Task> findByAssignee(User assignee);
    List<Task> findByCreatedBy(User createdBy);
    
    @Query("SELECT t FROM Task t WHERE t.title LIKE %:title% OR t.description LIKE %:description%")
    List<Task> findByTitleOrDescriptionContaining(@Param("title") String title, @Param("description") String description);
    
    @Query("SELECT t FROM Task t WHERE t.status = :status")
    List<Task> findByStatus(@Param("status") Task.TaskStatus status);
    
    @Query("SELECT t FROM Task t WHERE t.priority = :priority")
    List<Task> findByPriority(@Param("priority") Task.Priority priority);
    
    @Query("SELECT t FROM Task t WHERE t.assignee.id = :assigneeId")
    List<Task> findByAssigneeId(@Param("assigneeId") Long assigneeId);
    
    @Query("SELECT t FROM Task t WHERE t.project.id = :projectId")
    List<Task> findByProjectId(@Param("projectId") Long projectId);
}
