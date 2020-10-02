import math

arr_denom = []

numerator = int(input("Enter the numerator"))
denominator = int(input("Enter the denominator"))

if denominator == 0:
    print("Invalid Input")

else:
    while numerator != 0:

        flag = math.ceil(denominator/numerator)
        arr_denom.append(flag)

        numerator = flag*numerator-denominator
        denominator = denominator * flag

    for i in range(len(arr_denom)): 
        if i != len(arr_denom) - 1: 
            print(" 1/{0} +" .  format(arr_denom[i]), end = " ") 
        else: 
            print(" 1/{0}" . format(arr_denom[i]), end = " ") 
