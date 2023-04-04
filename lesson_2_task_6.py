lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

n = len(lst)-1
for i in range(0,n): 
    if lst[i] % 3 ==0 and lst[i] < 30:
        print(lst[i])