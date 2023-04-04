def is_square(side):
    return round(side*side)
try:
    side = float(input("Введите сторону квадрата: "))
except ValueError: 
    print("Это не число.")
square = is_square(side)
print ("Площадь квадрата: "+ str(square)) 