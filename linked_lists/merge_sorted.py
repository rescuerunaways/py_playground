class _Node:
    # why this implementation? - what are slots  - read in book about data structures in python;
    slots = '_element', '_next'

    # is __init__ function something special? :)
    def __init__(self, element, next):
        self._element = element
        self._next = next

    def push(self, e):
        self._next = self._next(e, self._next)


# this is how to iterate Linked List:

# cur_node = node0
# while cur_node is not None:
#     print(cur_node.get_data())
#     cur_node = cur_node.get_next()
# return None


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


def merge_sorted(node0, node1):
    dummy_head = Node(0, None)
    curr_0 = node0
    curr_1 = node1
    curr_d = dummy_head

    while curr_0 is not None and curr_1 is not None:
        if curr_0.data < curr_1.data:
            curr_d.set_next(curr_0)
            curr_0 = curr_0.next_node
        else:
            curr_d.set_next(curr_1)
            curr_1 = curr_1.next_node

        curr_d = curr_d.next_node

    # You can use a ternary expression in Python, but only for expressions, not for statements:

    curr_d.next_node = curr_0 if curr_0 is not None else curr_1

    return dummy_head.next_node


n0 = Node(1, Node(3, Node(4, Node(5, Node(6, Node(7, None))))))
n1 = Node(0, Node(2, Node(4, Node(8, Node(9, None)))))

print(merge_sorted(n0, n1))
