var buildTree = function(preorder, inorder) {
  if (!preorder.length) return null;
  
  let p0 = preorder[0],
      tree = new TreeNode( p0 );
  
  if ( preorder.length === 1 ) return tree;
  
  let i = inorder.indexOf(p0);

  tree.left = buildTree( preorder.slice( 1, i + 1 ), inorder.slice( 0, i ) ),
  tree.right = buildTree( preorder.slice( i + 1 ), inorder.slice( i + 1 ) );

  return tree;
};