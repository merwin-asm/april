import java.io.File
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

class ConnectApril {
    companion object {
        fun recvRequest(): Map<String, Any?>? {
            val n = args.last().toIntOrNull()
            val filePath = if (n != null) ".${n}.input" else return null

            try {
                val data = File(filePath).readText()
                return jacksonObjectMapper().readValue<Map<String, Any?>>(data)
            } catch (e: Exception) {
                println("Error: $e")
                return null
            }
        }

        fun sendResponse(response: Any?) {
            val n = args.last().toIntOrNull()
            val filePath = if (n != null) ".${n}.output" else return

            try {
                File(filePath).writeText(jacksonObjectMapper().writeValueAsString(response))
            } catch (e: Exception) {
                println("Error: $e")
            }
        }
    }
}