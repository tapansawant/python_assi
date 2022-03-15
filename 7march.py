# import operator
# text_line = input("Type in: ")
#
# freq_dict = {}
#
# for i in text_line.split(' '):
#     if i.isalpha():
#         if i not in freq_dict:
#             freq_dict[i] = 1
#         elif i in freq_dict:
#             freq_dict[i] = freq_dict[i] + 1
#     else:
#         pass
#
# sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
# print(sorted_freq_dict)
#
# for i in sorted_freq_dict:
#     print(i[0], i[1])


'''d = dict()
s = input("Enter the string:")
for i in s.split():
    d[i] = d.get(i, 0) + 1
#print(d)
sorted(d.items())
for i in d:
    print(i[0], i[1])'''

'''
def frequency(input):
    freq = {}

    for word in input.split():
        freq[word] = freq.get(word, 0) + 1

    words = list(freq.keys())
    words.sort()

    for w in words:
        print(f'{w}:{freq[w]}')


str = input('enter string: ')
frequency(str)
'''




'''str = input("Enter a string: ")

count = 0
for s in str:
    count = count + 1
print("Length of the string is:", count)
'''


'''def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True



str = input('Enter string ')
print(isPalindrome(str))'''




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:")
print(my_list)
print("\nSquare:")
square_my_list = list(map(lambda x: x ** 2, nums))
print(square_my_list)
print("\nCube:")
cube_my_list = list(map(lambda x: x ** 3, nums))
print(cube_my_list)




