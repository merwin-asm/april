import Foundation

class ConnectApril {
    static func recvRequest() -> [String: Any]? {
        let arguments = CommandLine.arguments
        guard let n = arguments.last else { return nil }
        let filePath = "./\(n).input"

        do {
            let data = try String(contentsOfFile: filePath, encoding: .utf8)
            return try JSONSerialization.jsonObject(with: data.data(using: .utf8)!, options: []) as? [String: Any]
        } catch {
            print(error)
            return nil
        }
    }

    static func sendResponse(response: [String: Any]) {
        let arguments = CommandLine.arguments
        guard let n = arguments.last else { return }
        let filePath = "./\(n).output"

        do {
            let jsonData = try JSONSerialization.data(withJSONObject: response)
            try jsonData.write(to: URL(fileURLWithPath: filePath), options: [])
        } catch {
            print(error)
        }
    }
}