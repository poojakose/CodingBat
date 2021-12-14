def big_diff(nums):
  diff = 0
  large, small = nums[0], nums[0]
  for x in nums:
    large = max(large, x)
    small = min(small, x)
    diff = large - small
  return diff
    
