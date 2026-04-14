#Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”

word = str(input("What word do you want to figure out?"))

for i in word:
    if i == "a":
        break
    print(i)