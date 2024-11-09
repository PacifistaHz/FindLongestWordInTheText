from array import array

text=input("Enter a string: ")
dictionary={}
longestWordLength=0
longestWord=""

arrayWords=text.split(" ")

for i in arrayWords:
    dictionary[i]=len(i)

for i in dictionary:
    if dictionary[i]>longestWordLength:
        longestWordLength=dictionary[i]
        longestWord=i
print("The Longest Word Length is "+str(longestWordLength))
print("The Longest Word is "+longestWord)