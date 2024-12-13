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


def verify_report_safety_with_exception(filename: str):
    reports = read_reports(filename)
    safety_counter = 0

    for report in reports:
        is_safe = True
        is_increasing = None
        exception_count = 0
        level_index = 1
        while level_index < len(report):
            diff = report[level_index] - report[level_index - 1]
            
            if is_increasing is None:
                # At the first iteration
                is_increasing = diff > 0

            if exception_count >= 2:
                is_safe = False
                break

            elif diff == 0:
                report.pop(level_index)
                exception_count += 1

            elif is_increasing and diff < 0:
                """
                Remove cur if equal to or less than
                prev prev
                """
                cur = report[level_index]
                prev_prev = report[level_index - 2]
                local_diff = cur - prev_prev
                
                if cur <= prev_prev and abs(local_diff) <= 3:
                    report.pop(level_index)
                else:
                    report.pop(level_index - 1)

                exception_count += 1
                level_index -= 1
            else:
                if abs(diff) > 3:
                    if exception_count < 2:
                        report.pop(level_index)
                        level_index -= 1
                        exception_count += 1
                    else:
                        is_safe = False
                        break
                    
            level_index += 1

        if is_safe:
            safety_counter += 1
            
    return safety_counter
    
if __name__=="__main__":
    print(verify_report_safety_with_exception("test2.txt"))
