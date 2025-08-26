
def cleanup_file(input_filename, output_filename):
    """
    Reads a file, removes trailing whitespace and empty lines,
    and writes the result to a new file.
    """
    print(f"Reading from '{input_filename}'...")
    
    cleaned_lines = []
    with open(input_filename, 'r') as infile:
        for line in infile:
            cleaned_line = line.rstrip()
            
            
            if cleaned_line:
                cleaned_lines.append(cleaned_line)

    print(f"Writing cleaned content to '{output_filename}'...")
    with open(output_filename, 'w') as outfile:
        outfile.write("\n".join(cleaned_lines))
        
    print("Cleanup complete!")


if __name__ == "__main__":
    cleanup_file("input.txt", "output.txt")