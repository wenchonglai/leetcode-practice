# A. Boredom
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.
# Given a sequence a consisting of n integers. The player can make several steps.
# In a single step he can choose an element of the sequence (let's denote it a[k]) and delete it, at that all elements equal to a[k] + 1 and a[k] - 1 also must be deleted from the sequence.
# That step brings ak points to the player.
# Alex is a perfectionist, so he decided to get as many points as possible. Help him.
# Input
# The first line contains integer n (1 <= n <= 10e5) that shows how many numbers are in Alex's sequence.
# The second line contains n integers (each between 1 and 10e5)
# Output
# Print a single integer - the maximum number of points that Alex can earn.
# input
# 2
# 1 2
# output
# 2
# input
# 3
# 1 2 3
# output
# 4
# input
# 9
# 1 2 1 3 2 2 2 2 3
# output
# 10

from collections import defaultdict
def getMax(n, arr):
  h = defaultdict(int)
  
  for num in arr:
    h[num] += 1
    
  keys = sorted([key for key in h])
  
  sums = [0, 0, 0]
  
  for i in range(0, len(keys)):
    val = h[keys[i]] * keys[i]
    
    sums.append(max(sums[-3], sums[-2]) + val)
  
  return max(sums[-3:])


print(getMax(3, [1,2,3]))
