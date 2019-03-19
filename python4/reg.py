import re

total = 0

file = open('re.txt', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            total += int(number)

print(total)
