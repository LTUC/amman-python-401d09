import pysnooper

class EmptyStackException(Exception):
  pass

class Node:
    """
    To save data and a reference to the other nodes in the data structure
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    A stack is a data structure that consists of Nodes. Each Node
    references the next Node in the stack, but does not reference its
    previous.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        input: Value
        output: None
        It will create a node and assign it to the top.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        input: None
        output: Value of the node that poped
        It will remove the top from the stack and return the value of that      node, and       assgin new top
        """
        if not self.top:
            raise EmptyStackException("Pop from empty stack is not allowed")

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        """
        input stack
        output True if its empty otherwise return False
        """
        # if self.top is None :
        #   return True
        # else:
        #   return False
        return True if self.top is None else False

@pysnooper.snoop()
def multi_brackets_validation(input):
    stack = Stack()

    for char in input:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        elif char == "]":
            if stack.pop() != '[':
                return False

        elif char == '}':
            if stack.pop() != '{':
                return False

        elif char == ')':
            if stack.pop() != '(':
                return False
    return True
    #     elif char == ')' or char == '}' or char == ']':
    #         if stack.is_empty():
    #             return False
    #         elif stack.top.value + char in shipes:
    #             stack.pop()
    #         else:
    #             return False
    #
    # return True if stack.is_empty() else False


print(multi_brackets_validation('{}()[]'))

