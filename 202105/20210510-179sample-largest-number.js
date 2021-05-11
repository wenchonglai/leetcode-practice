/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
  // 思路：两两比较 nums 中的元素并排序
  //   如果 b 在 a 前面比 a 在 b 前面时构成的数字更大，则 b 在前
  //     实现：比较 str(b) + str(a) 和 str(a) + str(b) 的大小
  return nums
    .sort((a, b) => Number('' + b + a) - Number('' + a + b) )
    .join('')
    .replace(/^0*/, '') || '0'
};