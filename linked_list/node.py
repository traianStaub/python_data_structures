class Node():
    """a node class for linked lists"""


    def __init__(self, value, next_node = None):
        """a classic constructor for the node"""
        if (next_node != None) and (not isinstance(next_node, self)):
            raise TypeError(str(type(next_node)) + ' object is not ' + str(type(self)) + ' object')

        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        """returns the value of the value"""
        return self.value

    def set_node(self, new_node):
        """ changes the next_node"""
        self.next_node = new_node

