from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    if lst.head:
        count = 1
        node = lst.head
        while node.next:# this will give one number less than what I need
            count += 1
            node = node.next
    else:
        count = 0
    return count


def llprint(lst):
    """print a finite linked list"""
    if lst.head:
        node = lst.head
        while node.next:
            print(node.val, end=" ")
            node = node.next
        print(node.val)
    else: 
        print("null")


if __name__ == "__main__":
    lst = LList()
    trial = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
    for i in trial:
        append(lst, Node(i))

    llprint(lst)
    print(length(lst))

    from genfinite import lst
    print(length(lst))