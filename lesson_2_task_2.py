def is_year_leap(year):
    if year % 2 == 0: return True
    else: return False
try:
    year = int(input("Введите год: "))
except ValueError: 
    print("Это не число.")
is_Vis = is_year_leap(year)
print ("Год "+ str(year) + " " + str(is_Vis)) 