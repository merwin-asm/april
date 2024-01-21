REBOL [Title: "ConnectApril in Red/Func"]

recv-request: func [
    /local n file-path data
][
    n: last system/options/args
    file-path: rejoin ["." n ".input"]

    attempt [
        data: read file-path
        from-json data
    ] [
        print ["Error:" disarm disarm system/error]
        none
    ]
]

send-response: func [response /local n file-path][
    n: last system/options/args
    file-path: rejoin ["." n ".output"]

    attempt [
        write file-path to-json response
    ] [
        print ["Error:" disarm disarm system/error]
    ]
]