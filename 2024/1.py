def read_file(filename: str):
    first = []
    second = []
    with open(filename) as f:
        for line in f:
            line_numbers = line.split()
            first.append(int(line_numbers[0]))
            second.append(int(line_numbers[1]))

    return first, second

def calculate_total(values):
    total = 0
    for num1, num2 in values:
        total += abs(num1 - num2)
    return total
        
def calculate_total_distance(filename: str):
    first, second = read_file(filename)
    zipped_values = list(zip(sorted(first), sorted(second)))
    total = calculate_total(zipped_values)
    return total

if __name__=="__main__":
    print(calculate_total_distance("input.txt"))
