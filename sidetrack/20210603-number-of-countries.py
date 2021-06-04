# Rectangular Map of N x M, each tile has a shade(5 different shades total).
# A country:
#     Has tiles of the same shade
#     Can travel from one tile to another orthogonally(up down, left right) without another shade being in the way
# How many countries are there?

# Test Case: 11 countries here

from collections import defaultdict

def countCountries(dp):
  N = len(dp)
  M = len(dp[0])
  i = 0
  indices = defaultdict(int)    # save the country index of a cell
  countries = defaultdict(int)  # save how many cells belong to a country index
  index_map = {0: 0}            # save which country a country represents

  for y in range(N):
    for x in range(M):
      # if a cell has the same color with its upper cell, assign the upper cell's country index to this cell
      if y - 1 >= 0 and dp[y][x] == dp[y - 1][x]:
        up_index = indices[(x, y - 1)]
        indices[(x, y)] = up_index
        countries[up_index] += 1

        # if it has also the same color with the cell to its left, make the country index assigned to the left cell point to the same country that the upper cell's index points to
        if x - 1 >= 0 and dp[y][x] == dp[y][x - 1]:
          left_index = indices[(x - 1, y)]

          if left_index != up_index:
            index_map[left_index] = up_index

      # if a cell has same color with its cell to its left but not the upper cell, assign the left cell's country index to this cell
      elif x - 1 >= 0 and dp[y][x] == dp[y][x - 1]:
        index = indices[(x - 1, y)]
        indices[(x, y)] = index
        countries[index] += 1

      # otherwise, assign a new country index (assign i and then i += 1) to this cell 
      else:
        indices[(x, y)] = i
        countries[i] += 1
        i += 1
        index_map[i] = i

  # the index map would have a series of keys(country indices) pointing to the values (countries); the distinct value count for country ids (if at least one cell has that country id; because the last time we execute i += 1, the new i may not be assigned to any cell) is the number of countries 
  return len(set([index_map[key] for key in index_map if countries[index_map[key]] > 0]))


print(
  countCountries(
    [[5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]]
  )
)

