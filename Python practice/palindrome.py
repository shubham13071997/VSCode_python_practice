# # Palindrome means Revere of string

# # We can do Palindrome by 2 ways:
# # 1.By Reverse string

# # A = input("Enter a name ")

# # Rev = A[::-1]
# # print(Rev)



# # if A==Rev:
# #     print ("It is A palindrome")
# # else:
# #   print("It is not palindrome")



  ### By number#3

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

 
# List_test =[2,3,4,6]
# R =tuple(List_test)
# print(R)