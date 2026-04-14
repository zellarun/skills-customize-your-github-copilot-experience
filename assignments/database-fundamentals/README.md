# 📘 Assignment: Database Fundamentals with SQLAlchemy and SQLite

## 🎯 Objective

Build a task management application that persists data to a SQLite database using SQLAlchemy ORM. You'll learn database design, CRUD operations, relationships, and how to structure data for long-term storage.

## 📝 Tasks

### 🛠️ Set Up Database & Models

#### Description

Create a SQLite database with a Task model using SQLAlchemy. Define the data structure with appropriate fields and constraints. Establish the database connection and set up the session management for all database operations.

#### Requirements

Completed program should:

- Define a Task model with fields: id, title, description, due_date, completed status
- Create database file using SQLAlchemy engine and session
- Use appropriate data types and constraints (e.g., String, Date, Boolean)
- Initialize an empty database with proper schema
- Prevent duplicate schema creation on repeated runs


### 🛠️ Implement CRUD Operations

#### Description

Build functions to Create, Read, Update, and Delete tasks from the database. Implement data validation and error handling to ensure database integrity. Provide a simple interface for users to interact with tasks through the command line.

#### Requirements

Completed program should:

- **Create**: Add new tasks to the database with required fields
- **Read**: Retrieve all tasks, find tasks by ID, filter by completion status
- **Update**: Modify existing task properties (title, due_date, completed)
- **Delete**: Remove tasks from the database by ID
- Handle errors gracefully (e.g., invalid ID, database connection issues)
- Display success/error messages to the user


### 🛠️ (Optional) Query Filtering & Relationships

#### Description

Add advanced filtering capabilities and optional relationships. Enable users to query tasks by due date, priority, or other criteria. Optionally introduce a User model and create one-to-many relationships between users and tasks.

#### Requirements

Completed program should:

- Filter tasks by due date range (due today, overdue, upcoming)
- Sort tasks by completion status or due date
- (Optional) Create a User model and associate tasks with users
- (Optional) Query tasks belonging to a specific user
- Use SQLAlchemy relationships to navigate between related objects
