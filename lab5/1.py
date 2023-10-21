nums = []
while len(nums) < 10:
    num = int(input("Enter a number: "))
    if num not in nums:
        nums.append(num)
    else:
        print("Number already in list.")

print(nums)