# f = []
# for i in 'python':
#     for j in 'learn':
#         f.append(i+j)
#
# print(f)
#
# for k in f:
#     f = k[1]
# f = list(f)
# print(f)
#
#
# a = ['tom', 'tapan', 'sandy']
# b = [83,24,76]
# my_dict = {}
# for i in range(3):
#     my_dict[i] = b[j]
#     list(tuple(my_dict[i]))
#
# print(my_dict)
#


# Assignments
# quw 1.

# i = 0
# sum = 0;
# while i <= 100:
#     sum = sum + i;
#     i += 1
# print(sum)


# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "":
#             new_list.append(list[i])
#         i = i+1
#     return new_list
#
# lst1=["Tapan", "Prathmesh","","Sawant", "Sandy", "johny"]
# i=0
# print(name_adder(lst1))


# lst1=["Phil", "Oz", "Seuss", "Dre"]
# lst2=[]
# for i in lst1:
#     lst2.append("Dr. " + i)
# print(lst2)
#


# lst1=[3.14, 66, "Teddy Bear", True, [], {}]
# lst2=[]
# for i in lst1:
#     lst2.append(type(i))
# print(lst2)


# num = int(input("enter no."))
#
# if num > 1:
#     for i in range(2, int(num / 2) + 1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")


# a = int(input("Number of classes held:"))
# b = int(input("Number of classes attended:"))
#
# per = b/a*100
#
# if per >= 75:
#     print("The student is allowed to sit in exam")
# else:
#     print("The student is not allowed to sit in exam")


# score = input("Enter your score")
# score = int(score)
# if score < 25:
#     print("F")
#
# elif score >= 25 and score < 45:
#     print("E")
#
# elif score >= 45 and score < 50:
#     print("D")
#
# elif score >= 50 and score < 60:
#     print("C")
#
# elif score >= 60 and score < 80:
#     print("B")
# else:
#     print("A")


# age1=int(input('enter age1: '))
# age2=int(input('enter age2: '))
# age3=int(input('enter age3: '))
# if age1>age2 and age1>age3:
#     print('age1 is oldest')
# elif age2>age1 and age2>age3:
#     print('age2 is oldest')
# else:
#     print('age3 is oldest')
# if age1<age2 and age1<age3:
#     print('age1 is youngest')
# elif age2<age1 and age2<age3:
#     print('age2 is youngest')
# else:
#      print('age3 is youngest')


# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("no. is Even")
# else:
#    print("no. is Odd")


# num = input("Enter a 4 digit number: ")
# if (len(num) == 4):
#     t = num.sort()
# if( num == t)
#     print("smallest")
# else
#     print("not smallest")


