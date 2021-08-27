var getSum = function(a, b) {
  if (b === 0){ return a; }
  
  [a, b] = [a ^ b, (a & b) << 1];
  
  return getSum(a, b);
};