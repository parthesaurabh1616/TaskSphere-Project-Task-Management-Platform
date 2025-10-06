package com.tasksphere.controller;

import com.tasksphere.dto.AuthRequest;
import com.tasksphere.dto.RegisterRequest;
import com.tasksphere.model.User;
import com.tasksphere.service.UserService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class AuthControllerTest {

    @Mock
    private UserService userService;

    @InjectMocks
    private AuthController authController;

    private User testUser;
    private AuthRequest authRequest;
    private RegisterRequest registerRequest;

    @BeforeEach
    void setUp() {
        testUser = new User();
        testUser.setId(1L);
        testUser.setUsername("testuser");
        testUser.setEmail("test@example.com");
        testUser.setFirstName("Test");
        testUser.setLastName("User");
        testUser.setRole(User.Role.USER);

        authRequest = new AuthRequest("testuser", "password");

        registerRequest = new RegisterRequest();
        registerRequest.setUsername("testuser");
        registerRequest.setEmail("test@example.com");
        registerRequest.setPassword("password");
        registerRequest.setFirstName("Test");
        registerRequest.setLastName("User");
    }

    @Test
    void testLogin_Success() {
        // Given
        when(userService.authenticateUser("testuser", "password")).thenReturn("jwt-token");
        when(userService.getUserByUsername("testuser")).thenReturn(Optional.of(testUser));

        // When
        ResponseEntity<?> response = authController.authenticateUser(authRequest);

        // Then
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
    }

    @Test
    void testLogin_InvalidCredentials() {
        // Given
        when(userService.authenticateUser("testuser", "wrongpassword"))
                .thenThrow(new RuntimeException("Invalid credentials"));

        // When
        ResponseEntity<?> response = authController.authenticateUser(authRequest);

        // Then
        assertEquals(HttpStatus.BAD_REQUEST, response.getStatusCode());
        assertEquals("Invalid username or password", response.getBody());
    }

    @Test
    void testRegister_Success() {
        // Given
        when(userService.registerUser(any(User.class))).thenReturn(testUser);

        // When
        ResponseEntity<?> response = authController.registerUser(registerRequest);

        // Then
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("User registered successfully", response.getBody());
    }

    @Test
    void testRegister_UsernameExists() {
        // Given
        when(userService.registerUser(any(User.class)))
                .thenThrow(new RuntimeException("Username is already taken!"));

        // When
        ResponseEntity<?> response = authController.registerUser(registerRequest);

        // Then
        assertEquals(HttpStatus.BAD_REQUEST, response.getStatusCode());
        assertEquals("Username is already taken!", response.getBody());
    }
}
