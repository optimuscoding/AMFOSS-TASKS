package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	
	inputFile, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening input file:", err)
		return
	}
	defer inputFile.Close()

	content, err := ioutil.ReadAll(inputFile)
	if err != nil {
		fmt.Println("Error reading from input file:", err)
		return
	}

	
	outputFile, err := os.Create("output.txt")
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer outputFile.Close()

	_, err = outputFile.Write(content)
	if err != nil {
		fmt.Println("Error writing to output file:", err)
		return
	}

	fmt.Println("File content copied successfully.")
}

