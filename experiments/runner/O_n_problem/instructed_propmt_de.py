class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the swapping process
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first_node = prev.next
            second_node = prev.next.next
            
            # Swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Reinitializing the prev for next swap
            prev = first_node
        
        return dummy.next
