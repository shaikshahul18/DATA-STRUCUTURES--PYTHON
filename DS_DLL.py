class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def print_List_start(self):
        start = self.head
        if start is None:
            print("EMPTY LIST")
            return
        else:
            while start is not None:
                print(start.value)
                start = start.next

    def insert_at_start(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.prev = None
            self.head.next = None
            print("ELEMENT ADDED {}".format(value))
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            print("ELEMENT ADDED {}".format(value))

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.prev = None
            self.head.next = None
            print("ELEMENT ADDED {}".format(value))
        else:
            start = self.head
            while start is not None:
                previous = start
                start = start.next
            start = new_node
            previous.next = new_node
            start.next = None
            start.prev = previous
            print("ELEMENT ADDED {}".format(value))
            return

    def insert_at_pos(self, position, value):
        new_node = Node(value)
        start = self.head
        while start is not None:
            if start.value == position and start.next is not None:
                previous = start.next.prev
                n_Reference = start.next
                new_node.next = n_Reference
                start.next.prev = new_node
                new_node.prev = previous
                start.next = new_node
                print("ELEMENT ADDED {}".format(value))
                return
            else:
                start = start.next
            if start is None:
                self.insert_at_end(value)

    def delete_node(self, value):
        start = self.head
        if start.value == value:
            self.head = start.next
            self.head.prev = None
            print("ELEMENT DELETED!")
            return
        while start.next is not None:
            if start.value == value:
                previous.next = start.next
                start.next.prev = previous
                print("ELEMENT DELETED!")
                return
            else:
                previous = start
                start = start.next
        previous.next = None
        print("ELEMENT DELETED!")
        return

    def delete_DLL(self):
        self.head = None
        print("LIST DELETED!")
        return

    def print_reverse_list(self):
        if self.head is None:
            print("LIST IS EMPTY!")
        start = self.head
        while start.next is not None:
            start = start.next
        print(start.value)
        while start.prev is not None:
            print(start.prev.value)
            start = start.prev

    def search_node(self,value):
        start = self.head
        count = 1
        while start is not None:
            if start.value == value:
                print("ELEMENT {} AT POSITION {}".format(value, count))
                return
            else:
                start = start.next
                count = count + 1

    def create_list(self):
        n = int(input("Please enter the number of nodes:\n"))
        for i in range(n):
            ELEMENT_VALUE = int(input("Please enter the element:"))
            self.insert_at_end(ELEMENT_VALUE)


List = DoublyLL()
while True:
    print("CREATING A DOUBLY LINKED LIST")
    print("1: Create a list")
    print("2: Print List")
    print("3: Print reverse list")
    print("4: Insert at start")
    print("5: Insert at end")
    print("6: Insert at a position")
    print("7: Remove Element")
    print("8: Search the node")
    print("9: Delete the entire List")
    print("10: EXIT")

    option = int(input("Please Enter the option Below:\n"))

    if option == 1:
        List.create_list()
    elif option == 2:
        List.print_List_start()
    elif option == 3:
        List.print_reverse_list()
    elif option == 4:
        number = int(input("Please enter the value:"))
        List.insert_at_start(number)
    elif option == 5:
        number = int(input("Please enter the value:"))
        List.insert_at_end(number)
    elif option == 6:
        number = int(input("Please enter the value:"))
        position = int(input("Please enter the value in the node:"))
        List.insert_at_pos(position, number)
    elif option == 7:
        number = int(input("Please enter the value:"))
        List.delete_node(number)
    elif option == 8:
        number = int(input("Please enter the value:"))
        List.search_node(number)
    elif option == 9:
        List.delete_DLL()
    elif option == 10:
        break

