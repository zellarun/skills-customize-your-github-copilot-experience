from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# Define the Todo model
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

# In-memory storage (replace with database in production)
todos_db = {}
next_id = 1

@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo API"}

@app.get("/todos", response_model=List[Todo], tags=["Todos"])
def get_todos():
    """Get all todos"""
    return list(todos_db.values())

@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["Todos"])
def create_todo(todo: TodoCreate):
    """Create a new todo"""
    global next_id
    # TODO: Implement todo creation logic
    pass

@app.get("/todos/{todo_id}", response_model=Todo, tags=["Todos"])
def get_todo(todo_id: int):
    """Get a specific todo by ID"""
    # TODO: Implement logic to retrieve a todo by ID
    pass

@app.put("/todos/{todo_id}", response_model=Todo, tags=["Todos"])
def update_todo(todo_id: int, todo: TodoCreate):
    """Update an existing todo"""
    # TODO: Implement todo update logic
    pass

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Todos"])
def delete_todo(todo_id: int):
    """Delete a todo by ID"""
    # TODO: Implement todo deletion logic
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
