import time
from typing import List

class Node:
    name = None
    right_child_name = None
    left_child_name = None

    def __str__(self):
        return f"{self.name}({self.right_child_name},{self.left_child_name})"

def get_nodes(lines: List[str]):
    nodes = {}
    # Make nodes
    for line in lines:
        n = Node()
        fields = line.split(" = ")
        n.name = fields[0]
        children = fields[1][1:-1].split(", ")
        n.left_child_name = children[0]
        n.right_child_name = children[1]
        nodes[n.name] = n
    
    # print(nodes)
    # # Link nodes
    # for node_name in nodes:
    #     print(f"{node_name} should link to {nodes[node_name].left_child_name} and {nodes[node_name].right_child_name}")
    #     nodes[node_name].choices['L'] = nodes[nodes[node_name].left_child_name]
    #     print(nodes[nodes[node_name].left_child_name])
    #     nodes[node_name].choices['R'] = nodes[nodes[node_name].right_child_name]
    #     print(nodes[nodes[node_name].right_child_name])
    #     print(f"Linked to {nodes[node_name].choices['L'].name} and {nodes[node_name].choices['R'].name}")
    #     print(nodes[node_name])
    #     print()

    return nodes

def traverse_nodes(choices: str, nodes: List[Node]) -> int:
    steps = 0
    current_node = nodes['AAA']
    print(choices)
    while True:
        for c in choices:
            # print("Am at:", current_node.name)
            if current_node.name == 'ZZZ':
                return steps
            # print(f"Can go to {current_node.left_child_name} or {current_node.right_child_name}")
            steps += 1
            # print(f"Choice {c}\n")
            if c == 'L':
                current_node = nodes[current_node.left_child_name]
            else:
                current_node = nodes[current_node.right_child_name]

        


if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    choices = lines[0]
    nodes = get_nodes(lines[2:])

    steps = traverse_nodes(choices, nodes)


    end_time = time.time()
    print(f"Steps needed: {steps}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")