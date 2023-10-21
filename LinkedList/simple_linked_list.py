class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

dummy = ListNode()
l1 = ListNode(1)
l2 = ListNode(2)
dummy.next = l1
l1.next = l2

while dummy:
    print(dummy.val, end="->")
    dummy = dummy.next
print("None")