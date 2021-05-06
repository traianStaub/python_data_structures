class Node():
    """a node class for linked lists"""


    def __init__(self, value, next_node = None, prev_node = None):
        """a classic constructor for the node"""
        #checks to see if the next_node and prev_node are of type node
        if not Node.__check_node(next_node):
            raise TypeError('next_node: ' + str(type(next_node)) + ' object is not ' + str(type(self)) + ' object')

        if not Node.__check_node(prev_node):
            raise TypeError('prev_node: ' + str(type(prev_node)) + ' object is not ' + str(type(self)) + ' object')

        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_value(self):
        """returns the value of the value"""
        return self.value

    def __check_node(new_node):
        """checks if the value is a node"""

        if (new_node != None) and (not isinstance(new_node, Node)):
            return False 
        else:
            return True



