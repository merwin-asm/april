local connect_april = {}

function connect_april.recv_request()
    local n = arg[#arg]
    local filePath = '.' .. n .. '.input'

    local file = io.open(filePath, 'r')
    if file then
        local data = file:read('*a')
        file:close()
        return json.decode(data)
    else
        print('Error reading file:', filePath)
        return nil
    end
end

function connect_april.send_response(response)
    local n = arg[#arg]
    local filePath = '.' .. n .. '.output'

    local file, err = io.open(filePath, 'w')
    if file then
        file:write(json.encode(response))
        file:close()
    else
        print('Error writing file:', err)
    end
end

return connect_april
