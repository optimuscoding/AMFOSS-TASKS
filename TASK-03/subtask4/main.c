
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int read_number_from_file(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error opening file '%s'\n", filename);
        return -1;
    }

    int number;
    if (fscanf(file, "%d", &number) != 1 || number <= 0) {
        fprintf(stderr, "Invalid number in file '%s'\n", filename);
        fclose(file);
        return -1;
    }

    fclose(file);
    return number;
}


void generate_diamond(int n, char *pattern) {
    if (n < 1 || n % 2 == 0) {
        strcpy(pattern, "Please enter a positive odd number.\n");
        return;
    }

    int half = n / 2;
    int index = 0;

 
    for (int i = 0; i < n; i++) {
        if (i <= half) {
            int spaces = half - i;
            int stars = 2 * i + 1;
            index += sprintf(pattern + index, "%*s%.*s\n", spaces, "", stars, "************************************");
        } else {
            int spaces = i - half;
            int stars = 2 * (n - i - 1) + 1;
            index += sprintf(pattern + index, "%*s%.*s\n", spaces, "", stars, "************************************");
        }
    }
}

void write_diamond_to_file(const char *filename, const char *pattern) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file '%s'\n", filename);
        return;
    }

    fprintf(file, "%s", pattern);
    fclose(file);
}

int main() {
    const char *input_filename = "input.txt";
    const char *output_filename = "output.txt";

 
    int n = read_number_from_file(input_filename);
    if (n == -1) {
        return 1; 
    }

   
    char pattern[1000]; 
    generate_diamond(n, pattern);

 
    write_diamond_to_file(output_filename, pattern);

    return 0;
}
