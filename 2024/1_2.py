from utils import read_file

def calculate_similarity_score(filename: str):
    first, second = read_file(filename)

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
    print(calculate_similarity_score("input.txt"))
