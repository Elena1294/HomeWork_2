def is_divided(num):
    if num % 3 ==0: 
        for x in range(1,num+1): print(x) 
        print("Fizz")
    if num % 5 ==0: 
        for x in range(1,num+1): print(x) 
        print("Buzz")
    if (num % 3 ==0) and (num % 5 ==0): 
        for x in range(1,num+1): print(x) 
        print("FizzBuzz")

try:
    num = int(input("Введите число: "))
except ValueError: 
    print("Это не число.")
is_divided(num)
