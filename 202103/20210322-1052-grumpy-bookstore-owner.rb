# @param {Integer[]} customers
# @param {Integer[]} grumpy
# @param {Integer} x
# @return {Integer}
def max_satisfied(customers, grumpy, x)
  normal_num = 0
  appeased_max = 0
  sum = 0
  
  customers.map.with_index do |el, i|
    sum -= customers[i - x] if i >= x && grumpy[i - x] == 1

    if grumpy[i] == 1
      sum += el
      appeased_max = sum if sum > appeased_max
    else
      normal_num += el
    end
  end

  normal_num + appeased_max
end