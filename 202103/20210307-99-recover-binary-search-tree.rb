# 深度搜索以 root 为根的子树
# root: 子树根节点
# nodes: 储存被打乱数据的数组，最大长度为 4
# last: 本轮搜索前，上一个访问的节点
# 返回最后访问的节点（最右节点）
def dfs(root, nodes = [], last = nil) 
  return last unless root #如果 root 为空，返回参数指定的上一个节点

  last = dfs(root.left, nodes, last)  #
  
  #若上一个访问的节点大于根节点，则把上一个访问的节点和根节点一同压入数组中
  #因为只有一对节点被打乱，所以这种情况最多只会出现两次。因此空间复杂度 O(1)
  nodes.push(last, root) if last && root.val < last.val 
     
  #访问根节点完成，最后一个访问的节点为根子树；将其作为上一个访问的节点，传入对右子树的深度搜索。
  dfs(root.right, nodes, root) || root #若右子树为空，返回根节点，否则返回右子树最大节点
end

def recover_tree(root)
  nodes = [] #初始化储存数组
  dfs(root, nodes) #深度搜索
  nodes[0].val, nodes[-1].val = nodes[-1].val, nodes[0].val #交换数组中第一个和最后一个节点的值
  
  root
end