const std = @import("std");

pub fn recvRequest() !json.Node {
    const n = std.os.args.last();
    const filePath = "." ++ n ++ ".input";

    const data = try std.fs.readFile(filePath);
    return try std.json.parse(data);
}

pub fn sendResponse(response: json.Node) !void {
    const n = std.os.args.last();
    const filePath = "." ++ n ++ ".output";

    const jsonData = try std.json.stringify(response);
    try std.fs.writeFile(filePath, jsonData);
}