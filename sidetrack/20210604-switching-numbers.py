# Given an Array, find the length of the longest switching numbers sequence
# Switching numbers sequence is an array with all even index the same and all odd index the same.  e.g. [2,-4,2,-4], [5,5,5]
# Test Cases:
# [7, 4, -2, 4, -2, -9] => 4
# [7, 7, 7, 4, -2, 4, -2, -9] => 4
# [7, 4, -2, 4, -9] => 3
# [7, 4, -2, 4, -2, -9, -2, -9, -2] => 5
# [1, 2, 3, 4, 5] => 2
# [3, 3, 3, 4, 5] => 3

def longestSwitchingNumbers(arr):
  N = len(arr)

  if N <= 2:
    return N

  saved_num = arr[0]
  left = 0
  res = 2

  for i in range(2, N):
    if arr[i] != arr[i - 2]:
      left = i - 1
    
    if i - left + 1 > res:
      res = i - left + 1
  
  return res


print(longestSwitchingNumbers([7, 4, -2, 4, -2, -9])) # => 4
print(longestSwitchingNumbers([7, 7, 7, 4, -2, 4, -2, -9])) # => 4
print(longestSwitchingNumbers([7, 4, -2, 4, -9])) # => 3
print(longestSwitchingNumbers([7, 4, -2, 4, -2, -9, -2, -9, -2])) # => 5
print(longestSwitchingNumbers([1, 2, 3, 4, 5])) # => 2
print(longestSwitchingNumbers([3, 3, 3, 4, 5])) # => 3
print(longestSwitchingNumbers([16,18,19,11,3,17,10,18,11,10,15,2,16,7,13,10,7,17,6,3,5,17,14,1,12,16,13,1,8,5,12,2,1,11,2,11,8,6,11,8,1,5,3,9,18,19,15,15,5,9,15,14,12,17,17,4,19,16,17,9,16,16,0,0,8,5,7,11,2,19,1,14,4,10,19,6,16,12,3,1,10,3,15,0,0,16,18,5,1,10,7,12,13,19,18,18,4,13,6,10,6,14,15,17,19,3,6,6,18,11,2,2,5,4,4,0,0,9,12,5,17,0,8,16,2,3,1,9,7,13,5,14,6,18,16,3,19,17,16,17,11,15,5,18,13,19,13,5,16,13,3,12,17,19,8,9,12,12,13,5,6,11,14,7,0,12,3,17,6,1,12,15,2,1,16,11,19,18,17,19,18,14,6,9,16,17,4,1,2,13,10,0,0,4,13,7,2,2,3,12,13,14,10,10,6,7,7,13,7,18,9,5,7,18,6,1,16,9,6,13,5,17,17,17,16,4,10,2,16,17,3,12,18,12,1,9,8,11,14,11,1,6,17,18,14,18,3,18,7,18,8,12,0,16,17,10,2,6,2,7,2,19,14,16,7,7,18,4,14,0,19,6,15,1,16,13,6,2,14,8,17,16,0,13,9,4,5,3,14,18,8,7,2,0,7,14,17,6,6,8,18,15,15,19,15,10,18,5,15,10,6,10,2,1,2,12,3,10,8,1,6,15,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,12,6,2,4,11,4,12,18,8,7,0,17,17,1,8,6,14,9,3,5,9,2,6,15,4,14,3,18,8,10,16,8,9,8,4,12,14,12,18,0,10,18,5,1,11,16,2,16,3,16,14,14,18,9,6,15,15,15,17,0,16,1,2,10,13,13,8,5,16,12,17,18,16,12,1,14,5,2,11,6,5,12,8,16,13,10,14,1,14,19,16,0,4,11,8,15,19,15,17,10,13,3,8,15,3,16,3,0,5,9,1,12,3,8,19,16,14,5,13,3,17,2,6,9,2,1,9,13,14,14,8,17,0,17,3,16,8,4,11,14,6,14,6,4,8,5,11,4,3,3,14,2,8,5,14,6,7,19,18,0,16,0,17,0,7,17,11,12,4,2,17,14,13,10,14,8,13,2,6,3,2,0,14,2,10,0,6,11,14,14,10,8,2,1,1,4,8,9,12,4,6,18,16,19,19,7,14,7,1,14,5,1,2,17,16,4,0,2,18,4,11,14,3,1,12,10,1,14,7,1,1,3,8,0,14,14,3,5,5,12,5,4,16,12,6,8,8,0,8,10,15,16,4,0,14,16,13,16,3,1,17,8,5,15,13,5,9,6,14,17,5,10,4,3,9,16,5,8,7,0,13,3,16,14,18,14,8,2,14,19,2,5,16,7,7,15,13,3,12,17,17,0,16,15,2,8,8,19,17,4,11,16,6,4,17,7,4,0,12,19,18,10,8,13,14,6,0,13,2,19,9,3,13,8,10,18,17,3,4,0,6,19,7,12,6,14,15,7,13,4,13,5,9,6,3,16,0,16,15,8,19,9,15,17,19,16,7,6,11,15,13,6,14,10,17,2,16,13,19,14,11,0,0,1,10,19,17,17,19,14,16,12,3,7,8,7,0,2,19,12,8,7,4,8,7,0,11,16,12,3,19,5,1,9,13,14,2,0,9,16,13,0,8,18,18,2,10,4,2,3,11,14,12,13,9,3,18,11,7,6,9,2,1,18,3,11,19,4,1,1,4,5,0,18,4,2,0,9,9,15,4,14,9,15,1,3,14,13,4,10,11,18,15,6,9,2,17,9,18,13,2,12,17,3,12,8,8,15,10,13,4,16,15,15,6,18,13,15,7,13,7,13,6,19,11,3,1,9,17,8,5,3,3,12,1,11,0,8,13,16,16,14,12,16,10,12,6,3,11,1,9,5,3,16,2,11,15,3,18,9,9,14,7,7,0,17,11,3,10,18,18,18,15,12,15,15,19,6,1,15,18,0,18,19,6,7,13,15,17,14,5,5,3,17,12,7,13,5,4,14,19,6,10,0,8,0,6,10,11,0,13,8,12,7,3,1,5,10,10,14,11,3,16,4,5,8,11,12,4,15,16,16,2,0,17,2,1,1,9,9,5,5,11,14,17,12,18,15,8,5,10,15,16,13,7,17,11,8,17,4,6,14,17,6,6,8,1,0,3,0,16,0,14,17,10,1,2,8,12,2,8,16,3,15,3,3,19,14,2,6,7,16,2,9,8,5]))