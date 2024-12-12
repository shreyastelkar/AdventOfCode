def read_reports(filename: str):
    matrix = []
    with open(filename) as f:
        for line in f:
            list_line = [ int(x) for x in line.split()]
            matrix.append(list_line)
    return matrix

def verify_report_safety(filename: str):
    reports = read_reports(filename)
    safety_counter = 0
    
    for report in reports:
        is_safe = True
        increasing_map = {}

        for level_index in range(1, len(report)):
            if 1 <= abs(report[level_index] - report[level_index - 1]) <= 3:
                # Check if the previous state was increasing
                is_increasing = increasing_map.get(level_index - 1, None)
                
                if is_increasing is None:
                    # At the first iteration
                    if report[level_index] > report[level_index - 1]:
                        increasing_map[level_index] = True
                    elif report[level_index] < report[level_index - 1]:
                        increasing_map[level_index] = False
                    else:
                        # Impossible case
                        break
                        
                elif is_increasing is True:
                    # Check if the current is also increasing
                    if report[level_index] < report[level_index - 1]:
                        is_safe = False
                        break
                    else:
                        increasing_map[level_index] = True
                else:
                    # is_increasing is False
                    if report[level_index] > report[level_index - 1]:
                        is_safe = False
                        break
                    else:
                        increasing_map[level_index] = False

            else:
                # Duplicate value and unsafe
                is_safe = False
                break

        if is_safe:
            safety_counter += 1
            
    return safety_counter

if __name__=="__main__":
    print(verify_report_safety("input2.txt"))
