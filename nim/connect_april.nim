import json
import os

proc recvRequest(): JsonNode {.raises: [IOError, JsonError].} =
  let n = paramStr(paramCount())
  let filePath = ".$n.input"

  try:
    let data = readFile(filePath)
    return parseJson(data)
  except IOError, JsonError:
    echo getCurrentExceptionMsg()
    result = nil

proc sendResponse(response: JsonNode) {.raises: [IOError, JsonError].} =
  let n = paramStr(paramCount())
  let filePath = ".$n.output"

  try:
    writeFile(filePath, $response)
  except IOError, JsonError:
    echo getCurrentExceptionMsg()