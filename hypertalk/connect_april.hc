on recv_request
   put the last word of the command into n
   put "." & n & ".input" into filePath

   try
      put url ("file:" & filePath) into data
      return from json data
   catch e
      put "Error: " & e into msg
      answer msg
      return empty
   end try
end recv_request

on send_response response
   put the last word of the command into n
   put "." & n & ".output" into filePath

   try
      put json of response into url ("file:" & filePath)
   catch e
      put "Error: " & e into msg
      answer msg
   end try
end send_response