class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def print_List(self):
        start = self.head
        if start is None:
            print("EMPTY LIST!")
            return
        else:
            print(start.value)
            while start.next != self.head:
                start = start.next
                print(start.value)
            return

    def add_element_start(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.next = self.head
        self.head = new_node
        print("ELEMENT ADDED")
        return

    def add_element_end(self, value):
        new_node = Node(value)
        if self.head.value is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            print("ELEMENT ADDED")
            return
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            print("ELEMENT ADDED")
            return

    def add_element_after(self, element, value):
        new_node = Node(value)
        start = self.head
        if start.value == element:
            temp = start.next
            start.next = new_node
            start.next.next = temp
            print("ELEMENT ADDED")
            return
        while start != self.tail:
            if start.value == element:
                temp = start.next
                start.next = new_node
                start.next.next = temp
                print("ELEMENT ADDED")
                return
            else:
                start = start.next
                if start == self.tail:
                    temp = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head
                    print("ELEMENT ADDED")
                    return

    def search_node(self, value):
        count = 1
        start = self.head
        while start != self.tail:
            if start.value == value:
                print("THE ELEMENT IS AT {}".format(count))
                return
            else:
                start = start.next
                count = count + 1
                if start.value == self.tail.value:
                    print("THE ELEMENT IS AT {}".format(count))

    def create_CLL(self):
        n = int(input("How many elements to insert:\n"))
        if n == 0:
            return
        for i in range(n):
            VALUE = int(input("Please Enter the number:\n"))
            self.add_element_end(VALUE)

    def delete_node(self, value):
        start = self.head
        if start.value == value:
            self.tail.next = start.next
            self.head = start.next
            return
        while start.next != self.head:
            prev = start
            if start.next.value == value:
                prev.next = start.next.next
                return
            start = start.next

    def delete_CSLL(self):
        self.head = None
        self.tail = None
        print("LIST DELETED!!")


List = CircularSLL()

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

    option = int(input("Please Enter the option Below:\n"))

    if option == 1:
        List.create_CLL()
    elif option == 2:
        List.print_List()
    elif option == 3:
        number = int(input("Please enter the value:"))
        List.add_element_start(number)
    elif option == 4:
        number = int(input("Please enter the value:"))
        List.add_element_end(number)
    elif option == 5:
        number = int(input("Please enter the value:"))
        position = int(input("Please enter the value in the node:"))
        List.add_element_after(position, number)
    elif option == 6:
        number = int(input("Please enter the value:"))
        List.delete_node(number)
    elif option == 7:
        number = int(input("Please enter the value:"))
        List.search_node(number)
    elif option == 8:
        List.delete_CSLL()
    elif option == 9:
        break

