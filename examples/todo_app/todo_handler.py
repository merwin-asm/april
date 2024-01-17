# Import necessary modules
import json
from connect_april import April

# Function to list all todos
def list_todos():
    response = {
        "headers": {"Content-Type": "application/json"},
        "status": 200,
        "output": {"todos": todos}
    }
    April().send_response(response)

# Function to add a new todo
def add_todo():
    input_data = April().recv_request()
    new_todo = input_data["input"]["todo"]
    todos.append(new_todo)

    response = {
        "headers": {"Content-Type": "application/json"},
        "status": 201,
        "output": {"message": "Todo added successfully"}
    }
    April().send_response(response)

# Function to mark a todo as completed
def complete_todo():
    input_data = April().recv_request()
    todo_id = input_data["input"]["todo_id"]

    try:
        todos[todo_id]['completed'] = True
        response = {
            "headers": {"Content-Type": "application/json"},
            "status": 200,
            "output": {"message": f"Todo {todo_id} marked as completed"}
        }
    except IndexError:
        response = {
            "headers": {"Content-Type": "application/json"},
            "status": 404,
            "output": {"error": "Todo not found"}
        }

    April().send_response(response)

# Execute the corresponding function based on the command-line argument
if __name__ == "__main__":
    command = sys.argv[2]
    if command == "list_todos":
        list_todos()
    elif command == "add_todo":
        add_todo()
    elif command == "complete_todo":
        complete_todo()
