class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
      visited = set()
      graph = defaultdict(list)
      res = 0

      for [a, b] in allowedSwaps:
        graph[a].append(b)
        graph[b].append(a)

      for i in range(len(source)):
        if i not in graph:
          graph[i] = [i]

      for node in graph:
        stack = [node]
        indices = []

        while stack:
          n = stack.pop()
          if n in visited:
            continue

          visited.add(n)
          indices.append(n)

          for nxt in graph[n]:
            if nxt not in visited:
              stack.append(nxt)

        h = defaultdict(int)
        ct = len(indices)

        for i in indices:
          h[source[i]] += 1

        for i in indices:
          t = target[i]

          if h[t] > 0:
            h[t] -= 1
            ct -= 1

        res += ct

      return res