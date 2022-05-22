# Q1:
x = 0
while x < 20:
    x = x + 1
    if x % 2 != 0:
        print(x)

# Q3:
x = 0
num = int(input('Please enter number:'))
while x < num:
    x = x + 1
    if x % 2 != 0:
        print(x)

# Q4:
x = 0
num = int(input('Please enter number:'))
que = input('For even Numbers press "2" , For odd Numbers press "1": ')
while x < num:
    x = x + 1
    if que == '1':
        if x % 2 != 0:
            print(x)
    if que == '2':
        if x % 2 == 0:
            print(x)
    if que != '1' and que != '2':
        print('Error')
        break

# Q5:
start = 0
end = 1000
middle = (start+end)//2
guess_num = int(input('Enter Number between 1 - 1000:'))
print('Start =', start, 'Middle =', middle, 'End =', end, 'The number is:', guess_num)
while guess_num != middle:
    middle = (start + end) // 2
    if guess_num > middle:
        start = middle
        print('Start =', start, 'Middle =', middle, 'End =', end)
    else:
        end = middle
        print('Start =', start, 'Middle =', middle, 'End =', end)
print('Found', guess_num)


# Q13:
x = 100
while x < 500:
    print(x)
    x = x + 4

# Q14:
x = 5
while x < 2500:
    x = x + 1
    if x % 6 == 0:
        print(x)

# Q16:
count = 0
total = 0
print("Program numbers : To exit Press 'Q'")
price = input("Enter The number:")
while price != 'Q':
    total = total + int(price)
    count = count + 1
    price = input("Enter another number:")
print('The sum is', total)
avg = total/count
print('The Average is', int(avg))

# Q18:
count = 0
total1 = 0
counter_max = []
num = input('Enter Number:')
while num != 'done':
    counter_max.append(num)
    total1 = total1 + int(num)
    count = count + 1
    num = input('Enter Number:')
avg = total1 / count
print('The Average is', int(avg))
print('the max number is:', max(counter_max), 'The Min Number is:', min(counter_max))


