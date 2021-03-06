from node import Node

class LinkedList():
    """LinkedList class that has the functionality of a list but stores the values as linked nodes"""

    def __init__(self):
        """Initializes the class with a empty head and of size 0"""
        self.head_node = None
        self.current_node = None
        self._size = 0

    def append_node(self, new_node):
        """Adds a node to the end of the list"""
        if self.head_node == None:
            self.head_node = new_node
            self.current_node = self.head_node
            self._size = 1
        else:
            self.current_node.next_node = new_node
            new_node.prev_node = self.current_node
            self.current_node = self.current_node.next_node
            self._size += 1
    
    def add_front_node(self, new_node):
        """Adds a node to the beginning of the list"""
        if self.head_node == None:
            self.head_node = new_node
            self.current_node = self.head_node
            self.size = 1
        else:
            new_node.next_node = self.head_node
            self.head_node.prev_node = new_node
            self.head_node = new_node
            self._size += 1

    def add_front(self, value):
        """creates a node with value and adds it to the front of the list"""
        self.add_front_node(Node(value))

    def append(self, value):
        """creates a node with value and appends it to the list"""
        self.append_node(Node(value))

    def get_size(self):
        """returns the size of the list"""
        return self._size

    def _remove_node(self, node_to_remove):
        """Removes a specific node"""
        return "working on"

    def search(self, value):
        """Searches the value in the list"""
        temp_node = self.head_node
        
        while temp_node != None:
            if temp_node.value == value:
                return True
            
            temp_node = temp_node.next_node
            
        return False
        
    def delete_index(self, index):
        """Deletes the node on the index"""

        if index >= self._size:
            print("index out of bounds")
            return False
        elif index < 0:
            print('index can\'t be negative')
            return False
        elif index == 0:
            return_value = self.head_node.value
            self.head_node = self.head_node.next_node
            self.head_node.prev_node.next_node = None
            self.head_node.prev_node = None
            return return_value
        else:
            temp_node = self.head_node.next_node

            i = 1
            while i < index:
                temp_node = temp_node.next_node
                i += 1

            return_value = temp_node.value
            temp_node.prev_node.next_node = temp_node.next_node
            temp_node.next_node.prev_node = temp_node.prev_node
            temp_node.next_node = None
            temp_node.prev_node = None

            return return_value

    #deque functionality
    def pop(self):
        temp_value = self.current_node.value

        self.current_node.prev_node.next_node = None
        self.current_node = self.current_node.prev_node

        return temp_value

    def peek(self):
        return self.current_node.value

    def __str__(self):
        """Returns all values of the list as a string"""
        temp_node = self.head_node
        solution = ''

        while temp_node != None:
            solution += str(temp_node.value) + " "
            temp_node = temp_node.next_node
        
        return solution

    def str_reverse(self):
        """Returns a string that is the values from the list in reverse"""
        temp_node = self.head_node
        while temp_node.next_node != None:
            temp_node = temp_node.next_node
        
        solution = ""
        while temp_node != None:
            
            solution += " " + str(temp_node.value)
            temp_node = temp_node.prev_node
        
        return solution
        
        
        

        
        



