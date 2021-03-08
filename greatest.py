print("-"*30)
print("   GREATEST AMONG NUMBERS    ")
print("-"*30)

nums = []
_input_ = 0
l = 1

while _input_!="x":
    nums.append(int(_input_))
    _input_ = input("num%d==>"%l)
    if _input_=="":break
    l +=1
    
count = 0
greatest = 0
for i in nums:
    for j in range(len(nums)):
        if i>=nums[j]:
            count += 1
    
    if count==len(nums):
        greatest = i
        break
    count = 0
        
print("="*30)
print("Greatest",nums[1:],"==>",greatest)
print("="*30)

