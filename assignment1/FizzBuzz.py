from tkinter import N


num=int(input("enter your number"))
if(num%3==0 and num%5==0):
    print("FizzBuzz")
elif(num%3==0):
    print("Fizz")
elif(num%5==0):
    print("Buzz")    