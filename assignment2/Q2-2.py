def sum(num1):
    def sum2(num2):
        return num1+num2
    return sum2    
print(sum(5)(12))