# Program to print first N UGLY NUMBERS

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

N = int(input("Enter the number"))
list = []
i=1
num=1
while N >= i:
    if (ugly_num(num) == 1):
        list.append(num)
        i+=1
    num+=1
    
for i in range(len(list)):
    print(list[i])