def read_reports(filename: str):
    with open(filename) as f:
        matrix = [[ int(x) for x in line.split()] for line in f]
    return matrix

def verify_report_safety(filename: str):
    reports = read_reports(filename)
    safety_counter = 0
    
    for report in reports:
        is_safe = True
        is_increasing = None

        for level_index in range(1, len(report)):
            diff = report[level_index] - report[level_index - 1]
            
            if 1 <= abs(diff) <= 3:
                if is_increasing is None:
                    # At the first iteration
                    is_increasing = diff > 0
                elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                    is_safe = False
                    break
                else:
                    # Leave the increasing trend as is
                    pass

            else:
                # Duplicate value or out of bounds
                is_safe = False
                break

        if is_safe:
            safety_counter += 1
            
    return safety_counter


if __name__=="__main__":
    print(verify_report_safety("input2.txt"))
