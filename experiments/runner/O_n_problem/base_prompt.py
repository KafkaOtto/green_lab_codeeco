#################################

# Prompt: please give me the python solution for the following question: question

#################################
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next:
            return head

        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Store the nodes to be swapped
            first_node = head
            second_node = head.next

            # Swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Move to the next pair of nodes
            prev = first_node
            head = first_node.next

        return dummy.next


def list_to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a linked list back to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(1_000):

        head = list_to_linked_list(input_list)

        swapped_head = Solution().swapPairs(head)

        result_list = linked_list_to_list(swapped_head)
