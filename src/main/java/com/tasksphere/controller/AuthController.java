package com.tasksphere.controller;

import com.tasksphere.dto.AuthRequest;
import com.tasksphere.dto.AuthResponse;
import com.tasksphere.dto.RegisterRequest;
import com.tasksphere.model.User;
import com.tasksphere.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class AuthController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping("/login")
    public ResponseEntity<?> authenticateUser(@Valid @RequestBody AuthRequest authRequest) {
        try {
            String token = userService.authenticateUser(authRequest.getUsername(), authRequest.getPassword());
            User user = userService.getUserByUsername(authRequest.getUsername()).orElse(null);
            
            AuthResponse response = new AuthResponse(token, user.getUsername(), user.getRole().name());
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Invalid username or password");
        }
    }
    
    @PostMapping("/register")
    public ResponseEntity<?> registerUser(@Valid @RequestBody RegisterRequest registerRequest) {
        try {
            User user = new User(
                registerRequest.getUsername(),
                registerRequest.getEmail(),
                registerRequest.getPassword(),
                registerRequest.getFirstName(),
                registerRequest.getLastName(),
                User.Role.USER
            );
            
            User savedUser = userService.registerUser(user);
            return ResponseEntity.ok("User registered successfully");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}
