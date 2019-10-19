def Maior(nums):
    maior1 = (nums[0]+nums[1]+abs(nums[0]-nums[1]))/2
    maior2 = (nums[1]+nums[2]+abs(nums[1]-nums[2]))/2
    return "%.0f"%((maior1+maior2+abs(maior1-maior2))/2)
print(Maior(list(map(int, str(input()).split())))+" eh o maior")

