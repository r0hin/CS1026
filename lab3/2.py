# Write a program that reads a set of integer values. First, we ask the user for how many numbers they plan to enter, and then ask the user to enter the values, then print:

num = int(input("How many numbers do you want to enter? "))
print("Enter the numbers: ")
numbers = []
for i in range(num):
    numbers.append(int(input()))
print("The numbers are: ", numbers)

# a) The sum of the numbers
print("The sum of the numbers is: ", sum(numbers))

# b) The average of the numbers
print("The average of the numbers is: ", sum(numbers)/len(numbers))

# c) The largest and smallest values
print("The largest value is: ", max(numbers))
print("The smallest value is: ", min(numbers))

# d) The range of the numbers (the difference between the largest and smallest value)
print("The range of the numbers is: ", max(numbers)-min(numbers))
