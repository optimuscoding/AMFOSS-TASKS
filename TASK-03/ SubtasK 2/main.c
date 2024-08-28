#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *inputFile, *outputFile;
    char buffer[1024]; 

   
    inputFile = fopen("input.txt", "r");
    if (inputFile == NULL) {
        perror("Error opening input file");
        return EXIT_FAILURE;
    }

   
    outputFile = fopen("output.txt", "w");
    if (outputFile == NULL) {
        perror("Error opening output file");
        fclose(inputFile);
        return EXIT_FAILURE;
    }

    while (fgets(buffer, sizeof(buffer), inputFile) != NULL) {
        fputs(buffer, outputFile);
    }

  
    fclose(inputFile);
    fclose(outputFile);

    printf("File content copied successfully.\n");
    return EXIT_SUCCESS;
}

