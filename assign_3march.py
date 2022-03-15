# b = [34, 5, 2, 65, 4]
# b.sort()
# print("ascending sorted list is", b)
# b.sort(reverse=True)
# print("descending sorted list is", b)


# my_dict = {0:10, 1:20}
# print(my_dict)
# my_dict.update({2:30})
# print(my_dict)



# my_dict = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
# print("The given dictionary : ",my_dict)
# check_key = "Fri"
# if check_key in my_dict:
#    print(check_key,"is Present.")
# else:
#    print(check_key, " is not Present.")


# my_list = [2, 4, 10, 20, 5, 2, 20, 4]
# print("unique elements are",list(set(my_list)))



string = input("Enter the string: ")
w = ''
length = 0

for word in string.split():
    if (len(word) > length):
        length = len(word)
        w = word
print("Longest word is ", w)