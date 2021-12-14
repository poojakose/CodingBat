def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1
    return total

def Msum13(nums):
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 13 or (i>0 and nums[i-1]==13):
      i += 2
      continue
    sum += nums[i]
  return sum
