import math

# Q1:
def even_or_odd_numbers():
    num1 = int(input('Type Number:'))
    if num1 % 2 == 0:
        return 'This Even Number!'
    else:
        return 'This Odd Number!'

# Q2:
def average(num1, num2, num3):
    sum_nums = num1 + num2 + num3
    avg = sum_nums / 3
    print('The Average is:')
    return round(avg, 3)

# Q3:
def len_number():
    num = input('Enter Number, Or Press -999 to Exit !:')
    while num != '-999':
        len_number1 = len(num)
        print('The len of the number is:', len_number1)
        num = input('Another Number:')
    print('End Of The Program !')

# Q4:
def change(price):
    change20 = price // 20
    change10 = (price - change20 * 20) // 10
    change5 = (price - change20 * 20 - change10 * 10) // 5
    change1 = (price - change20 * 20 - change10 * 10 - change5 * 5) // 1
    print(20, '**', change20)
    print(10, '**', change10)
    print(5, ' **', change5)
    print(1, ' **', change1)

# Q5:
def cal_power(num1, num2):
    result = num1 ** num2
    print('The Result Of Power is:')
    return result

# Q6:
def above_1000(price):
    sale = price * 0.35
    result1 = price - sale
    print('Favorite Customer, You get a Discount of 35% , The New Price is:  :')
    return round(result1, 3)
def sale_price():
    price = int(input('Enter Price:'))
    if price >= 1000:
        call_function = (above_1000(price))
        return round(call_function, 3)
    else:
        answer = price * 0.10
        result2 = price - answer
        print('You get Discount of 10% , The New Price is::')
        return result2

# Q9:
def result_of_pow(num1, num2):
    print('The result of Pow:')
    return num1 ** num2

def result_of_sqrt(num1, num2):
    result = math.sqrt(num1) - math.sqrt(num2)
    print('The result of sqrt:')
    return result

def big_divider(x, y):
    empty_ls = []
    for i in range(1, y+1):
        if x % i == 0 and y % i == 0:
            empty_ls.append(i)
    print('The biggest Divider:')
    return max(empty_ls)

def smallest_divider(num1, num2):
    empty_list2 = []
    for i in range(1, num2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            empty_list2.append(i)
        print('The Smallest Divider:')
        return min(empty_list2)

def user_program():
    num1 = int(input('Enter First Number:'))
    num2 = int(input('Enter Second Number:'))
    menu = input('''Welcome,\n"a" for Biggest Divider\n"b" for Smallest Divider\n"c" for sqrt\n"d" for Pow\n"e" for exit
Select Program: ''')
    if menu == 'a':
        print(big_divider(num1, num2))
    elif menu == 'b':
        print(smallest_divider(num1, num2))
    elif menu == 'c':
        print(result_of_pow(num1, num2))
    elif menu == 'd':
        print(result_of_sqrt(num1, num2))
    elif menu == 'e':
        print('End Of the Program')
    else:
        print('Wrong Choice')


# Q11:
def print_id(customer):
    print('Give to', customer, 'Special Care')
def books():
    customer_id = input('Customer ID:')
    commodity_value = int(input('Enter The Price:'))
    pay_on_time = int(input('You pay The bills on time ?, |"0" = No | "1" = Yes|'))
    num_of_years = int(input('Number Of Years:'))
    if pay_on_time == 1:
        return print_id(customer_id)
    if commodity_value > 8000 and num_of_years > 5:
        return print_id(customer_id)
    else:
        return 'Regular Care To The Customer !'
