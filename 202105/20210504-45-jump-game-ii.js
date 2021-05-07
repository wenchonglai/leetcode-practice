var jump = function(nums) {
  for (var ct = 0, j = 0, i = nums.length - 1; i > 0; ct++){
    for (j = 0; nums[j] + j < i; j++);
    i = j
  }
  
  return ct
};