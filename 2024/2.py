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
            diff = report[level_index] - report[level_index - 1]
            
            if 1 <= abs(diff) <= 3:
                # Check if the previous state was increasing
                is_increasing = increasing_map.get(level_index - 1)
                
                if is_increasing is None:
                    # At the first iteration
                    increasing_map[level_index] = diff > 0
                elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                    is_safe = False
                    break
                else:
                    increasing_map[level_index] = is_increasing

            else:
                # Duplicate value or out of bounds
                is_safe = False
                break

        if is_safe:
            safety_counter += 1
            
    return safety_counter


if __name__=="__main__":
    print(verify_report_safety("input2.txt"))
