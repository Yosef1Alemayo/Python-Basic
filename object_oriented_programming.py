# this is Test on OOP:
# Q1:
class Circle:
    def __init__(self, color, area=25):
        self.__color = color
        self.__area = area

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def __str__(self):
        return self.__color + ' ' + str(self.__area)


class Square:
    def __init__(self, color='Black', area=25):
        self.__color = color
        self.__area = area

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def __str__(self):
        return self.__color + ' ' + str(self.__area)


circle1 = Circle('Green')
circle2 = Circle('Yellow', 65)
print(circle1, '\t', circle2)
print(circle1.get_area())

square1 = Square()
square2 = Square('Grey', 56)
square1.set_color('Pink')
print(square1, '\t', square2)
print(square2.get_area())

# Q2:
class Apartment:
    def __init__(self, address, house_number, price, price_for_rent):
        self.__address = address
        self.__house_number = house_number
        self.__price = price
        self.__price_for_rent = price_for_rent

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_price_for_rent(self):
        return self.__price_for_rent

    def set_price_for_rent(self, price_for_rent):
        self.__price_for_rent = price_for_rent

    def percentage_of_return(self):
        percentage = (self.__price_for_rent * 12) / self.__price * 100
        print('The Percentage of return is:')
        return percentage

    def __str__(self):
        return self.__address + ' ' + str(self.__house_number)+' '+str(self.__price)+' '+str(self.__price_for_rent)


apartment1 = Apartment('Rehovot', 106, 1500000, 4500)
apartment2 = Apartment('Lod', 55, 1260000, 3000)
print(apartment2.percentage_of_return())
print(apartment1.percentage_of_return())

# Q3:
class Cat:
    def __init__(self, name, age, hair_color):
        self.__name = name
        self.__age = age
        self.__hair_color = hair_color

    def cat_sound(self):
        sound = '~~ Meow ~~'
        return sound

    def cat_mustache(self):
        answer1 = 'The cat has a mustache.'
        answer2 = "The cat doesn't have a mustache."
        if self.__age >= 9:
            return answer1
        else:
            return answer2

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_hair_color(self):
        return self.__hair_color

    def set_hair_color(self, hair_color):
        self.__hair_color = hair_color

    def __str__(self):
        return self.__name + ' ' + str(self.__age) + ' ' + self.__hair_color

class Dog:
    # Constractor in the Function:
    def __init__(self, name, breed, color='Black'):
        self.__name = name
        self.__breed = breed
        self.__color = color

# Main Functions in the Program:
    def dog_sound(self):
        sound = '~~ Woof ~~'
        return sound

    def bite_dog(self):
        answer1 = 'The Dog can Bite You , Be Carefully'
        answer2 = 'The Dog is not bite , Its Ok '
        if self.__breed == 'Pit-bull':
            return answer1
        else:
            return answer2
# Get & Set Functions:
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
# Delete Function:
    def delete_parameters(self, parameter):
        default = 'Wrong Choice'
        if parameter == 'name' or 'Name':
            self.__name = None
        elif parameter == 'breed' or 'Breed':
            self.__breed = None
        elif parameter == 'color' or 'Color':
            self.__color = None
        else:
            return default

    def __str__(self):
        return self.__name + ' ' + self.__breed + ' ' + self.__color


cat1 = Cat('Dan', 20, 'Red')
cat2 = Cat('Ran', 1, 'Pink')
dog1 = Dog('Kia', 'Pit-bull', 'Black')
dog2 = Dog('Lucky', 'Pincher', 'White')

# Cat1 :
print('Cat name:', cat1.get_name(), '\nCat sound:', cat1.cat_sound(), '\nCat mustache:', cat1.cat_mustache())

# Cat2:
print('Cat name:', cat2.get_name(), '\nCat sound:', cat2.cat_sound(), '\nCat mustache:', cat2.cat_mustache())

# Dog1:
print('Dog name:', dog1.get_name(), '\nDog breed:', dog1.get_breed(), '\nThe dog Bite ? --------:', dog1.bite_dog())

# Dog2:
print('Dog name:', dog2.get_name(), '\nDog breed:', dog2.get_breed(), '\nThe dog Bite ? --------:', dog2.bite_dog())

# Set Name:
dog1.set_color('Brown')
print(dog1.get_color())

# Add To the Class Features:
dog1.set_color('Black')
print(dog1.get_color())
print(dog1.get_name())
# Delete Features from Class:
dog1.delete_parameters('color')
dog1.delete_parameters('Name')
print(dog1.get_name())

