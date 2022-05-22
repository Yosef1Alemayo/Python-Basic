# Q2:
for i in range(0, 21):
    if i % 2 != 0:
        print(i)

# Q6:
sum1 = 0
for i in range(1, 14):
    sum1 = sum1 + i
    print(sum1)

# Q7:
for i in range(1, 11):
    for y in range(1, 11):
        print(y*i, '\t', end='')
    print()

# Q8:
num1 = input('Enter number :')
num2 = input('Enter number :')
for i in range(5):
    if num1[i] == num2[i]:
        print(num1[i], sep=':', end=' ')

# Q9:
num1 = input('Enter number with 5 digits:')
num2 = input('Enter number with 1 digit:')
for i in range(1):
    if num2 in num1:
        print(num2, 'in', num1)
    else:
        print(num2, 'Not in', num1)

# Q10:
sum1 = 0
for i in range(5):
    num = int(input('Enter number:'))
    sum1 += num
print('Your Average is:', sum1//5)

# Q11:
for i in range(3, 101):
    flag = 0
    for y in range(2, i):
        if i % y == 0:
            flag = 1
            break
    if flag != 1:
        print('Prime Number:', i)

# Q12:
for i in range(1, 11):
    for u in range(1, 11):
        result = i * u
        print(result, end=' ')
    print()

# Q15:
for i in range(7):
    string = 'Yosef Alemayo ☻'
    print(string)


# Q17:
rows = int(input('Enter Number:'))
columns = rows - 4
for i in range(rows):
    for y in range(columns):
        print('*', end=' ')
    print()
