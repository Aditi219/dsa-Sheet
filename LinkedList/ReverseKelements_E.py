class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverselinked(self, head, k):
        if (k == 1):
            return head

        start_node = head
        end_node = head
        previous_start_node = None

        while (1):
            remaining_nodes = k

            while (remaining_nodes > 0 and end_node != None):
                end_node = end_node.next
                remaining_nodes -= 1

            if (remaining_nodes == 0):
                middle_node = start_node.next
                reversed_group_head = start_node

                while (middle_node != end_node):
                    next_middle_node = middle_node.next
                    middle_node.next = reversed_group_head
                    reversed_group_head = middle_node
                    middle_node = next_middle_node

                if (previous_start_node != None):
                    previous_start_node.next = reversed_group_head
                else:
                    head = reversed_group_head

                previous_start_node = start_node
                start_node = end_node
            else:
                if (previous_start_node != None):
                    previous_start_node.next = start_node

                break

        return head

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
