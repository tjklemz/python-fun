file = open('/Users/tjklemz/Desktop/file.txt', 'r')
lines = file.readlines()
file.close()

total = 0
for line in lines:
    name = line.split(',')[0]
    grade = int(line.split(',')[1].strip())
    total = total + grade

grade_avg = total / len(lines)

with open('/Users/tjklemz/Desktop/results.txt', 'w') as file:
    file.write(str(grade_avg))
