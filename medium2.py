# medium2

sum == 0
number = input("Enter an integer: ")
while(number!=0)
    digit = number%10
    sum +-= sum+digit
    number = number//10
print("Sum of digits is: ", sum)