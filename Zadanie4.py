import random

mark = list()

for x in range(3):
    l = list()
    for y in range(15):
        l.append(random.randint(1, 5))
    mark.append(l)

print('Random table:')
for y in range(15):
    print(mark[0][y], mark[1][y], mark[2][y])
print()

sum1 = sum(mark[0])
sum2 = sum(mark[1])
sum3 = sum(mark[2])

value_max = max(sum1, sum2, sum3)

if ((sum1 >= sum2) and (sum1 >= sum3)):
    print('Biggest sum ({}) - lesson 1'.format(value_max))
    exit(0)
    
if ((sum2 >= sum1) and (sum2 >= sum3)):
    print('Biggest sum ({}) - lesson 2'.format(value_max))
    exit(0)
    
if ((sum3 >= sum1) and (sum3 >= sum2)):
    print('Biggest sum ({}) - lesson 3'.format(value_max))
    exit(0)
