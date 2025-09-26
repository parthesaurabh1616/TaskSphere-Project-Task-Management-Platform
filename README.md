# TaskSphere - Project & Task Management Platform

A full-stack web application for managing projects and tasks with secure user authentication, role-based access control, and collaborative features.

## 🚀 Features

- **User Authentication & Authorization**: JWT-based authentication with role-based access control (Admin, Manager, User)
- **Project Management**: Create, update, delete, and track projects with status management
- **Task Management**: Comprehensive task management with priority levels, status tracking, and assignment
- **Search & Filter**: Advanced search and filtering capabilities for tasks and projects
- **Responsive UI**: Modern, responsive user interface built with React and Material-UI
- **RESTful APIs**: Well-structured REST APIs with proper error handling and validation
- **Database Optimization**: Optimized database queries with Hibernate/JPA and indexing

## 🛠️ Tech Stack

### Backend
- **Java 17**
- **Spring Boot 3.2.0**
- **Spring Security** with JWT authentication
- **Spring Data JPA** with Hibernate
- **MySQL 8.0**
- **Maven** for dependency management
- **JUnit 5** for testing

### Frontend
- **React 18**
- **Material-UI (MUI)** for UI components
- **React Router** for navigation
- **Axios** for API calls
- **Context API** for state management

## 📋 Prerequisites

- Java 17 or higher
- Node.js 16 or higher
- MySQL 8.0 or higher
- Maven 3.6 or higher

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/parthesaurabh1616/TaskSphere-Project-Task-Management-Platform.git
cd TaskSphere-Project-Task-Management-Platform
```

### 2. Database Setup

1. Create a MySQL database named `tasksphere`
2. Update the database configuration in `src/main/resources/application.properties`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/tasksphere?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
spring.datasource.username=your_username
spring.datasource.password=your_password
```

### 3. Backend Setup

1. Navigate to the project root directory
2. Run the Spring Boot application:

```bash
mvn spring-boot:run
```

The backend will start on `http://localhost:8080`

### 4. Frontend Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

The frontend will start on `http://localhost:3000`

## 📚 API Documentation

### Authentication Endpoints

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### User Endpoints

- `GET /api/users` - Get all users (Admin/Manager only)
- `GET /api/users/{id}` - Get user by ID
- `GET /api/users/profile` - Get current user profile
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user (Admin only)

### Project Endpoints

- `GET /api/projects` - Get all projects
- `GET /api/projects/my-projects` - Get user's projects
- `GET /api/projects/{id}` - Get project by ID
- `POST /api/projects` - Create new project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project
- `GET /api/projects/search?name={name}` - Search projects by name
- `GET /api/projects/status/{status}` - Filter projects by status

### Task Endpoints

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/my-tasks` - Get user's created tasks
- `GET /api/tasks/assigned-to-me` - Get tasks assigned to user
- `GET /api/tasks/{id}` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `GET /api/tasks/search?searchTerm={term}` - Search tasks
- `GET /api/tasks/status/{status}` - Filter tasks by status
- `GET /api/tasks/priority/{priority}` - Filter tasks by priority
- `GET /api/tasks/assignee/{assigneeId}` - Get tasks by assignee
- `GET /api/tasks/project/{projectId}` - Get tasks by project

## 🏗️ Project Structure

```
TaskSphere/
├── src/
│   ├── main/
│   │   ├── java/com/tasksphere/
│   │   │   ├── controller/          # REST Controllers
│   │   │   ├── model/               # JPA Entities
│   │   │   ├── repository/          # Data Access Layer
│   │   │   ├── service/             # Business Logic
│   │   │   ├── security/            # Security Configuration
│   │   │   └── dto/                 # Data Transfer Objects
│   │   └── resources/
│   │       └── application.properties
│   └── test/                        # Test Classes
├── frontend/
│   ├── src/
│   │   ├── components/              # React Components
│   │   ├── contexts/                # React Context Providers
│   │   └── App.js                   # Main App Component
│   └── package.json
├── pom.xml                          # Maven Configuration
└── README.md
```

## 🔐 User Roles

- **ADMIN**: Full access to all features and user management
- **MANAGER**: Can manage projects and tasks, view all users
- **USER**: Can create and manage their own projects and tasks

## 🧪 Testing

Run the backend tests:

```bash
mvn test
```

Run the frontend tests:

```bash
cd frontend
npm test
```

## 🚀 Deployment

### Backend Deployment

1. Build the JAR file:
```bash
mvn clean package
```

2. Run the JAR file:
```bash
java -jar target/tasksphere-0.0.1-SNAPSHOT.jar
```

### Frontend Deployment

1. Build the production bundle:
```bash
cd frontend
npm run build
```

2. Serve the build folder using a web server like Nginx or Apache

## 📈 Performance Optimizations

- **Database Indexing**: Optimized database queries with proper indexing
- **Hibernate Optimization**: Efficient entity relationships and lazy loading
- **JWT Token Management**: Secure and efficient authentication
- **React Context**: Optimized state management with minimal re-renders

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Saurabh Parthe**
- GitHub: [@parthesaurabh1616](https://github.com/parthesaurabh1616)

## 🙏 Acknowledgments

- Spring Boot team for the excellent framework
- React team for the amazing frontend library
- Material-UI team for the beautiful components
- MySQL team for the robust database system
