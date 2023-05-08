array = [1, 1, 5, 124, 400, 599, 1004, 2876, 8712]
def binary_search(array, find_value):
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    while left < right:
        if array[mid] == find_value:
            return mid
        if array[mid] < find_value:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return -1
print(binary_search(array, 2876)) # 7
print(binary_search(array, 1)) # 1
print(binary_search(array, 500)) # -1


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value < value:
                if curr_node.right is None:
                    curr_node.right = new_node
                    break
                curr_node = curr_node.right
            else:
                if curr_node.left is None:
                    curr_node.left = new_node
                    break
                curr_node = curr_node.left
    def has(self, value):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value == value:
                return True
            if curr_node.value < value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False
tree = BinarySearchTree()
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(5)
tree.insert(6)
tree.insert(2)
print(tree.has(8)) #True
print(tree.has(1)) #False


import bisect
array = [1, 1, 5, 124, 400, 599, 1004, 2876, 8712]

#bisect_left(arr, x) 함수는 정렬된 상태를 유지하며
#x 값을 넣을 수 있는 가장 왼쪽 Index 반환
print(bisect.bisect_left(array, 2876)) # 7
print(bisect.bisect_left(array, 1)) # 0
print(bisect.bisect_left(array, 500)) # 5

#bisect_right(arr, x) 함수는 정렬ㄹ된 상태를 유지하며
#x 값을 넣을 수 있는 가장 오른쪽 Index를 반환
#bisect와 bisect_rigth는 동일하게 동작
print(bisect.bisect(array, 2876)) # 8
print(bisect.bisect(array, 1)) # 2
print(bisect.bisect(array, 500)) # 5

def search(array, value):
    index = bisect.bisect_left(array, value)
    return index if array[index] == value else -1

print(search(array, 2876)) #7
print(search(array, 1)) #0
print(search(array, 500)) #-1