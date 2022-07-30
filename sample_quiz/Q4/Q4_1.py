import string 
import random
letters_lowerCase=list(string.ascii_lowercase)
letters_uperCase=list(string.ascii_uppercase)
digits=list(string.digits)

def generatePassword():
    while True:
        try:
            passwordLength = int(passwordLength)
            if passwordLength < 8 :
                print("Sorry password must be at least 8 chars")
                passwordLength = int(input('Enter password length : '))
            break
        except:
            print('Please enter numbers only ...')
            passwordLength = int(input('Enter password length: '))

    password = []
    random.shuffle(letters_uperCase) 
    random.shuffle(letters_lowerCase)  
    random.shuffle(digits)   

    for i in range(round(passwordLength * .4)):
        password.append(letters_uperCase[i])

    for i in range(round(passwordLength * .3)):
        password.append(letters_lowerCase[i])

    for i in range(round(passwordLength * .3)):
        password.append(digits[i])
    

    if(len(password)<passwordLength):
        password.append(letters_uperCase)
    if (len(password)>passwordLength):
        del password[-1]
    password = "".join(password[0:])
    print(len(password))

    print(f"Your password is : \n  {password}")


generatePassword()    