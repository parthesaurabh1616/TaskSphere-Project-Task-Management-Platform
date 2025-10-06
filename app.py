import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json
from typing import Dict, List, Optional
import time

# Page Configuration
st.set_page_config(
    page_title="TaskSphere - Project Management Platform",
    page_icon="ðŸš€",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern Professional Design
st.markdown("""
<style>
    /* Modern Professional Theme - Blue & White */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        color: #1e293b;
    }
    
    /* Main Header */
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        text-shadow: 0 0 30px rgba(37, 99, 235, 0.3);
    }
    
    .sub-header {
        font-size: 1.3rem;
        font-weight: 400;
        text-align: center;
        color: #64748b;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #1e293b;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Professional Cards */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.1);
        text-align: center;
        margin: 1rem;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(37, 99, 235, 0.2);
        border-color: #2563eb;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #2563eb, #3b82f6, #1d4ed8);
    }
    
    .metric-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1.1rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-subtitle {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-top: 0.5rem;
    }
    
    /* Project Cards */
    .project-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.1);
        margin: 1rem 0;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .project-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(37, 99, 235, 0.2);
        border-color: #2563eb;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .project-description {
        color: #64748b;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    
    .project-status {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-active {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
    }
    
    .status-completed {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        color: white;
    }
    
    .status-pending {
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
    }
    
    /* Task Cards */
    .task-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.08);
        margin: 0.8rem 0;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .task-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.15);
        border-color: #2563eb;
    }
    
    .task-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .task-priority {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 15px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-right: 0.5rem;
    }
    
    .priority-high {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
    }
    
    .priority-medium {
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
    }
    
    .priority-low {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
    }
    
    /* Progress Bars */
    .progress-container {
        background: #e2e8f0;
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        font-weight: 600;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
        transform: translateY(-2px);
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    }
    
    .stSidebar .stSelectbox > div > div {
        background-color: #ffffff;
        color: #1e293b;
        border: 2px solid #2563eb;
        border-radius: 8px;
    }
    
    .stSidebar .stSelectbox label {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Form Elements */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #1e293b;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        padding: 8px;
    }
    
    .stTextInput label {
        color: #1e293b;
        font-weight: 600;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #ffffff;
        color: #1e293b;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        padding: 8px;
    }
    
    .stTextArea label {
        color: #1e293b;
        font-weight: 600;
    }
    
    .stDateInput > div > div > input {
        background-color: #ffffff;
        color: #1e293b;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        padding: 8px;
    }
    
    .stDateInput label {
        color: #1e293b;
        font-weight: 600;
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background-color: #f0fdf4;
        color: #166534;
        border: 1px solid #10b981;
        border-radius: 8px;
    }
    
    .stError {
        background-color: #fef2f2;
        color: #dc2626;
        border: 1px solid #ef4444;
        border-radius: 8px;
    }
    
    .stWarning {
        background-color: #fffbeb;
        color: #d97706;
        border: 1px solid #f59e0b;
        border-radius: 8px;
    }
    
    .stInfo {
        background-color: #eff6ff;
        color: #2563eb;
        border: 1px solid #3b82f6;
        border-radius: 8px;
    }
    
    /* Charts */
    .chart-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.1);
        border: 2px solid #e2e8f0;
        margin: 1rem 0;
    }
    
    /* Team Section */
    .team-member {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.08);
        margin: 0.5rem;
        border: 1px solid #e2e8f0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .team-member:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.15);
    }
    
    .member-avatar {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 auto 0.5rem;
    }
    
    .member-name {
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }
    
    .member-role {
        font-size: 0.8rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'projects' not in st.session_state:
    st.session_state.projects = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'team_members' not in st.session_state:
    st.session_state.team_members = []

# Sample data for demonstration
def initialize_sample_data():
    if not st.session_state.projects:
        st.session_state.projects = [
            {
                'id': 1,
                'name': 'E-Commerce Platform',
                'description': 'Build a modern e-commerce platform with React and Node.js',
                'status': 'Active',
                'progress': 75,
                'start_date': '2024-01-15',
                'end_date': '2024-03-15',
                'team_size': 5,
                'budget': 50000
            },
            {
                'id': 2,
                'name': 'Mobile App Development',
                'description': 'Create a cross-platform mobile app using React Native',
                'status': 'Active',
                'progress': 45,
                'start_date': '2024-02-01',
                'end_date': '2024-04-30',
                'team_size': 3,
                'budget': 35000
            },
            {
                'id': 3,
                'name': 'Data Analytics Dashboard',
                'description': 'Develop a comprehensive analytics dashboard with real-time data',
                'status': 'Completed',
                'progress': 100,
                'start_date': '2023-11-01',
                'end_date': '2024-01-31',
                'team_size': 4,
                'budget': 25000
            }
        ]
    
    if not st.session_state.tasks:
        st.session_state.tasks = [
            {
                'id': 1,
                'title': 'Design User Interface',
                'project': 'E-Commerce Platform',
                'assignee': 'John Doe',
                'priority': 'High',
                'status': 'In Progress',
                'due_date': '2024-02-15',
                'description': 'Create wireframes and mockups for the e-commerce platform'
            },
            {
                'id': 2,
                'title': 'Setup Database Schema',
                'project': 'E-Commerce Platform',
                'assignee': 'Jane Smith',
                'priority': 'High',
                'status': 'Completed',
                'due_date': '2024-01-30',
                'description': 'Design and implement the database structure'
            },
            {
                'id': 3,
                'title': 'Implement Authentication',
                'project': 'Mobile App Development',
                'assignee': 'Mike Johnson',
                'priority': 'Medium',
                'status': 'Pending',
                'due_date': '2024-02-20',
                'description': 'Add user authentication and authorization'
            },
            {
                'id': 4,
                'title': 'API Integration',
                'project': 'Data Analytics Dashboard',
                'assignee': 'Sarah Wilson',
                'priority': 'Low',
                'status': 'Completed',
                'due_date': '2024-01-15',
                'description': 'Connect dashboard to various data sources'
            }
        ]
    
    if not st.session_state.team_members:
        st.session_state.team_members = [
            {'name': 'John Doe', 'role': 'Frontend Developer', 'avatar': 'JD'},
            {'name': 'Jane Smith', 'role': 'Backend Developer', 'avatar': 'JS'},
            {'name': 'Mike Johnson', 'role': 'Mobile Developer', 'avatar': 'MJ'},
            {'name': 'Sarah Wilson', 'role': 'Data Analyst', 'avatar': 'SW'},
            {'name': 'David Brown', 'role': 'Project Manager', 'avatar': 'DB'}
        ]

# Initialize sample data
initialize_sample_data()

# Sidebar Navigation
st.sidebar.markdown("## ðŸš€ TaskSphere")
st.sidebar.markdown("---")

page = st.sidebar.selectbox(
    "Navigate",
    ["ðŸ“Š Dashboard", "ðŸ“ Projects", "âœ… Tasks", "ðŸ‘¥ Team", "ðŸ“ˆ Analytics", "âš™ï¸ Settings"]
)

# Dashboard Page
if page == "ðŸ“Š Dashboard":
    st.markdown('<h1 class="main-header">TaskSphere</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Professional Project Management Platform</p>', unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{len(st.session_state.projects)}</div>
            <div class="metric-label">Total Projects</div>
            <div class="metric-subtitle">{len([p for p in st.session_state.projects if p['status'] == 'Active'])} Active</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{len(st.session_state.tasks)}</div>
            <div class="metric-label">Total Tasks</div>
            <div class="metric-subtitle">{len([t for t in st.session_state.tasks if t['status'] == 'Completed'])} Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        completion_rate = (len([t for t in st.session_state.tasks if t['status'] == 'Completed']) / len(st.session_state.tasks) * 100) if st.session_state.tasks else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{completion_rate:.0f}%</div>
            <div class="metric-label">Completion Rate</div>
            <div class="metric-subtitle">Task Progress</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{len(st.session_state.team_members)}</div>
            <div class="metric-label">Team Members</div>
            <div class="metric-subtitle">Active Contributors</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts Section
    st.markdown('<h2 class="section-header">Project Overview</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project Status Chart
        status_counts = {}
        for project in st.session_state.projects:
            status = project['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        if status_counts:
            fig_status = px.pie(
                values=list(status_counts.values()),
                names=list(status_counts.keys()),
                title="Project Status Distribution",
                color_discrete_map={
                    'Active': '#2563eb',
                    'Completed': '#10b981',
                    'Pending': '#f59e0b'
                }
            )
            fig_status.update_layout(
                title_font_size=16,
                font=dict(size=12),
                showlegend=True,
                height=400
            )
            st.plotly_chart(fig_status, use_container_width=True)
    
    with col2:
        # Task Priority Chart
        priority_counts = {}
        for task in st.session_state.tasks:
            priority = task['priority']
            priority_counts[priority] = priority_counts.get(priority, 0) + 1
        
        if priority_counts:
            fig_priority = px.bar(
                x=list(priority_counts.keys()),
                y=list(priority_counts.values()),
                title="Task Priority Distribution",
                color=list(priority_counts.keys()),
                color_discrete_map={
                    'High': '#ef4444',
                    'Medium': '#f59e0b',
                    'Low': '#10b981'
                }
            )
            fig_priority.update_layout(
                title_font_size=16,
                font=dict(size=12),
                showlegend=False,
                height=400,
                xaxis_title="Priority Level",
                yaxis_title="Number of Tasks"
            )
            st.plotly_chart(fig_priority, use_container_width=True)
    
    # Recent Projects
    st.markdown('<h2 class="section-header">Recent Projects</h2>', unsafe_allow_html=True)
    
    for project in st.session_state.projects[:3]:
        status_class = f"status-{project['status'].lower()}"
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['name']}</div>
            <div class="project-description">{project['description']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="project-status {status_class}">{project['status']}</span>
                <span style="color: #64748b; font-size: 0.9rem;">{project['progress']}% Complete</span>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {project['progress']}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Projects Page
elif page == "ðŸ“ Projects":
    st.markdown('<h1 class="section-header">Project Management</h1>', unsafe_allow_html=True)
    
    # Add New Project
    with st.expander("âž• Add New Project", expanded=False):
        with st.form("add_project"):
            col1, col2 = st.columns(2)
            
            with col1:
                project_name = st.text_input("Project Name")
                project_description = st.text_area("Description")
                project_status = st.selectbox("Status", ["Active", "Pending", "Completed"])
            
            with col2:
                start_date = st.date_input("Start Date")
                end_date = st.date_input("End Date")
                team_size = st.number_input("Team Size", min_value=1, max_value=20)
                budget = st.number_input("Budget ($)", min_value=0)
            
            if st.form_submit_button("Add Project"):
                new_project = {
                    'id': len(st.session_state.projects) + 1,
                    'name': project_name,
                    'description': project_description,
                    'status': project_status,
                    'progress': 0,
                    'start_date': str(start_date),
                    'end_date': str(end_date),
                    'team_size': team_size,
                    'budget': budget
                }
                st.session_state.projects.append(new_project)
                st.success("Project added successfully!")
                st.rerun()
    
    # Display Projects
    st.markdown('<h2 class="section-header">All Projects</h2>', unsafe_allow_html=True)
    
    for project in st.session_state.projects:
        status_class = f"status-{project['status'].lower()}"
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['name']}</div>
            <div class="project-description">{project['description']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <span class="project-status {status_class}">{project['status']}</span>
                <span style="color: #64748b; font-size: 0.9rem;">{project['progress']}% Complete</span>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {project['progress']}%"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 1rem; font-size: 0.9rem; color: #64748b;">
                <span>ðŸ‘¥ {project['team_size']} members</span>
                <span>ðŸ’° </span>
                <span>ðŸ“… {project['start_date']} - {project['end_date']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Tasks Page
elif page == "âœ… Tasks":
    st.markdown('<h1 class="section-header">Task Management</h1>', unsafe_allow_html=True)
    
    # Add New Task
    with st.expander("âž• Add New Task", expanded=False):
        with st.form("add_task"):
            col1, col2 = st.columns(2)
            
            with col1:
                task_title = st.text_input("Task Title")
                task_project = st.selectbox("Project", [p['name'] for p in st.session_state.projects])
                task_assignee = st.selectbox("Assignee", [m['name'] for m in st.session_state.team_members])
                task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
            
            with col2:
                task_status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
                task_due_date = st.date_input("Due Date")
                task_description = st.text_area("Description")
            
            if st.form_submit_button("Add Task"):
                new_task = {
                    'id': len(st.session_state.tasks) + 1,
                    'title': task_title,
                    'project': task_project,
                    'assignee': task_assignee,
                    'priority': task_priority,
                    'status': task_status,
                    'due_date': str(task_due_date),
                    'description': task_description
                }
                st.session_state.tasks.append(new_task)
                st.success("Task added successfully!")
                st.rerun()
    
    # Display Tasks
    st.markdown('<h2 class="section-header">All Tasks</h2>', unsafe_allow_html=True)
    
    for task in st.session_state.tasks:
        priority_class = f"priority-{task['priority'].lower()}"
        st.markdown(f"""
        <div class="task-card">
            <div class="task-title">{task['title']}</div>
            <div style="color: #64748b; margin-bottom: 0.5rem;">{task['description']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span class="task-priority {priority_class}">{task['priority']}</span>
                    <span style="background: #e2e8f0; padding: 0.2rem 0.6rem; border-radius: 15px; font-size: 0.7rem; font-weight: 600; color: #64748b;">{task['status']}</span>
                </div>
                <span style="color: #64748b; font-size: 0.9rem;">ðŸ“… {task['due_date']}</span>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.9rem; color: #64748b;">
                <span>ðŸ“ {task['project']}</span> â€¢ <span>ðŸ‘¤ {task['assignee']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Team Page
elif page == "ðŸ‘¥ Team":
    st.markdown('<h1 class="section-header">Team Management</h1>', unsafe_allow_html=True)
    
    # Add New Team Member
    with st.expander("âž• Add Team Member", expanded=False):
        with st.form("add_member"):
            col1, col2 = st.columns(2)
            
            with col1:
                member_name = st.text_input("Full Name")
                member_role = st.selectbox("Role", ["Project Manager", "Frontend Developer", "Backend Developer", "Mobile Developer", "Data Analyst", "UI/UX Designer", "DevOps Engineer"])
            
            with col2:
                member_email = st.text_input("Email")
                member_phone = st.text_input("Phone")
            
            if st.form_submit_button("Add Member"):
                new_member = {
                    'name': member_name,
                    'role': member_role,
                    'email': member_email,
                    'phone': member_phone,
                    'avatar': ''.join([word[0] for word in member_name.split()])
                }
                st.session_state.team_members.append(new_member)
                st.success("Team member added successfully!")
                st.rerun()
    
    # Display Team Members
    st.markdown('<h2 class="section-header">Team Members</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, member in enumerate(st.session_state.team_members):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="team-member">
                <div class="member-avatar">{member['avatar']}</div>
                <div class="member-name">{member['name']}</div>
                <div class="member-role">{member['role']}</div>
            </div>
            """, unsafe_allow_html=True)

# Analytics Page
elif page == "ðŸ“ˆ Analytics":
    st.markdown('<h1 class="section-header">Analytics & Reports</h1>', unsafe_allow_html=True)
    
    # Project Progress Chart
    st.markdown('<h3 style="color: #1e293b; margin: 2rem 0 1rem;">Project Progress Overview</h3>', unsafe_allow_html=True)
    
    project_data = []
    for project in st.session_state.projects:
        project_data.append({
            'Project': project['name'],
            'Progress': project['progress'],
            'Status': project['status']
        })
    
    if project_data:
        df_projects = pd.DataFrame(project_data)
        fig_progress = px.bar(
            df_projects,
            x='Project',
            y='Progress',
            color='Status',
            title="Project Progress by Status",
            color_discrete_map={
                'Active': '#2563eb',
                'Completed': '#10b981',
                'Pending': '#f59e0b'
            }
        )
        fig_progress.update_layout(
            title_font_size=16,
            font=dict(size=12),
            height=400,
            xaxis_title="Project Name",
            yaxis_title="Progress (%)"
        )
        st.plotly_chart(fig_progress, use_container_width=True)
    
    # Task Distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3 style="color: #1e293b; margin: 2rem 0 1rem;">Task Status Distribution</h3>', unsafe_allow_html=True)
        
        task_status_counts = {}
        for task in st.session_state.tasks:
            status = task['status']
            task_status_counts[status] = task_status_counts.get(status, 0) + 1
        
        if task_status_counts:
            fig_task_status = px.pie(
                values=list(task_status_counts.values()),
                names=list(task_status_counts.keys()),
                title="Task Status Distribution",
                color_discrete_map={
                    'Completed': '#10b981',
                    'In Progress': '#2563eb',
                    'Pending': '#f59e0b'
                }
            )
            fig_task_status.update_layout(
                title_font_size=14,
                font=dict(size=11),
                height=350
            )
            st.plotly_chart(fig_task_status, use_container_width=True)
    
    with col2:
        st.markdown('<h3 style="color: #1e293b; margin: 2rem 0 1rem;">Team Workload</h3>', unsafe_allow_html=True)
        
        assignee_counts = {}
        for task in st.session_state.tasks:
            assignee = task['assignee']
            assignee_counts[assignee] = assignee_counts.get(assignee, 0) + 1
        
        if assignee_counts:
            fig_workload = px.bar(
                x=list(assignee_counts.keys()),
                y=list(assignee_counts.values()),
                title="Tasks per Team Member",
                color=list(assignee_counts.values()),
                color_continuous_scale="Blues"
            )
            fig_workload.update_layout(
                title_font_size=14,
                font=dict(size=11),
                height=350,
                xaxis_title="Team Member",
                yaxis_title="Number of Tasks",
                showlegend=False
            )
            st.plotly_chart(fig_workload, use_container_width=True)

# Settings Page
elif page == "âš™ï¸ Settings":
    st.markdown('<h1 class="section-header">Settings & Configuration</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ðŸŽ¨ Theme Settings")
        theme_option = st.selectbox("Choose Theme", ["Professional Blue", "Dark Mode", "Light Mode"])
        st.info(f"Current theme: {theme_option}")
        
        st.markdown("### ðŸ“§ Notification Settings")
        email_notifications = st.checkbox("Email Notifications", value=True)
        push_notifications = st.checkbox("Push Notifications", value=True)
        task_reminders = st.checkbox("Task Reminders", value=True)
    
    with col2:
        st.markdown("### ðŸ” Security Settings")
        two_factor_auth = st.checkbox("Two-Factor Authentication", value=False)
        session_timeout = st.selectbox("Session Timeout", ["15 minutes", "30 minutes", "1 hour", "2 hours"])
        
        st.markdown("### ðŸ“Š Data Management")
        auto_backup = st.checkbox("Automatic Backup", value=True)
        data_retention = st.selectbox("Data Retention Period", ["30 days", "90 days", "1 year", "Forever"])
    
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
    
    st.markdown("---")
    st.markdown("### ðŸ—‘ï¸ Danger Zone")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear All Data", type="secondary"):
            st.warning("This will permanently delete all projects, tasks, and team data. Are you sure?")
    
    with col2:
        if st.button("Export Data", type="secondary"):
            st.info("Data export feature coming soon!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p>ðŸš€ <strong>TaskSphere</strong> - Professional Project Management Platform</p>
    <p>Built with â¤ï¸ using Streamlit | Â© 2024 Saurabh Parthe</p>
</div>
""", unsafe_allow_html=True)
