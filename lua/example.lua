-- main.lua

local connect_april = require("connect_april")
local json = require("json")  -- Assuming you have a JSON library for Lua

-- Example usage:
local requestData = connect_april.recv_request()
print('Received data:', requestData)

local responseData = { output = 'Hello from, Lua!' }
connect_april.send_response(responseData)
print('Response sent.')

