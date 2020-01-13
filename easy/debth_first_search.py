'''
Traverse the graph in debth first search
Example of intpu is:
        A
     /     \
    B      C
   / \     / \
  D   E   F  G
     / \
    H   I

Example of output:
["A", "B", "D", "E", "H", "C", "F", "G"]
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    time O(v + e) | space O(v)
    where v - number vertices in graph (nodes)
          e - number of edges (lines that connect nodes)
    def debth_first_search(self, array=[]):
        array.append(self.name)
        for child in self.children:
            child.debth_first_search(array)
        return array

test1 = Node('A')
test1.add_child('B').add_child('C')
test1.children[0].add_child("D").add_child("E")
test1.children[0].children[1].add_child("H").add_child("I")
test1.children[1].add_child("F").add_child("G")

print(test1.debth_first_search())
