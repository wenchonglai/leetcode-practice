var maxSatisfaction = function(satisfaction) {
  let sum = satisfaction.sort((a, b) => a - b)
    .reduce((sum, el) => sum + el);
  let i = 0

  while (sum < 0)
    sum -= satisfaction[i++];

  return satisfaction.slice(i)
    .reduce((sum, el, i) => sum + el * (i + 1), 0);
};