def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


for line in read_file_line_by_line('Day 64/sample.txt'):
    print(line)
