class ConnectApril {
    static function recvRequest(): Null<Dynamic> {
        var n: Int = Std.parseInt(Std.string(Std.int(Std.args()[Std.args().length - 1])));
        var filePath: String = '.' + Std.string(n) + '.input';

        try {
            var data: String = sys.io.File.getContent(filePath);
            return haxe.Json.parse(data);
        } catch (e: Dynamic) {
            trace('Error: $e');
            return null;
        }
    }

    static function sendResponse(response: Dynamic): Void {
        var n: Int = Std.parseInt(Std.string(Std.int(Std.args()[Std.args().length - 1])));
        var filePath: String = '.' + Std.string(n) + '.output';

        try {
            sys.io.File.saveContent(filePath, haxe.Json.stringify(response));
        } catch (e: Dynamic) {
            trace('Error: $e');
        }
    }
}