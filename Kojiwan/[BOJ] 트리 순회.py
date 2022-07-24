n = int(input())
tree_obj = {}
for _ in range(n):
  root, left, right = input().split()
  tree_obj[root] = (left, right)

def preorder(root):
  print(root, end="")
  if tree_obj[root][0] != '.':
    preorder(tree_obj[root][0])
  if tree_obj[root][1] != '.':
    preorder(tree_obj[root][1])
  return

def inorder(root):
  if tree_obj[root][0] != '.':
    inorder(tree_obj[root][0])
  print(root, end="")
  if tree_obj[root][1] != '.':
    inorder(tree_obj[root][1])
  return

def postorder(root):
  if tree_obj[root][0] != '.':
      postorder(tree_obj[root][0])
  if tree_obj[root][1] != '.':
    postorder(tree_obj[root][1])
  print(root, end="")
  return

preorder('A')
print()
inorder('A')
print()
postorder('A')