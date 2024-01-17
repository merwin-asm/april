# Import the connect_april package
import connect_april

april = connect_april.April()

# Read input from the input file using the connect_april package
input_data = april.recv_request()

# Get the current time
from datetime import datetime
current_time = str(datetime.now())

# Prepare the output data
output_data = {
    "headers": {"Content-Type": "application/json"},
    "status": 200,
    "output": {"current_time": current_time}
}

# Write output to the output file using the connect_april package
april.send_response(output_data)
