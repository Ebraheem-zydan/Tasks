list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
list_odd=[]
list_even=[]
for i in list1:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
for i in list2:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_even)
print(list_odd)