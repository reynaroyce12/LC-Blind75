class ListNode(object):
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class Solution_1(object):
    def hasCycle(self, head):

        visited_nodes = set()

        current_node = head
        while current_node is not None:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next

        return False


class Solution_2(object):
    def hasCycle(self, head):

        fast_pointer = slow_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True

        return False


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

solution = Solution_2()
result = solution.hasCycle(head)
print(result)