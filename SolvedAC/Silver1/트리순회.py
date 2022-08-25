import sys

preorder_result = []
inorder_result = []
postorder_result = []


def preorder(node):
    if node == '.':
        return

    preorder_result.append(node)
    preorder(trees[node][0])
    preorder(trees[node][1])


def inorder(node):
    if node == '.':
        return

    inorder(trees[node][0])
    inorder_result.append(node)
    inorder(trees[node][1])


def postorder(node):
    if node == '.':
        return

    postorder(trees[node][0])
    postorder(trees[node][1])
    postorder_result.append(node)


N = int(sys.stdin.readline())
trees = dict()
for _ in range(N):
    n, l, r = sys.stdin.readline().strip().split()
    trees[n] = [l, r]

preorder('A')
inorder('A')
postorder('A')

print(*preorder_result, sep='')
print(*inorder_result, sep='')
print(*postorder_result, sep='')