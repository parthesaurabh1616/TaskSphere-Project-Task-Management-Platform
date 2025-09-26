import React, { useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useTasks } from '../../contexts/TaskContext';
import { useProjects } from '../../contexts/ProjectContext';
import {
  Container,
  Grid,
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
  Chip,
  CircularProgress
} from '@mui/material';
import {
  Assignment as ProjectIcon,
  Task as TaskIcon,
  CheckCircle as CompletedIcon,
  Schedule as PendingIcon
} from '@mui/icons-material';

const Dashboard = () => {
  const { user } = useAuth();
  const { tasks, loading: tasksLoading, fetchMyTasks, fetchAssignedTasks } = useTasks();
  const { projects, loading: projectsLoading, fetchMyProjects } = useProjects();

  useEffect(() => {
    fetchMyTasks();
    fetchMyProjects();
  }, []);

  const completedTasks = tasks.filter(task => task.status === 'COMPLETED').length;
  const pendingTasks = tasks.filter(task => task.status !== 'COMPLETED').length;
  const activeProjects = projects.filter(project => project.status === 'ACTIVE').length;

  if (tasksLoading || projectsLoading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="400px">
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Welcome back, {user?.firstName}!
      </Typography>
      
      <Grid container spacing={3}>
        {/* Stats Cards */}
        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box display="flex" alignItems="center">
                <ProjectIcon color="primary" sx={{ mr: 2 }} />
                <Box>
                  <Typography color="textSecondary" gutterBottom>
                    My Projects
                  </Typography>
                  <Typography variant="h4">
                    {projects.length}
                  </Typography>
                </Box>
              </Box>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box display="flex" alignItems="center">
                <TaskIcon color="primary" sx={{ mr: 2 }} />
                <Box>
                  <Typography color="textSecondary" gutterBottom>
                    My Tasks
                  </Typography>
                  <Typography variant="h4">
                    {tasks.length}
                  </Typography>
                </Box>
              </Box>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box display="flex" alignItems="center">
                <CompletedIcon color="success" sx={{ mr: 2 }} />
                <Box>
                  <Typography color="textSecondary" gutterBottom>
                    Completed
                  </Typography>
                  <Typography variant="h4">
                    {completedTasks}
                  </Typography>
                </Box>
              </Box>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box display="flex" alignItems="center">
                <PendingIcon color="warning" sx={{ mr: 2 }} />
                <Box>
                  <Typography color="textSecondary" gutterBottom>
                    Pending
                  </Typography>
                  <Typography variant="h4">
                    {pendingTasks}
                  </Typography>
                </Box>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        {/* Recent Tasks */}
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Recent Tasks
            </Typography>
            {tasks.slice(0, 5).map((task) => (
              <Box key={task.id} sx={{ mb: 2, p: 2, border: '1px solid #e0e0e0', borderRadius: 1 }}>
                <Typography variant="subtitle1" gutterBottom>
                  {task.title}
                </Typography>
                <Box display="flex" gap={1}>
                  <Chip 
                    label={task.status} 
                    size="small" 
                    color={task.status === 'COMPLETED' ? 'success' : 'default'}
                  />
                  <Chip 
                    label={task.priority} 
                    size="small" 
                    color={task.priority === 'HIGH' ? 'error' : task.priority === 'MEDIUM' ? 'warning' : 'default'}
                  />
                </Box>
              </Box>
            ))}
            {tasks.length === 0 && (
              <Typography color="textSecondary">
                No tasks found. Create your first task!
              </Typography>
            )}
          </Paper>
        </Grid>

        {/* Recent Projects */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              My Projects
            </Typography>
            {projects.slice(0, 5).map((project) => (
              <Box key={project.id} sx={{ mb: 2, p: 2, border: '1px solid #e0e0e0', borderRadius: 1 }}>
                <Typography variant="subtitle1" gutterBottom>
                  {project.name}
                </Typography>
                <Chip 
                  label={project.status} 
                  size="small" 
                  color={project.status === 'ACTIVE' ? 'success' : 'default'}
                />
              </Box>
            ))}
            {projects.length === 0 && (
              <Typography color="textSecondary">
                No projects found. Create your first project!
              </Typography>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
