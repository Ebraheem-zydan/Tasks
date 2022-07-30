num=int(input("enter a number"))
toggle=0
while(num>0):
    toggle=toggle*10+num%10
    num=num/10
if toggle==num:
    print("num is palindrom")
else:
    print("num isn't a palindrome!")