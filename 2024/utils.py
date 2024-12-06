def read_file(filename: str):
    first = []
    second = []
    with open(filename) as f:
        for line in f:
            line_numbers = line.split()
            first.append(int(line_numbers[0]))
            second.append(int(line_numbers[1]))

    return first, second
