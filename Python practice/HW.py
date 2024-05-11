
# Count  -- list.count(value)

# A = ("gchjewc gfce cgcbec egkc e negj") 
# B= ("eg")

# print(len(A))

# print(A.count(B))


# 1 . Write a Python program to replace the last value of tuples in a list.

# Sample_list = [( 10, 20, 40), (40, 50, 60), (70, 80, 90)]

# for i in range(len(Sample_list)):

#  Test = list(Sample_list[i])
#  Test [-1]= 100
#  Sample_list[i] =tuple(Test)

# print(Sample_list)

# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


# 2. Write a Python program to remove an empty tuple(s) from a list of tuples.

# datas = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# test = [tup for tup in datas if tup]
# print(test)


# # By For loop
# filtered_data = []

# # Iterate over each tuple in data
# for tup in datas:
#     # Check if the tuple is not empty
#     if tup:
#         # If not empty, append it to filtered_data
#         filtered_data.append(tup)

# print(filtered_data)

# By Slicing
# data=datas[2:]
# print(data)

# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']




# 3. Write a Python program to sort a tuple by its float element.


Test_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

sorted_data = sorted(Test_data, key=lambda x: float(x[1]), reverse=True)

print(sorted_data)



# for i in range(len(Sample_list)):

#  Test = list(Sample_list[i]))
# for i in range(len(Test_data)):

#  Tests = list(Test_data[i])
#  print(Tests)
#  Sort_data = Tests.sort
#  print (Sort_data)

# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
