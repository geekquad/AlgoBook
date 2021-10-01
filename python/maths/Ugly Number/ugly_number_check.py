#Program to check whether a number is an UGLY NUMBER

def ugly_num(num):
    
    while num != 1:

        if num % 2 == 0:
            num//=2
        elif num % 3 == 0:
            num//=3
        elif num % 5 == 0:
            num//=5
        else:
            return num
    return num
    
num = int(input("Enter the number"))
m=num

if (ugly_num(num) == 1):
    print(m," is an Ugly Number")
else:
    print(num," is not an Ugly Number")