def read_file_and_build_cols(filename: str):
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
    first, second = read_file_and_build_cols(filename)
    zipped_values = list(zip(sorted(first), sorted(second)))
    total = calculate_total(zipped_values)
    return total

def calculate_similarity_score(filename: str):
    first, second = read_file_and_build_cols(filename)

    #Frequency of second list
    d = {}
    for num in second:
        d[num] = d.get(num, 0) + 1

    score = 0
    for num in first:
        # Calculate the score for each value in `first`
        score += num * d.get(num, 0)
    return score

if __name__=="__main__":
    print(calculate_total_distance("input1.txt"))
    print(calculate_similarity_score("input1.txt"))
