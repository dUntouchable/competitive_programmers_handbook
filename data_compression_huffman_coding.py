#
# Data Compression with Huffman Coding
#
from collections import defaultdict

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
    def __str__(self):
        k,v = self.val[0], self.val[1]
        return k

def dataCompression(arr):
    data = {}
    for val in arr:
        if val not in data:
            data[val] = 1
        else:
            data[val] += 1
    #
    # Huffman Coding
    #

    node_list = []
    while(len(data) > 0):
        key_min = min(data.keys(), key=(lambda k: data[k]))
        new_node = Node(tuple([key_min, data[key_min]]))
        node_list.append(new_node)
        del data[key_min]

    tree_node = Node(0)
    tree_node.left  = node_list[0]
    tree_node.right = node_list[1]

    for i in range(2, len(node_list)):
        new_tree_node = Node(0)
        new_tree_node.left = node_list[i]
        new_tree_node.right = tree_node

        tree_node = new_tree_node

    node = tree_node
    bits = []
    while(node.right != None):
        print(node.left, ''.join(bits+['0']))
        node = node.right
        bits.append('1')

        if node.right == None:
            print(node, ''.join(bits))


arr = ['A', 'B', 'C', 'D', 'A', 'C', 'A', 'A', 'A']
dataCompression(arr)
