def centered_average(nums):
  minVal, maxVal = nums[0], nums[0]
  sum = 0
  for num in nums:
    minVal = min(minVal, num)
    maxVal = max(maxVal, num)
    sum += num
  return ((sum-minVal-maxVal)/(len(nums)-2))
