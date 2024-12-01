text_file = open('day01\input.txt','r')
left = []
right = []
for line in text_file.readlines():
  line = line.replace('\n', '')
  numbers = line.split('  ')
  left.append(int(numbers[0]))
  right.append(int(numbers[1]))
right.sort()
left.sort()
distance = 0
for i in range(len(left)):
  distance += abs(left[i] - right[i])
print(distance)
similarity_score = 0
for number in left:
    similarity_score += number * right.count(number)

print(similarity_score)