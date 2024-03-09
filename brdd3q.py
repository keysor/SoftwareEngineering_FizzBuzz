def fizzbuzz(n = 100): # default value of 100
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz") # if i is divisible by 3 and 5 print FizzBuzz
        elif i % 3 == 0:
            print("Fizz") # if i is divisible by 3 print Fizz
        elif i % 5 == 0:
            print("Buzz") # if i is divisible by 5 print Buzz
        else:
            print(i) # if i is not divisible by 3 or 5 print i

fizzbuzz(int(input("Enter a number for fizzbuzz: "))) # calls the function and asks for users input
