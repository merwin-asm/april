

package connect_april

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

// RecvRequest reads a file based on the command-line argument and returns the parsed JSON data.
func RecvRequest() (map[string]interface{}, error) {
	n := os.Args[len(os.Args)-1]
	filePath := fmt.Sprintf(".%s.input", n)

	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("error reading file: %s", filePath)
	}

	var jsonData map[string]interface{}
	if err := json.Unmarshal(data, &jsonData); err != nil {
		return nil, fmt.Errorf("error parsing JSON data: %v", err)
	}

	return jsonData, nil
}

// SendResponse writes the provided response as JSON to a file based on the command-line argument.
func SendResponse(response map[string]interface{}) error {
	n := os.Args[len(os.Args)-1]
	filePath := fmt.Sprintf(".%s.output", n)

	responseJSON, err := json.Marshal(response)
	if err != nil {
		return fmt.Errorf("error encoding response as JSON: %v", err)
	}

	if err := ioutil.WriteFile(filePath, responseJSON, 0644); err != nil {
		return fmt.Errorf("error writing file: %s", filePath)
	}

	return nil
}

