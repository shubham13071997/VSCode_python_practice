# 1.Factorial number
# 2.Palindrome Number
# 3. Armstrong no
# 4. Star program
# 5.Fibonacci



# To take input from the user
num = int(input("Enter a number: "))

factorial = 1  # fact it is compulasory to assign fact=1

# check if the number is negative, positive or zero
if num <= 0:
   print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):  # i =1, now if i =2,i=3
       factorial = factorial*i  # 1= 1*1 =1 means 1 fact 1, now fact =1, 1*2 =2, so fact 2 is 2, now fact 2=2*3=6 and fac3=6
   print("The factorial of",num,"is",factorial)
        