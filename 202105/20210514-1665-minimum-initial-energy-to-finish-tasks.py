class Solution:
  def minimumEffort(self, tasks: List[List[int]]) -> int:
    N = len(tasks)
    tasks.sort(key=lambda task: task[1] - task[0])

    for i in range(1, N):
      delta = tasks[i - 1][1] - tasks[i][1] + tasks[i][0]
      if delta > 0:
        tasks[i][1] += delta

    return tasks[-1][1]
