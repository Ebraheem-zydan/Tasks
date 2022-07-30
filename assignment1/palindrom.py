check_string=input("enter yor string")
string=""
for i in check_string:
    string=i+string
if(string==check_string):
    print (check_string , "is a palindrom")    
else:
    print (check_string , "isn't a palindrom")