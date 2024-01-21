ConnectApril := (
    recv_request := {
        |n|
        filePath := '.' + n + '.input'.
        data := NSString stringWithContentsOfFile:filePath encoding:4 error:nil.
        ^ data JSONValue.
    },

    send_response := {
        |response|
        n := NSString stringWithUTF8String:(__argv at:__argv size - 1).
        filePath := '.' + n + '.output'.
        responseStr := response JSONRepresentation.
        responseStr writeToFile:filePath atomically:YES encoding:4 error:nil.
    }
).