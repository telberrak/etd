def filter_lines_by_prefix(input_file, output_file, prefix="FTOF"):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Iterate through each line in the input file
            for line in infile:
                # Check if the first 4 characters match the prefix
                if line.startswith(prefix):
                    # Write the line to the output file if it matches
                    outfile.write(line)
        print(f"Lines starting with '{prefix}' have been written to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file
    output_file = "output.txt"  # Replace with your output file
    filter_lines_by_prefix(input_file, output_file)
