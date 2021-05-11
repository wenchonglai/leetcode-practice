/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
  return nums
    .sort((a, b) => Number('' + b + a) - Number('' + a + b) )
    .join('')
    .replace(/^0*/, '') || '0'
};