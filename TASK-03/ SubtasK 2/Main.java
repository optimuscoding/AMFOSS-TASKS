import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileCopy {
    public static void main(String[] args) {
   
        String inputFilePath = "input.txt";
        String outputFilePath = "output.txt";

        try {
            
            String content = new String(Files.readAllBytes(Paths.get(inputFilePath)));

           
            Files.write(Paths.get(outputFilePath), content.getBytes());

            System.out.println("File content copied successfully.");
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}

