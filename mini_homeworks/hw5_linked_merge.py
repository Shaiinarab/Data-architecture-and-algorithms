class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(head1, head2):
    if not head1:
        return head2
    current = head1
    while current.next:
        current = current.next
    current.next = head2
    return head1