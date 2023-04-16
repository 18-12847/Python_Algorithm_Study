#0번 인덱스는 편의를 위해 비워둔다.
#Left = Index * 2
#Right = Index * 2 + 1
#Parent = floor(Index / 2)
tree = [None, 9, 3, 8, 2, 5, None, 7, None, None, None, 4]
tree = [
    None, #0번
    9, #Root
    3, 8, #왼쪽, 오른쪽 노드
    2, 5, None, 7, #3의 왼, 오, 8의 왼, 오
    None, None, None, 4 #2의 왼, 오, 5의 왼, 오
]

#LinkedList
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self, node):
        self.root = node
    #디버그용
    def display(self):
        #Level Order
        queue = deque()
        queue.append(self.root)
        while queue:
            curr_node = queue.popleft()
            print(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
tree = Tree(Node(9))
tree.root.left = Node(3)
tree.root.right = Node(8)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.right.right = Node(7)
tree.root.left.right.right = Node(4)
print(tree.displaey()) #9 3 8 2 5 7 4