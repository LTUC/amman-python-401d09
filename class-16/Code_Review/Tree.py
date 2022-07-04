class TNode:
    pass

class Tree:
    pass

class BST(Tree):
    def add(self, value):
        pass
    # Iterative solution
    # Define a variable to save the root value
    # Create a while loop if the root is not None
        # If the root > the value
            # If not root.left
                # Insert the value
                # return
            # root equal root.left
        # else
            # If not root.right
                # Insert the value
                # return
            # root equal root.right

    # Recursion Solution
    # if not root
        # Set the new value to the root
        # Return
    # Define a function called _walk that will take a value as root
        # if value < root.value:
            # if there is left for the root:
                # call _walk with the left node
            # else
                # Set the new value to the left
        # else the value > root.value
            # if there is right for the root:
                # call _walk with the right node
            # else
                # Set the new value to the right
    # class _walk with the root of the tree

    def cotanins(self, value):
        pass
    # Iterative solution
    # Define a temp variable and assign the root for it
    # While loop there is temp
        # if the value == temp.value:
            # return True
        # else if the value is less than the temp:
            # temp equal to the temp.left
        # else
            # temp equal to the temp.right
    # return False

    # Recursion Solution
    # if there is no root
        # return False

    # Define the _walk function and pass a parameter as root
        # if the root equal to the value
            # return True
        # else
            # try
                # if the value < root
                    # return _walk(root.left)
                # else
                    # return _walk(root.right)
            # except:
                # return False
    # if _walk(root) == None
        # return False
    # else:
        # return _walk(root)

    # if the root equal to the value
        # return True
    # if the value < root
        # if there is left:
            # return _walk(root.left)
        # else:
            # return False
    # else
        # return _walk(root.right)
