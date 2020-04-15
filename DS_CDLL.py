class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.tail.next = self.head
        self.head.next = self.tail

    def print_List(self):
        start = self.head
        if start is None:
            print("EMPTY LIST")
        else:
            print(start.value)
            start = start.next
            while start != self.head:
                print(start.value)
                start = start.next

    def insert_at_end(self, value):
        new_node = Node(value)
        start = self.head
        if start.value is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            print("ELEMENT ADDED")
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            print("ELEMENT ADDED")
            return

    def insert_at_start(self, value):
        start = self.head
        new_node = Node(value)
        if start.value is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = self.head
            print("ELEMENT ADDED")
            return
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = start
            start.prev = new_node
            self.head = new_node
            print("ELEMENT ADDED")
            return

    def insert_at_pos(self, ELEMENT, value):
        new_node = Node(value)
        start = self.head
        if start.value is None:
            print("EMPTY LIST!")
            return
        else:
            while start.next != self.head:
                if start.value == ELEMENT:
                    NEXT = start.next
                    new_node.prev = start
                    new_node.next = NEXT
                    start.next = new_node
                    NEXT.prev = new_node
                    print("ELEMENT ADDED")
                    return
                else:
                    start = start.next
            self.insert_at_end(value)
            return

    def search_node(self, value):
        start = self.head
        count = 1
        if start.value == value:
            print("THE ELEMENT IS AT POSITION {}".format(count))
            return
        else:
            start = start.next
            while start != self.head:
                count = count + 1
                if start.value == value:
                    print("THE ELEMENT IS AT POSITION {}".format(count))
                    return
                else:
                    start = start.next
                    if start == self.head:
                        print("THERE IS NO ELEMENT PRESENT IN THE LIST")

    def delete_node(self, value):
        start = self.head
        if start.value == value:
            self.head = start.next
            self.head.prev = start.prev
            self.tail.next = self.head
            print("ELEMENT DELETED")
            return
        elif self.tail.value == value:
            PREVIOUS = self.tail.prev
            PREVIOUS.next = self.head
            self.head.prev = PREVIOUS
            print("ELEMENT DELETED")
            return
        else:
            start = start.next
            PREVIOUS = self.head
            while start is not self.tail:
                if start.value == value:
                    NEXT = start.next
                    PREVIOUS.next = NEXT
                    NEXT.prev = PREVIOUS.next
                    print("ELEMENT DELETED")
                    return
                PREVIOUS = start
                start = start.next

    def delete_CDLL(self):
        self.head = None
        self.tail = None
        print("LIST DELETED!")

    def create_list(self):
        n = int(input("Please enter the number of the elements:\n"))
        for i in range(n):
            NUMBER = int(input("Please enter the element:\n"))
            self.insert_at_end(NUMBER)
        return

    def print_reverse(self):
        start = self.head
        while start != self.tail:
            start = start.next
        print(start.value)
        while start is not self.head:
            start = start.prev
            print(start.value)
        return


List = CircularDLL()

while True:
    print("CREATING A CIRCULAR DOUBLY LINKED LIST")
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
        List.print_List()
    elif option == 3:
        List.print_reverse()
    elif option == 4:
        number = int(input("Please enter the value:"))
        List.insert_at_start(number)
    elif option == 5:
        number = int(input("Please enter the value:"))
        List.insert_at_end(number)
    elif option == 6:
        number = int(input("Please enter the value to insert:"))
        position = int(input("Please enter the value in the node:"))
        List.insert_at_pos(position, number)
    elif option == 7:
        number = int(input("Please enter the value:"))
        List.delete_node(number)
    elif option == 8:
        number = int(input("Please enter the value:"))
        List.search_node(number)
    elif option == 9:
        List.delete_CDLL()
    elif option == 10:
        break
