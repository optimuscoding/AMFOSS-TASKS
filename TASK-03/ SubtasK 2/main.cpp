#include <iostream>
#include <fstream>
#include <string>

int main() {
   
    std::string inputFilePath = "input.txt";
    std::string outputFilePath = "output.txt";

 
    std::ifstream inputFile(inputFilePath);
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputFilePath << std::endl;
        return 1;
    }

    
    std::string content((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close(); 

  
    std::ofstream outputFile(outputFilePath);
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputFilePath << std::endl;
        return 1;
    }

    /
    outputFile << content;
    outputFile.close(); 

    std::cout << "Content successfully copied from " << inputFilePath << " to " << outputFilePath << std::endl;

    return 0;
}
