#2.Create a BT to represent computer folder structure containing folders and files

# Binary Tree representation of a folder structure in Python

class BinaryTree:
    def __init__(self, name, item_type="folder"):
        self.name = name
        self.item_type = item_type
        self.left = None
        self.right = None

# Root folder: Computer
computer = BinaryTree("Computer")

# Main folders inside Computer
documents = BinaryTree("Documents")
downloads = BinaryTree("Downloads")
projects = BinaryTree("Projects")

# Connect root to main folders
computer.left = documents
computer.right = downloads

# Add a folder under Documents
report = BinaryTree("report.docx", "file")
notes = BinaryTree("notes.txt", "file")
documents.left = report
documents.right = notes

# Add files under Downloads
setup = BinaryTree("setup.exe", "file")
music = BinaryTree("music.mp3", "file")
downloads.left = setup
downloads.right = music

# Add nested folder under Projects
python_folder = BinaryTree("Python")
java_folder = BinaryTree("Java")
projects.left = python_folder
projects.right = java_folder

# Files inside Python folder
main_py = BinaryTree("main.py", "file")
readme = BinaryTree("README.md", "file")
python_folder.left = main_py
python_folder.right = readme

# File inside Java folder
app_java = BinaryTree("app.java", "file")
java_folder.left = app_java

# Preorder traversal: root -> left -> right

def preorder(node, level=0):
    if node is None:
        return

    spaces = "  " * level
    print(f"{spaces}{node.item_type.upper()}: {node.name}")
    preorder(node.left, level + 1)
    preorder(node.right, level + 1)


print("Computer Folder Structure (Binary Tree)")
preorder(computer)
