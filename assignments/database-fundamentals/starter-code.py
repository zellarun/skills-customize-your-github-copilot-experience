from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)
    
    def __repr__(self):
        status = "✓" if self.completed else "○"
        return f"{status} [{self.id}] {self.title} (Due: {self.due_date})"

# Create database tables
Base.metadata.create_all(bind=engine)

# CRUD Operations
def create_task(title, description=None, due_date=None):
    """Create a new task in the database"""
    # TODO: Implement task creation
    pass

def get_all_tasks():
    """Retrieve all tasks from the database"""
    # TODO: Implement retrieval of all tasks
    pass

def get_task_by_id(task_id):
    """Retrieve a specific task by ID"""
    # TODO: Implement retrieval of task by ID
    pass

def update_task(task_id, **kwargs):
    """Update an existing task"""
    # TODO: Implement task update logic
    pass

def delete_task(task_id):
    """Delete a task by ID"""
    # TODO: Implement task deletion
    pass

def get_tasks_by_status(completed=False):
    """Filter tasks by completion status"""
    # TODO: Implement status filtering
    pass

def get_overdue_tasks():
    """Get tasks that are overdue"""
    # TODO: Implement overdue task retrieval
    pass

# CLI Menu
def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            # TODO: Implement add task
            pass
        elif choice == "2":
            # TODO: Implement view all tasks
            pass
        elif choice == "3":
            # TODO: Implement mark complete
            pass
        elif choice == "4":
            # TODO: Implement delete task
            pass
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
