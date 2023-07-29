# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getNumbers(l1)
        num2 = self.getNumbers(l2)

        res = num1 + num2

        node = ListNode()
        node.val = 0
        node.next = None

        start = node
        while res != 0:
            num = res % 10
            res //= 10

            node.val = num
            if (res == 0):
                node.mext = None
            else:   
                node.next = ListNode()
                node = node.next

        return start

    def getNumbers(self, l: ListNode):
        res = 0
        nextNode = l
        counter = 0
        while nextNode is not None:
            num = nextNode.val
            res += (num * (10 ** counter))
            counter += 1
            nextNode = nextNode.next
        return res