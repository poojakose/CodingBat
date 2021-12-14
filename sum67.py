def sum67(nums):
  flag = False
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 6:
      flag = True
      continue
      
    if flag == True and nums[i] == 7:
      flag = False
      continue

    if flag== False:
      sum += nums[i]
  
  return sum

############## OR ###################

def Msum67(nums):
  flag=False
  sum=0
  for num in nums:
    if(num==6):               
        flag=True
        continue
    if(num==7 and flag is True): 
        flag=False
        continue
    if(flag is False):         
       sum+=num
  return sum


