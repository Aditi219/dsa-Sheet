class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, new_data):  # to insert at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverselinked(self, head, k):
        current = head
        prev = None
        next = None
        count = 0
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverselinked(next, k)
        return prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    l1 = LinkedList()
    n = int(input())
    for i in range(n):
        l1.push(int(input()))
    l1.printList()
    print("-----------------")
    print("enter the value of k:")
    k = int(input())
    print("-----------------")
    l1.head = l1.reverselinked(l1.head, k)
    l1.printList()
