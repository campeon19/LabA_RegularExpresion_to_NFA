import tree_visualizer
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'


def shunting_yard(infix):
    precedence = {'|': 1, '.': 2, '?': 3, '*': 3, '+': 3}
    stack = []
    postfix = []
    for i, c in enumerate(infix):
        # if c.isalnum():
        #     postfix.append(c)
        #     if (i+1 < len(infix)) and (infix[i+1].isalnum() or infix[i+1] == "("):
        #         stack.append(".")
        # if c.isalnum():
        #     postfix.append(c)
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif c in precedence:
            while stack and stack[-1] != '(' and precedence[c] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(c)
        else:
            postfix.append(c)

    while stack:
        postfix.append(stack.pop())

    return postfix


def add_concatenation(exp):
    precedence = {'|': 1, '.': 2, '?': 3, '*': 3,
                  '+': 3}  # precedencia de los operadores
    output = []  # cola de salida
    stack = []  # pila de operadores

    for i, char in enumerate(exp):
        if char.isalnum() and i < len(exp) - 1 and exp[i + 1].isalnum() or \
                char == ')' and i < len(exp) - 1 and exp[i + 1].isalnum() or \
                char.isalnum() and i < len(exp) - 1 and exp[i + 1] == '(' or \
                char == ')' and i < len(exp) - 1 and exp[i + 1] == '(' or \
                char == '*' and i < len(exp) - 1 and exp[i + 1] == '(' or \
                char == '+' and i < len(exp) - 1 and exp[i + 1] == '(' or \
                char == '?' and i < len(exp) - 1 and exp[i + 1] == '(' or \
                char == '*' and i < len(exp) - 1 and exp[i + 1].isalnum() or \
                char == '+' and i < len(exp) - 1 and exp[i + 1].isalnum() or \
                char == '?' and i < len(exp) - 1 and exp[i + 1].isalnum():
            output.append(char)
            output.append('.')
        else:
            output.append(char)

    return ''.join(output)


def infix_to_postfix(infix):
    resultado = add_concatenation(infix)
    resultado = shunting_yard(resultado)
    resultado = ''.join(resultado)
    return resultado

# regular_expression = input("Enter a regular expression: ")
# resultado = add_concatenation(regular_expression)
# print(resultado)
# resultado = shunting_yard(resultado)
# resultado = ''.join(resultado)
# print(resultado)
# # visualize the tree
# tree = tree_visualizer.show_tree(resultado)
