const eraseOverlapIntervals = function (intervals) {
// 整体思路：按照 interval.end 大小排序，看最多存在多少个分立的区间。最大区间数即为最大非重叠 intervals 的数量。返回 intervals 长度减去区间的个数。

  intervals.sort((a, b) => a.end - b.end); // 按 interval.end 大小排序
  
  let segments = 1                    // 最初 1 个区间
  let curr = intervals[0]             // 指针指向头元素
  let len = intervals.length;   

  for (let i = 1; i < len; i++){      // 比较第 i 个元素与指针元素
    let interval = intervals[i];

    // 如果第 i 个元素的 start 不小于当前元素的 end，则证明第 i 个元素可以存在于新的区间；此时需要将当前元素更新为第 i 个元素
    // 如果第 i 个元素的 start 小于当前元素的 end，则当前元素不可能是决定最大区间数的元素
      // 反证：若 intervals[i] 决定最大区间数，则：
      // 1. 若 intervals[i].start < curr.start，则 curr 的两端都比 intervals[i] 更为约束，由 curr 决定的区间数大于等于 intervals[i]
      // 2. 若 intervals[i].start > curr.start。此时最大区间数的上一个区间的 end 必然在 curr.start 和 intervals[i].start 之间
      //    因此必存在 j, intervals[j].end < curr.end，intervals[i] 在指针指向 intervals[j] 时就会被选取，进而指针不可能指向 curr
    if (interval.start >= curr.end){
      curr = interval;
      segments += 1;
    }
  }

  return len - segments
}
