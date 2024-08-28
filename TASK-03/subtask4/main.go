
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)


func readNumberFromFile(filename string) (int, error) {
    file, err := os.Open(filename)
    if err != nil {
        return 0, fmt.Errorf("error opening file '%s': %v", filename, err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    if !scanner.Scan() {
        return 0, fmt.Errorf("error reading from file '%s': %v", filename, scanner.Err())
    }

    line := strings.TrimSpace(scanner.Text())
    number, err := strconv.Atoi(line)
    if err != nil || number <= 0 {
        return 0, fmt.Errorf("invalid number in file '%s': %v", filename, err)
    }

    return number, nil
}


func generateDiamond(n int) string {
    if n < 1 || n%2 == 0 {
        return "Please enter a positive odd number.\n"
    }

    var sb strings.Builder
    half := n / 2

    
    for i := 0; i < n; i++ {
        if i <= half {
            spaces := strings.Repeat(" ", half-i)
            stars := strings.Repeat("*", 2*i+1)
            sb.WriteString(spaces + stars + "\n")
        } else {
            spaces := strings.Repeat(" ", i-half)
            stars := strings.Repeat("*", 2*(n-i-1)+1)
            sb.WriteString(spaces + stars + "\n")
        }
    }

    return sb.String()
}


func writeDiamondToFile(filename string, pattern string) error {
    file, err := os.Create(filename)
    if err != nil {
        return fmt.Errorf("error creating file '%s': %v", filename, err)
    }
    defer file.Close()

    _, err = file.WriteString(pattern)
    if err != nil {
        return fmt.Errorf("error writing to file '%s': %v", filename, err)
    }

    return nil
}

func main() {
    inputFilename := "input.txt"
    outputFilename := "output.txt"

   
    n, err := readNumberFromFile(inputFilename)
    if err != nil {
        fmt.Println(err)
        return
    }

    diamondPattern := generateDiamond(n)

    err = writeDiamondToFile(outputFilename, diamondPattern)
    if err != nil {
        fmt.Println(err)
    }
}
