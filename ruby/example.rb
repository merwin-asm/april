# main.rb

require_relative 'connect_april'

# Example usage:
request_data = ConnectApril.recv_request
puts "Received data: #{request_data}"

response_data = { 'output' => 'Hello from, Ruby!' }
ConnectApril.send_response(response_data)
puts 'Response sent.'

