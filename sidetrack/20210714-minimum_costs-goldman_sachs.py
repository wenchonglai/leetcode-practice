# There is a shop, where vendors sell items. They all sell same item but they can change the price of the item during the day
# Given intervals of time and a lower price for the item during this interval for each vendor
# calculate the cheapest price for the item during the day within different time intervals. Input data for each vendor is {startTime, endTime, price}.
# For example for 3 vendors in the shop: [{0, 4, 5}, {2, 8, 3}, {7, 11, 10}], the result should be[{0, 2, 5}, {2, 8, 3}, {8, 11, 10}]

from heapq import heappop, heappush

def min_costs(intervals):
  N = len(intervals)

  if N < 2:
    return intervals

  h = []
  s1 = sorted([(tup[0], tup[2]) for tup in intervals])
  s2 = sorted([(tup[1], tup[2]) for tup in intervals])
  res = []

  i1, i2 = 0, 0
  t = s1[0][0]

  while i2 < N:
    if i1 < N:
      (t1, p1) = s1[i1]

    (t2, p2) = s2[i2]
    
    if i1 < N and t1 < t2:
      if h and p1 < h[0]:
        res.append((t, t1, h[0]))
        t = t1
        
      i1 += 1
      heappush(h, p1)
    else:
      p = heappop(h)
      
      if not h or h != h[0]:
        res.append((t, t2, p2))
        t = t2

      i2 += 1

      

  return res


print(min_costs([(3,14,15), (9,26,53), (5,8,9), (7,9,2)]))
