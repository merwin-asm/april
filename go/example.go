// example.go

package main

import (
	"fmt"
	"connect_april" // Adjust the import path based on your project structure
)

func main() {
	// Example usage:
	requestData, err := connect_april.RecvRequest()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Received data:", requestData)

	responseData := map[string]interface{}{"output": "Hello from, Go!"}
	if err := connect_april.SendResponse(responseData); err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Response sent.")
}

