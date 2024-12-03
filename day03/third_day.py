import re
def part_one_sum(text):
    matches = re.findall("mul\((\d{1,3},\d{1,3})\)", text)
    matches = [int(a) * int(b) for a, b in [re.findall(r'\d{1,3}', match) for match in matches]]
    print(sum(matches))

def part_two_sum(text):
    matches = re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', text)
    result = 0
    enabled = True
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == 'don\'t()':
            enabled = False
        elif enabled:
            result += [int(a) * int(b) for a, b in [re.findall(r'\d{1,3}', match)]][0]
    print(result)

if __name__ == "__main__":
    text = ""
    with open('day03/input.txt', 'r') as text_file:
        text = text_file.read()
    part_one = part_one_sum(text)
    part_two = part_two_sum(text)

    

