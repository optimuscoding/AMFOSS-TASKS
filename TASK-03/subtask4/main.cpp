#include <iostream>
#include <fstream>
#include <string>


int readNumberFromFile(const std::string& filename) {
    std::ifstream file(filename);
    int number;
    
    if (!file.is_open()) {
        std::cerr << "Error opening file '" << filename << "'" << std::endl;
        return -1;
    }
    
    file >> number;
    
    if (file.fail() || number <= 0) {
        std::cerr << "Invalid number in file '" << filename << "'" << std::endl;
        file.close();
        return -1;
    }
    
    file.close();
    return number;
}


std::string generateDiamond(int n) {
    if (n < 1 || n % 2 == 0) {
        return "Please enter a positive odd number.\n";
    }

    std::string pattern;
    int half = n / 2;

  
    for (int i = 0; i < n; ++i) {
        if (i <= half) {
            pattern.append(half - i, ' '); 
            pattern.append(2 * i + 1, '*'); 
        } else {
            pattern.append(i - half, ' '); 
            pattern.append(2 * (n - i - 1) + 1, '*'); 
        pattern.append("\n"); 
    }

    return pattern;
}


void writeDiamondToFile(const std::string& filename, const std::string& pattern) {
    std::ofstream file(filename);
    
    if (!file.is_open()) {
        std::cerr << "Error opening file '" << filename << "'" << std::endl;
        return;
    }
    
    file << pattern;
    file.close();
}

int main() {
    const std::string inputFilename = "input.txt";
    const std::string outputFilename = "output.txt";

   
    int n = readNumberFromFile(inputFilename);
    if (n == -1) {
        return 1; 
    }

  
    std::string diamondPattern = generateDiamond(n);

  
    writeDiamondToFile(outputFilename, diamondPattern);

    return 0;
}