# Q4:
class Car:
    def __init__(self, model, color, price):
        self.__model = model
        self.__color = color
        self.__price = price

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        car_print = 'Car Model: {} \nThe color is: {} \nThe Price is: {}'\
        .format(self.__model, self.__color, str(self.__price))
        return car_print


car1 = Car('Skoda', 'Black', 55000000000)
car2 = Car('Mercedes', 'Grey', 250000000000000)
car3 = Car('Honda', 'White', 3000000000)
car4 = Car('Seat', 'Red', 65000000000000)
#
# # Return the Details of The Expensive car:
cars = [car1, car2, car3, car4]

def max_number(list_name):
    max_num = 0
    for i in range(len(cars)-1):
        if cars[i].get_price() > cars[i+1].get_price():
            max_num = cars[i]
        else:
            max_num = cars[i+1]
        return max_num


a = max_number(cars)
print(a)

# Q5:
class Student:
    def __init__(self, name, identity_document, math_grade, history_grade,
                 literature_grade,  birth_year, class_room='A'):
        self.__name = name
        self.__identity_document = identity_document
        self.__math_grade = math_grade
        self.__history_grade = history_grade
        self.__literature_grade = literature_grade
        self.__class_room = class_room
        self.__birth_year = birth_year

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_identity_document(self):
        return self.__identity_document

    def set_identity_document(self, identity_document):
        self.__identity_document = identity_document

    def get_math_grade(self):
        return self.__math_grade

    def set_math_grade(self, math_grade):
        self.__math_grade = math_grade

    def get_history_grade(self):
        return self.__history_grade

    def set_history_grade(self, history_grade):
        self.__history_grade = history_grade

    def get_literature_grade(self):
        return self.__literature_grade

    def set_literature_grade(self, literature_grade):
        self.__literature_grade = literature_grade

    def get_birth_year(self):
        return self.__birth_year

    def set_birth_year(self, birth_year):
        self.__birth_year = birth_year

    def get_class_room(self):
        return self.__class_room

    def set_class_room(self, class_room):
        self.__class_room = class_room

    def cal_age(self):
        age = 2022 - self.__birth_year
        return age

    def cal_avg(self):
        avg = (self.__math_grade + self.__literature_grade + self.__history_grade) // 3

        return avg

    def __str__(self):

        if self.cal_avg() <= 60:
            return 'Name' + ' : ' + self.__name + '\nID : ' + self.__identity_document\
                   + '  ' + '\nThe Grades are : ' + ' ' + str(self.__math_grade)\
                   + '  ' + str(self.__history_grade) + ' ' + str(self.__literature_grade)\
                   + ' ' + '\nThe Average is : ' + str(self.cal_avg())\
                   + '\nPass/Failed : Failed'

        elif self.cal_avg() >= 90:
            return 'Name' + ' : ' + self.__name + '\nID :'+' : ' + self.__identity_document \
                   + '  ' + '\nThe Grades are : ' + ' ' + str(self.__math_grade) \
                   + '  ' + str(self.__history_grade) + ' ' + str(self.__literature_grade) \
                   + ' ' + '\nThe Average is : ' + str(self.cal_avg()) \
                   + '\nPass/Failed : Passed with distinction'

        else:
            return 'Name' + ' : ' + self.__name + '\nID : ' + self.__identity_document \
                   + '  ' + '\nThe Grades are : ' + ' ' + str(self.__math_grade) \
                   + '  ' + str(self.__history_grade) + ' ' + str(self.__literature_grade) \
                   + ' ' + '\nThe Average is : ' + str(self.cal_avg()) \
                   + '\nPass/Failed : Passed'


student1 = Student('Moshe', '205252525', 100, 15, 93, 1996)
student2 = Student('Avi', '56856856', 100, 900, 100, 1990, 'B')
student3 = Student('David', '147852963', 40, 20, 110, 2002, 'C')
student4 = Student('Yosef', '321654987', 100, 100, 100, 1996, 'Tech-Career')
student5 = Student('Natan', '145236985', 70, 70, 90, 1996)


students = [student1, student2, student3, student4, student5]

def max_avg(list_name):
    maxima_avg = 0
    for i in range(len(students)-1):
        if students[i].cal_avg() > students[i+1].cal_avg():
            maxima_avg = students[i]
        else:
            maxima_avg = students[i + 1]
        return maxima_avg


print(max_avg(students))
