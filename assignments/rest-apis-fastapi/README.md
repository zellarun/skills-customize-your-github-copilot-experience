# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework. You'll learn how to create endpoints, handle HTTP requests and responses, validate data, and deploy a web service that can be consumed by other applications.

## 📝 Tasks

### 🛠️ Create a Basic REST API

#### Description

Develop a REST API for a simple todo application using FastAPI. The API should support basic CRUD operations (Create, Read, Update, Delete) for managing todo items. Implement proper HTTP methods, response status codes, and data validation.

#### Requirements

Completed program should:

- Create at least 4 endpoints (GET, POST, PUT, DELETE) for todo management
- Use proper HTTP status codes (200, 201, 404, etc.)
- Validate incoming data and return appropriate error messages
- Support storing and retrieving todo items with relevant fields (id, title, description, completed)
- Run on a local server and accept requests via curl or a web client

### 🛠️ Add Data Validation and Error Handling

#### Description

Enhance the API with robust input validation and comprehensive error handling. Implement request/response models using Pydantic to ensure data consistency and provide clear error messages to API clients.

#### Requirements

Completed program should:

- Define Pydantic models for request and response data
- Validate all incoming requests and reject invalid data with descriptive error messages
- Handle edge cases such as missing required fields or ID not found
- Return meaningful HTTP error responses (400, 404, 500)
- Include type hints throughout the code for better code documentation
