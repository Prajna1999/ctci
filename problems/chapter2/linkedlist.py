# create a linkedlist and create a few methods

class Node:
    def __init__(self, data):
        self.data=data
        # extra attributes can be put to None even if they are not kept as an argument  to 
        # the __init__ function
        self.nextp=None
    


class LinkedList:
    def __init__(self):
        self.head:Node=None

        
    def delete_node(self, d):

        if self.head is None:
            return 
        
        if self.head.data==d:
            self.head=self.head.nextp
            return
        
        # iterate loop to reach the previous node to the required node to be deleted
        current=self.head
        while current.nextp is not None:

            if current.nextp.data==d:
                current.nextp=current.nextp.nextp
                return 
            current=current.nextp



def main():
    ll = LinkedList()
    
    # Build list: 1 -> 2 -> 3 -> 4
    ll.head = Node(1)
    ll.head.nextp = Node(2)
    ll.head.nextp.nextp = Node(3)
    ll.head.nextp.nextp.nextp = Node(4)
    
    # Test 1: Delete middle node
    ll.delete_node(2)
    print("After deleting 2:")
    print_list(ll.head)  # Should print: 1 -> 3 -> 4
    
    # Test 2: Delete head
    ll.delete_node(1)
    print("After deleting 1:")
    print_list(ll.head)  # Should print: 3 -> 4
    
    # Test 3: Delete last node
    ll.delete_node(4)
    print("After deleting 4:")
    print_list(ll.head)  # Should print: 3

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.nextp
    print("None")

if __name__ == "__main__":
    main()

