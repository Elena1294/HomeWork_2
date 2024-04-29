try:
    num = int(input("Введите число: "))
except ValueError: 
    print("Это не число.")
is_divided(num)

def is_divided(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif (i % 5 == 0):
        elif i % 5 == 0:
            print("Buzz")
        elif ((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz")
        else:
            print(i)


num = int(input("Введите число: "))
n = int(input("Введите число: "))

is_divided(num)
is_divided(n)