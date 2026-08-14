# Beginner-friendly binary tree example for a company hierarchy
# CEO has two managers, and each manager has two employees

class BinaryTree:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# Create nodes for the company hierarchy
ceo = BinaryTree("CEO")
manager1 = BinaryTree("Manager 1")
manager2 = BinaryTree("Manager 2")
emp1 = BinaryTree("Employee 1")
emp2 = BinaryTree("Employee 2")
emp3 = BinaryTree("Employee 3")
emp4 = BinaryTree("Employee 4")

# Connect the tree
ceo.left = manager1
ceo.right = manager2

manager1.left = emp1
manager1.right = emp2

manager2.left = emp3
manager2.right = emp4

# Print the tree in preorder (root -> left -> right)
def preorder(node):
    if node is not None:
        print(node.name)
        preorder(node.left)
        preorder(node.right)


print("Company Hierarchy:")
preorder(ceo)

        
