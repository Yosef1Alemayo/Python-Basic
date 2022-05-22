# Q1:
for i in range(5):
    print('I Love Python ♥')

# Q2:
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

# Q3:
nums = []
for i in range(10):
    nums.append(int(input('Number:')))
new_nums = sorted(nums, reverse=True)
print(new_nums)
print(nums)

# Q4:
nums_main = []
result_dividing_11 = []
nums_even = []
nums_big_10 = 0
num_low_10 = 0
nums_dividing_3 = 0
result_dividing_3 = []
for i in range(11):
    nums_main.append(int(input('Enter Number:')))
for i in nums_main:
    x = i / 11
    result_dividing_11.append(x)
    if i > 10:
        nums_big_10 += 1
    if i < 10:
        num_low_10 += 1
    if i % 2 == 0:
        nums_even.append(i)
    if i % 3 == 0:
        nums_dividing_3 += 1
        y = i // 3
        result_dividing_3.append(y)
print('You Insert the Numbers:', nums_main)
print('The sum of the Numbers:', sum(nums_main))
print('The Result of Dividing with 11:', result_dividing_11)
print('The Amount of Numbers greater than 10:', nums_big_10)
print('The Amount of Numbers lower than 10:', num_low_10)
print('The Max Number is:', max(nums_main))
print('The Even Numbers are:', nums_even)
print('The Amount of Numbers that dividing with 3:', nums_dividing_3)
print('The Result of Dividing with 3:', result_dividing_3)

# Q6:
student1 = []
student2 = []
counter_overLapping = 0
for i in range(5):
    grade1 = int(input('Student 1 ,Enter Your Grades:'))
    grade2 = int(input('Student 2 , Enter Your Grades:'))
    student1.append(grade1)
    student2.append(grade2)
for i in student1:
    for j in student2:
        if i == j:
            counter_overLapping += 1
animal = input('Enter Your Favorite Animal:')
if len(animal) % 2 == 0:
    print('\t\t-String length even ')
else:
    print('\t\t-String length odd')
print('\t\t-Student1 Grades are:', student1)
print('\t\t-Student2 Grades are:', student2)
print('\t\t-The Amount of Overlapping Numbers:', counter_overLapping)

# Q7:
israel_Road_name = []
israel_Road_length = []
israel_Road_new = []
for i in range(20):
    name = input('Name Of Road:')
    length = float(input('Length of the Road:'))
    israel_Road_name.append(name)
    israel_Road_length.append(length)
for i in israel_Road_length:
    if i > 10:
        israel_Road_new.append(i)

print('The Name Of The Road:', israel_Road_name)
print('The Length of The Road:', israel_Road_length)
print('The Total Length of the Road is:', sum(israel_Road_length))
print('Length Roads that Bigger than 10 KM', israel_Road_new)

# Q8:
customers = []
total_boxes = []
total_price = []
price_box = 35
tax = 10
counter_big_20 = 0
for i in range(100):
    name = input('Name:')
    num_boxes = int(input('Number of boxes ? :'))
    customers.append(name)
    total_boxes.append(num_boxes)
for i in total_boxes:
    if i < 4:
        x = i * price_box + tax
        total_price.append(x)
    else:
        y = i * price_box
        total_price.append(y)
    if i > 20:
        counter_big_20 += 1
print('The customers Name:', customers)
print('Total Boxes', total_boxes)
print('Total Price for each customer:', total_price)
print('The Amount of Customers that order over 20 Boxes:', counter_big_20)

# Q9:
family_name = []
number_Of_Children = []
for i in range(3):
    name = input('Family Name:')
    num = int(input('How much Children ? :'))
    family_name.append(name)
    number_Of_Children.append(num)
for i in number_Of_Children:
    if i > 3:
        print('A Discount !')
    else:
        pass
print('The number of the children that Going to the trip:', sum(number_Of_Children))

# Q10:
people = []
birth_Year = []
blood = []
counter_Blood_O = 0
for i in range(25):
    name = input('Name:')
    year = int(input('Year:'))
    que1 = input('Blood:')
    people.append(name)
    birth_Year.append(year)
    blood.append(que1)
for i in blood:
    if i == 'O' or i == 'o':
        counter_Blood_O += 1
new_list = [people, birth_Year, blood]
print('People Names', people, '\n Year:', birth_Year, '\n Type of Blood:', blood)
print('Numbers of People with O Blood:', counter_Blood_O)

# Q5:
nums = []
for i in range(5):
    nums.append(int(input('Number:')))
for i in range(len(nums)-1):
    if abs(nums[i] - nums[i+1]) == 1:
        print('Following Numbers !')

nums.insert(0, 3)
nums.insert(1, int(input('Num:')))
nums.insert(2, nums[0]+nums[1])
nums.insert(3, nums[0]*nums[1]*nums[2])
print(nums)

