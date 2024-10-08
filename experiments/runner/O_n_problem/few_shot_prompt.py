#################################

# given three <question, answer> given in the report
# based on the examples, please give me answer solution for the question
#################################

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the edge case
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

        # Return the head of the modified list
        return dummy.next

   # Helper function to convert a list to a linked list
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

    for i in range(25_000_000):

        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        head = list_to_linked_list(input_list)

        swapped_head = Solution().swapPairs(head)

        result_list = linked_list_to_list(swapped_head)
