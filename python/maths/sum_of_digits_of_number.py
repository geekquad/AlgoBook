#Approach 1

number = int(input('Enter the number to get the sum of digits : '))

sum_of_digits = sum(int(digit) for digit in str(number))

print("Sum of all digits of {} is: {}".format(number,sum_of_digits))


#Approach 2 

number = int(input("Enter a Number: ")) 
sum_of_digits = 0 
num = number
while number > 0: 
    rem = number % 10 
    sum_of_digits += rem 
    number = int(number/10)

print("Sum of all digits of {} is: {}".format(num,sum_of_digits))



#Sum of float no. 
number = float(input('Enter the number to get sum of the digits : '))

sum_of_digits = 0
for digit in str(number):
    if digit == '.':
        continue 
    sum_of_digits += int(digit)

print("Sum of all digits of {} is: {}".format(number,sum_of_digits))


