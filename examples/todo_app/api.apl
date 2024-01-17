// Set API information
TITLE 'Todo API'
VERSION 1.0
DESC 'An API for a simple todo app'

// Define endpoint to get all todos
get('/todos') : python3 todo_handler.py list_todos

// Define endpoint to add a new todo
post('/todos') : python3 todo_handler.py add_todo

// Define endpoint to mark a todo as completed
put('/todos/{todo_id}') : python3 todo_handler.py complete_todo
