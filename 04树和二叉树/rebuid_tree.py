#!/user/bin/env python3
# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def buildtree(preorder,inorder):
    if preorder==[] or inorder==[]:
        return None
    root_val = preorder[0]
    root_index=inorder.index(root_val)
    root=TreeNode(root_val)

    left_preorder=preorder[1:root_index+1]
    left_inorder=inorder[:root_index]

    right_preorder=preorder[root_index+1:]
    right_inorder =inorder[root_index+1:]

    root.left=buildtree(left_preorder,left_inorder)
    root.right = buildtree(right_preorder, right_inorder)
    return root

def postorder(tree):
    left,right='',''
    if tree.left:
        left=postorder(tree.left)
    if tree.right:
        right=postorder(tree.right)
    return left+right+tree.val



while 1:
    try:
        a,b=map(str,input().split())
        preorder,inorder=list(a),list(b)
        tree=buildtree(preorder,inorder)
        print(postorder(tree))
    except:
        break


