import math 

def bank (x,y):
    S = x;
    for x in range(0,y):
        S += S *0.10
    print("Итоговый доход за весь срок: " + str(round(S, 2)))

try:
    x = float(input("Введите размер вклада: "))
except ValueError: 
    print("Это не число.")
try:
    y = int(input("Введите срок кредитования, лет: "))
except ValueError: 
    print("Это не число.")
    
bank(x,y)