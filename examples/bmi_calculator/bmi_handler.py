# Import necessary modules
import json
from connect_april import April

# Function to calculate BMI
def calculate_bmi():
    # Read input from the input file using the connect_april package
    input_data = April().recv_request()

    # Extract height and weight from input
    height = float(input_data["input"]["height"])
    weight = float(input_data["input"]["weight"])

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Prepare the output data
    output_data = {
        "headers": {"Content-Type": "application/json"},
        "status": 200,
        "output": {
            "bmi": bmi,
            "category": bmi_category
        }
    }

    # Write output to the output file using the connect_april package
    April().send_response(output_data)

# Execute the calculate_bmi function if the script is run directly
if __name__ == "__main__":
    calculate_bmi()
