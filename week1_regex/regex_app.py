import re

sample = open('regex_assignment.txt','r')
sum = 0
for line in sample:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num)!=0:
        for item in num:
            sum += int(item)
print(sum)