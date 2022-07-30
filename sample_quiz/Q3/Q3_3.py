def Fibonacci():
    a,b,sum=0,1,0
    print(a)
    print(b)
    for counter in range(8):
        sum=a+b
        a=b
        b=sum
        print(sum)
Fibonacci()