 input = input("Enter the input ")
 print(input.isnumeric())


# a = 'Hi i am tapan here tapan i am'
# b = []
#
# for w in a.split():
#     if w not in b:
#         b.append(w)
#
# print(b)


# string=input("Enter string:")
# string=string.replace(' ','#')
# print("Modified string:")
# print(string)



# print("Enter the String:")
# text = input()
#
# vowela = ['a', 'A']
# vowele = ['e', 'E']
# voweli = ['i', 'I']
# vowelo = ['o', 'O']
# vowelu = ['u', 'U']
# ca = 0
# ce = 0
# ci = 0
# co = 0
# cu = 0
#
# for x in text:
#     if x in vowela:
#         ca = ca+1
#     elif x in vowele:
#         ce = ce+1
#     elif x in voweli:
#         ci = ci+1
#     elif x in vowelo:
#         co = co+1
#     elif x in vowelu:
#         cu = cu+1
#
# print("\n'a' occurs ", ca)
# print("'e' occurs ", ce)
# print("'i' occurs ", ci)
# print("'o' occurs ", co)
# print("'u' occurs ", cu)


string = "Tapan Dattatray sawant";
word = "";
words = [];

# Add extra space after string to get the last word in the given string
string = string + " ";

for i in range(0, len(string)):
    # Split the string into words
    if (string[i] != ' '):
        word = word + string[i];
    else:
        # Add word to array words
        words.append(word);
        # Make word an empty string
        word = "";

    # Initialize small and large with first word in the string
small = large = words[0];

# Determine smallest and largest word in the string
for k in range(0, len(words)):

    # If length of small is greater than any word present in the string
    # Store value of word into small
    if (len(small) > len(words[k])):
        small = words[k];

        # If length of large is less than any word present in the string
    # Store value of word into large
    if (len(large) < len(words[k])):
        large = words[k];

print("Smallest word: " + small);
print("Largest word: " + large);