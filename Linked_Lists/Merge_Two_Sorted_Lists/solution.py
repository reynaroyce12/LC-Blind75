class ListNode(object):
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy_node = ListNode()
        current = dummy_node


        while list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy_node.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()
result_object = solution.mergeTwoLists(list1, list2)
result_head = []

while result_object:
    result_head.append(result_object.value)
    result_object = result_object.next

print(result_head)