# if-else
a = 1
b = 2
if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('a is less than b')

# for loop
a = [11, 12, 13]
for i in a:
    print(i)

# while loop
a = 0
while a < 6:
    print(a)
    a += 1

# design1
line = '*'
max_len = 5
while len(line) <= max_len:
    print(line)
    line += '*'

while len(line) > 0:
    print(line)
    line = line[:-1]

# design2
line = '*'
gap = ' '
max_len = 5
while len(line) <= max_len:
    gap1 = round((max_len - len(line))/2)
    print((gap1*gap) + line + (gap1*gap))
    line += '**'

# defining function
def square(a):
    print(a*a)

square(3)
