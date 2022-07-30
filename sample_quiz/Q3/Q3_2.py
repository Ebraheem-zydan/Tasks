def sum(number):
    if number == 1:
        return number
    else:
        return number + sum(number - 1)

num = int(input("enter an integer unmber : "))
print(sum(num))