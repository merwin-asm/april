// Set API information
TITLE 'BMI Calculator API'
VERSION 1.0
DESC 'An API for calculating Body Mass Index (BMI)'

// Define endpoint to calculate BMI
post('/bmi') : python3 bmi_handler.py calculate_bmi
