# 02. add two numbers
# n = max(len(p), len(q)) 
# time: O(n), space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        p, q, carry_in, cur = l1, l2, 0, dummy_head

        while p or q or carry_in != 0:
            p_val = p.val if p else 0
            q_val = q.val if q else 0
            sum_res = p_val + q_val + carry_in
            carry_in, node_val = sum_res // 10, sum_res % 10

            node = ListNode(node_val)
            cur.next = node
            cur = cur.next

            if p: p = p.next
            if q: q = q.next

        return dummy_head.next