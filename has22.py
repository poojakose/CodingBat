def has22(nums):
  result = False
  for i in range(len(nums)):
    if nums[i] == 2 and (i>0 and nums[i-1]) == 2:
      result = True
  return result  

#################### OR ####################

def Mhas22(nums):
  for i in range(len(nums)-1):
      if nums[i] ==2:
        if nums[i] == nums[i+1]:
          return True
  return False
