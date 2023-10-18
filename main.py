nums = [0,1,2,3,0,4]
val = 2
print(nums)
for i,num in enumerate(nums): 
    if num == val:
        del nums[i]
print(len(nums))
print(nums)