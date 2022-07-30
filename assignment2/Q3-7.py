for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        pass
    elif fizzbuzz % 3 == 0:
        print("fizz")
        pass
    elif fizzbuzz % 5 == 0:
        print("buzz")
        pass
    else:
        print(fizzbuzz)
