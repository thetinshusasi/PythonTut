import  print_module
# print("hi this is tinshu")
# message = "hi i am master"
# print(message)
# message = input()
# print(message)
# print(message.title())
# firstName = "tinshu"
# lastName = "Sasi"
# fullName = firstName + " " + lastName
# print(fullName)
# name = "tinshu "
# print(name.rstrip().__len__())
# print(name.__len__())
# # to remove it permanently
# name= name.rstrip();
# print(name.__len__())

# age = 20;
# msg = 'happy ' + str(age) + ' Birthday'
# print(msg)
#
# data = 3/2
# print(data)
# import  this
# msg = 'tinshu'
# msg = msg.title()
# print(msg)
firstList = [1, 2, 3, 4.9,  6]
# print(firstList)
# print(firstList[0])
# # gives you the last element in the array
# print(firstList[-1])
# firstList[2] = 100
# print(firstList)
# firstList.append(300)
# print(firstList)
# firstList.insert(1,500)
# print(firstList)
# del firstList[1]
# print(firstList)
# ele = firstList.pop()
# print(ele)
# print(firstList)
# ele1 = firstList.pop(0)
# print(ele1)
# print(firstList)
# firstList.remove('ko')
# print(firstList)
# firstList.sort()
# firstList.sort(reverse=True)
# print(firstList)
# print(sorted(firstList))
# print(len( firstList))
# for item in firstList:
#     print('here is the item : ' + str(item))
#     print('what is the value in item : ' + str(item))
#
# even_number = list(range(2,11,2))
# print(even_number)
#
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# # list comprehension
# squares = [value**2 for value in range(1,11)]
# print(squares)
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])
#
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print(friend_foods)
# alien = {'color': 'green', 'points': 5}
# print(alien)
# x = alien['color']
# print(x)
# x = 'ghost'
# print(x)
# print(alien)
#
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# print(user_0.items())
# data = user_0.items()
# print(data)
# # for key, value in user_0.items():
# #     print("\nKey: " + key)
# #     print("Value: " + value)
# name = input("Please enter your name: ")
# print(name)

# def print_name(name):
#     # hohoho
#     """" dead man walking
#     :rtype: object
#     """
#     print(name)

#
# print_module.print_values(1 ,2 ,4 ,5 ,5)
# my_new_car = print_module.Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_tesla = print_module.ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

with open("digits.txt") as file_obj:
    contents = file_obj.read()
    print(contents)