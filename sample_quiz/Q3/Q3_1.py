def vowels(string):
    counter=0
    list=['A','a','E','e','O','o','U','u','I','i']
    for char in string:
        for i in range(10):
            if char==list[i]:
                counter = counter + 1
                break
    return counter            
string_input=input("enter a string : ")
print(vowels(string_input))              