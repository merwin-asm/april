class ConnectApril {
    static def recv_request() {
        def n = Integer.parseInt(args[args.length - 1])
        def filePath = ".${n}.input"

        try {
            def data = new File(filePath).text
            return new groovy.json.JsonSlurper().parseText(data)
        } catch (Exception e) {
            println("Error: $e")
            return null
        }
    }

    static def send_response(response) {
        def n = Integer.parseInt(args[args.length - 1])
        def filePath = ".${n}.output"

        try {
            new File(filePath).text = new groovy.json.JsonBuilder(response).toPrettyString()
        } catch (Exception e) {
            println("Error: $e")
        }
    }
}