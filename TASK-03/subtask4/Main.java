import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DiamondPattern {

    
    public static int readNumberFromFile(String filename) {
        int number = -1;
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line = reader.readLine().trim();
            number = Integer.parseInt(line);
            if (number <= 0) {
                throw new NumberFormatException();
            }
        } catch (IOException | NumberFormatException e) {
            System.out.println("Error reading from file '" + filename + "': " + e.getMessage());
            number = -1;
        }
        return number;
    }

   
    public static String generateDiamond(int n) {
        if (n < 1 || n % 2 == 0) {
            return "Please enter a positive odd number.\n";
        }

        StringBuilder pattern = new StringBuilder();
        int half = n / 2;

        for (int i = 0; i < n; i++) {
            if (i <= half) {
                String spaces = " ".repeat(half - i);
                String stars = "*".repeat(2 * i + 1);
                pattern.append(spaces).append(stars).append("\n");
            } else {
                String spaces = " ".repeat(i - half);
                String stars = "*".repeat(2 * (n - i - 1) + 1);
                pattern.append(spaces).append(stars).append("\n");
            }
        }

        return pattern.toString();
    }

    
    public static void writeDiamondToFile(String filename, String pattern) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            writer.write(pattern);
        } catch (IOException e) {
            System.out.println("Error writing to file '" + filename + "': " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String inputFilename = "input.txt";
        String outputFilename = "output.txt";

        int n = readNumberFromFile(inputFilename);


        if (n != -1) {
            String diamondPattern = generateDiamond(n);
            writeDiamondToFile(outputFilename, diamondPattern);
        }
    }
}
