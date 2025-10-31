import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

tree = []

while True:
    try:
        tree.append(int(input()))
        
    except:
        break
    
def binary_search_tree(tree):
    left = []
    right = []
    
    if tree:
        parent = tree.pop(0)
        
        for node in tree:
            if node < parent:
                left.append(node)
            else:
                right.append(node)    
                            
        binary_search_tree(left)
        binary_search_tree(right)
        print(parent)
        
binary_search_tree(tree)