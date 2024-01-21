module ConnectApril {
    import std.io;
    import std.json;
    import std.file;

    fn recv_request() -> ?Json {
        n := to_i32(get_args()[get_args().len - 1]);
        filePath := fmts(".%d.input", n);

        try {
            data := read_entire_file(filePath);
            return json_parse(data);
        } catch (e) {
            println("Error: ", e);
            return null;
        }
    }

    fn send_response(response: Json) {
        n := to_i32(get_args()[get_args().len - 1]);
        filePath := fmts(".%d.output", n);

        try {
            write_entire_file(filePath, json_stringify(response));
        } catch (e) {
            println("Error: ", e);
        }
    }
}