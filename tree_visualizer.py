import graphviz
# build syntax tree from postfix expression
postfix = "ab*.a.b*."


class Node:
    def __init__(self, data):
        self.id = id(self)
        self.data = data
        self.left = None
        self.right = None


def build_tree(postfix):
    stack = []
    for c in postfix:
        if c.isalnum():
            stack.append(Node(c))
        elif c == '*' or c == '?' or c == '+':
            node = Node(c)
            node.left = stack.pop()
            stack.append(node)
        else:
            node = Node(c)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()


def draw_tree(root):
    dot = graphviz.Digraph()

    def traverse(node):
        if node:
            dot.node(str(id(node)), node.data)
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return dot


def show_tree(postfix):
    tree = build_tree(postfix)
    dot = draw_tree(tree)
    dot.format = 'png'
    dot.render('postfix', view=True)

# tree = build_tree(postfix)
# dot = draw_tree(tree)
# dot.format = 'png'
# dot.render('postfix', view=True)
