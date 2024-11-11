class Node:
    def __init__(self, val):
        self.value = val
        self.left = -float('inf')
        self.right = float('inf')

def is_bst(filename):
    nodes = []
    with open(filename, 'r') as file:
        count = int(file.readline().strip())
        root_val = int(file.readline().strip())
        root = Node(root_val)
        nodes.append(root)
        for i in range(count-1):
            line = file.readline().strip().split()
            val, parent, direction = int(line[0]), int(line[1]), line[2]
            parent_node = nodes[parent - 1]
            node = Node(val)
            if direction == 'L':
                node.left = parent_node.left
                node.right = parent_node.value
            elif direction =='R':
                node.left = parent_node.value
                node.right = parent_node.right
            nodes.append(node)
            if node.value < node.left or node.value >= node.right:
                return "NO"
    return "YES"

result = is_bst('bst.in')
print(result)
with open('bst.out', 'w') as file:
    file.write(result)
