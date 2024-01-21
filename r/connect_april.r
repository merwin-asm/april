recv_request <- function() {
  n <- commandArgs(trailingOnly = TRUE)[length(commandArgs(trailingOnly = TRUE))]
  file_path <- paste0(".", n, ".input")

  tryCatch({
    data <- readLines(file_path, warn = FALSE)
    json_data <- jsonlite::fromJSON(data[1])
    return(json_data)
  }, error = function(err) {
    cat("Error: ", conditionMessage(err), "\n")
    return(NULL)
  })
}

send_response <- function(response) {
  n <- commandArgs(trailingOnly = TRUE)[length(commandArgs(trailingOnly = TRUE))]
  file_path <- paste0(".", n, ".output")

  tryCatch({
    json_data <- jsonlite::toJSON(response, auto_unbox = TRUE)
    writeLines(json_data, file_path)
  }, error = function(err) {
    cat("Error: ", conditionMessage(err), "\n")
  })
}