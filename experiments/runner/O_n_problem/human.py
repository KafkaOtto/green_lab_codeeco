#################################

# Problems: Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# average time complexity: O(n)
# space complexity O(1)

# links to solution: https://leetcode.com/problems/swap-nodes-in-pairs/solutions/5323100/python-and-java-solution-o-n-space-o-1-time-easy-and-straightforward

#################################

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head.next)
        node = head
        pre = None
        while node and node.next:
            nx = node.next
            node.next, nx.next = nx.next, node
            if pre:
                pre.next = nx

            pre = node
            node = node.next
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

    # import time
    # start = time.process_time()

    with open('./experiments/runner/O_n_problem/arr1.txt', 'r') as f:
        input_list = [int(x) for x in f.read().split()]

    # print('Time1: ', time.process_time() - start)

    for i in range(12_000):
        head = list_to_linked_list(input_list)
        swapped_head = Solution().swapPairs(head)
        result_list = linked_list_to_list(swapped_head)

    # print('Time2: ', time.process_time() - start)
