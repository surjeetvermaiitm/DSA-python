from re import X


class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return f"node {self.val} --> {self.next}"
    
a=Node(1,Node(2,Node(3,Node(4))))
#print(a)
def print_ll(head):
    while head:
        print(head.val)
        head=head.next
#print_ll(a)
def count_ll(head):
    c=0
    while head:
        c+=1
        head=head.next
    return c
#print(count_ll(a))
def insert_at_last(head,data):
    if head==None:
        return Node(data)
    ptr=head
    while ptr.next:
        ptr=ptr.next
    ptr.next=Node(data)
    return head
a=insert_at_last(a,5)
#print(a) 
def insert_at_front(head,data):
    return Node(data,head)
    if head==None:
        return Node(data)
    ptr=head
    x=Node(data)
    x.next=ptr
    head=x
    return head
a=insert_at_front(a,0)
print(a) 
 
    