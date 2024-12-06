from utils import read_file

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
