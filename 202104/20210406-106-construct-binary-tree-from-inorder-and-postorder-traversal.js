var buildTree = function(inorder, postorder) {
  let len = postorder.length;
  
  if (!len) return null;
  
  let p = postorder[ postorder.length - 1 ],
      tree = new TreeNode(p),
      i = inorder.indexOf(p);
  
  if (len === 1) return tree;
  
  tree.left = buildTree( inorder.slice(0, i), postorder.slice(0, i) );
  tree.right = buildTree( inorder.slice(i + 1, len), postorder.slice(i, len - 1) )
  
  return tree;
};