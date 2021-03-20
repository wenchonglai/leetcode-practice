from heapq import heappush, heappop, heapify # 数据结构：最小堆

class Solution:
  def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # 这个 while loop 在主程序 for loop 之内和之外各用到一次，所以写成 helper method
    def helper(heights, ends, skyline, start):
      # 检测新矩形左边界左方是否存在未处理的右边界（边界条件1 - ends 堆为空）
      while ends and ends[0] < start:         
        # 若 heights 堆中最高矩形的右边界小于等于 ends 堆中最小右边界（边界条件2 - heights 堆为空）
        # 本题的矩形为左闭右开区间，因此右边界的高度于其所属矩形的高度无关
        # 则该矩形高度已经不影响此后所有右边界的高度，因此可以弹出
        while heights and heights[0][1] <= ends[0]:
          heappop(heights)

        # 弹出最小右边界
        end1 = heappop(ends)
        height1 = -heights[0][0] if heights else 0

        # 最小右边界高度不可能大于 skyline 末元素高度
        # 若最小右边界高度小于 skyline 末元素高度，将最小右边界和新高度压入 skyline
        if not skyline or height1 < skyline[-1][1]:
          skyline.append([end1, height1])

    # heights 储存矩形高度，ends 储存矩形右边界位置
    heights = []
    ends = []
    skyline = []
    heapify(ends)
    heapify(heights)

    # start - 矩形左边界；end - 右边界；height - 矩形高度 
    for [start, end, height] in buildings:
      # 处理剩余的右边界
      helper(heights, ends, skyline, start)

      # 将新矩形的高度和右边界压入相应堆中
      # heights 除了储存高度，也要储存右边界。
      # 这样在弹出 ends 最小值时，可以检测高度最大的矩形的右边界是否在 ends 的左方
      heappush(heights, [-height, end]) # heights 为最大堆，所以要储存负值
      heappush(ends, end)

      # 处理左边界
      # 如果当前高度大于 skyline 末元素的高度（边界情况 1 - skyline 为空）
      if not skyline or height > skyline[-1][1]:
        # 边界情况2 - 如果当前左边界等于 skyline 末元素的左边界，则更新末元素高度
        if skyline and skyline[-1][0] == start:
          skyline[-1][1] = max(skyline[-1][1], height)
        # 正常情况：将左边界位置和高度压入 skyline
        else:
          skyline.append([start, height])

    # 检测剩余的右边界
    helper(heights, ends, skyline, 2 ** 31)

    return skyline
