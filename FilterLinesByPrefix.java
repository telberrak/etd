import java.io.*;

public class FilterLinesByPrefix {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java FilterLinesByPrefix <inputFile> <outputFile>");
            return;
        }

        String inputFile = args[0];
        String outputFile = args[1];

        try (
            BufferedReader reader = new BufferedReader(new FileReader(inputFile));
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))
        ) {
            String line;
            // Read each line from the input file
            while ((line = reader.readLine()) != null) {
                // Check if the line starts with "FTOF"
                if (line.startsWith("FTOF")) {
                    // Write the matching line to the output file
                    writer.write(line);
                    writer.newLine();
                }
            }
            System.out.println("Processing complete. Matching lines written to " + outputFile);
        } catch (IOException e) {
            System.err.println("Error processing the file: " + e.getMessage());
        }
    }
}
