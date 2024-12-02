def is_safe(report):
    for i in range(len(report)-1):
        num = report[i+1] - report[i]
        if not (1 <= num <= 3 or -3 <= num <= -1):
            return False
    return all(report[i] < report[i + 1] for i in range(len(report) - 1)) or \
           all(report[i] > report[i + 1] for i in range(len(report) - 1))

def is_safe_damper(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        mod_report = report[:i] + report[i+1:]
        if is_safe(mod_report):
            return True
    return False

safe_count = 0 
safe_count_damper = 0
with open('day02/input.txt', 'r') as text_file:
    data = text_file.read().strip().split('\n')
for report in data:
    reports = list(map(int, report.split()))
    if is_safe(reports):
        safe_count += 1
    if is_safe_damper(reports):
        safe_count_damper += 1
print(safe_count)
print(safe_count_damper)

  