package com.tasksphere.repository;

import com.tasksphere.model.Project;
import com.tasksphere.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProjectRepository extends JpaRepository<Project, Long> {
    List<Project> findByCreatedBy(User createdBy);
    
    @Query("SELECT p FROM Project p WHERE p.name LIKE %:name%")
    List<Project> findByNameContaining(@Param("name") String name);
    
    @Query("SELECT p FROM Project p WHERE p.status = :status")
    List<Project> findByStatus(@Param("status") Project.ProjectStatus status);
}
