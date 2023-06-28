text = input("dime una palabra: ")
split = list(text)
split.reverse()

if(list(text) == split):


    print(split)

    print("tu palabra es palindrome")


else:
    print("tu palabra no es palidrome")  

print(text)
print("".join(split))
