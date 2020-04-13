class Node:
    # THIS IS A CONSTRUCTOR
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def print_List(self):
        VALUE = self.head
        if VALUE is None:
            print("LIST IS EMPTY!")
        while VALUE is not None:
            print(VALUE.data)
            VALUE = VALUE.next

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            VALUE = self.head
            while VALUE.next is not None:
                VALUE = VALUE.next
            VALUE.next = new_node

    def insert_at_pos(self, after, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            VALUE = self.head
            while VALUE is not None:
                if VALUE.data == after:
                    temp = VALUE.next
                    VALUE.next = new_node
                    new_node.next = temp
                    return
                else:
                    VALUE = VALUE.next

    def remove_element(self, value):
        start = self.head
        if start is None:
            print("No data in the List")
            return
        elif start.data == value:
            self.head = start.next
            return
        else:
            while start is not None:
                print(start.data, value)
                if start.data == value:
                    prev = start
                    next_ref = start.next.next
                    prev.next = next_ref
                    print("ELEMENT REMOVED!")
                    return
                else:
                    start = start.next
                    if start is None:
                        print("No data in the List")
                        return

    def search_node(self, value):
        count = 1
        start = self.head
        if start is None:
            print("NO ELEMENT IN THE LIST")
        while start is not None:
            if start.data == value:
                print("The element is at position {}".format(count))
                return
            else:
                count = count + 1
                start = start.next

    def delete_entire_SLL(self):
        self.head = None
        print("LIST IS DELETED!")

    def create_list(self):
        n = int(input("Enter the number of nodes:"))
        if n == 0:
            return
        for i in range(n):
            element = int(input("Please enter the data for the node:"))
            self.insert_at_end(element)


List = SingleLinkedList()

while True:
    print("CREATING A SINGLE LINKED LIST")
    print("1: Create a list")
    print("2: Print List")
    print("3: Insert at start")
    print("4: Insert at end")
    print("5: Insert at a position")
    print("6: Remove Element")
    print("7: Search the node")
    print("8: Delete the entire List")
    print("9: EXIT")

    option = int(input("Please Enter the option Below:"))

    if option == 1:
        List.create_list()
    elif option == 2:
        List.print_List()
    elif option == 3:
        number = int(input("Please enter the value:"))
        List.insert_at_start(number)
    elif option == 4:
        number = int(input("Please enter the value:"))
        List.insert_at_end(number)
    elif option == 5:
        number = int(input("Please enter the value:"))
        position = int(input("Please enter the value in the node:"))
        List.insert_at_pos(position, number)
    elif option == 6:
        number = int(input("Please enter the value:"))
        List.remove_element(number)
    elif option == 7:
        number = int(input("Please enter the value:"))
        List.search_node(number)
    elif option == 8:
        List.delete_entire_SLL()
    elif option == 9:
        break
