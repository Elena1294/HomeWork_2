def bank (x,y):
    S = x;
    for x in range(0,y):
        S=S/100.0*0.1+S 
    print("Итоговый доход за весь срок: " + str(S))
try:
    x = float(input("Введите размер вклада: "))
except ValueError: 
    print("Это не число.")
try:
    y = int(input("Введите срок кредитования, лет: "))
except ValueError: 
    print("Это не число.")
bank(x,y)
