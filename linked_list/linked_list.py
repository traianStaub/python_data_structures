from node import Node

class LinkedList():

    def __init__(self):
        self.head_node = None
        self.current_node = None
        self.size = 0

    def append_node(self, new_node):
        if self.head_node == None:
            self.head_node = new_node
            self.current_node = self.head_node
            self.size = 1
        else:
            self.current_node.next_node = new_node
            self.current_node = self.current_node.next_node
            self.size += 1
    
    def append(self, value):
        self.append_node(Node(value))

    def __str__(self):
        temp_node = self.head_node
        solution = ''

        while temp_node != None:
            solution += str(temp_node.value) + " "
            temp_node = temp_node.next_node
        
        return solution

    def get_size(self):
        return self.size

    def _remove_node(self, node_to_remove):
        return "working on"

    def delete_index(self, index):
        """deletes the node on the index"""

        if index >= self.size:
            print("index out of bounds")
            return False
        elif index < 0:
            print('index can\'t be negative')
            return False
        elif index == 0:
            del_node = self.head_node
            self.head_node = self.head_node.next_node
            del_node.next_node = None
            return del_node.value

        prev_node = self.head_node
        temp_node = prev_node.next_node

        i = 1
        while i < index:
            prev_node = temp_node
            temp_node = temp_node.next_node
            i += 1
        
        prev_node.next_node = temp_node.next_node
        temp_node.next_node = None
        return temp_node.value
        

        
        



