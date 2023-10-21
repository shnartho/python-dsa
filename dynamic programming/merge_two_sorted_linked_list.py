class ListNode: 
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

def merge_two_sorted_linked_list(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(2, ListNode(3, ListNode(6)))

merged = merge_two_sorted_linked_list(l1, l2)
while merged:
    print(merged.val, end='->')
    merged = merged.next
print("None")
