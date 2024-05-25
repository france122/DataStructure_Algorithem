class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkList:
    def __init__(self,lst):
        self.head=Node(lst[0])
        p=self.head
        for i in lst[1:]:
            node=Node(i)
            p.next=node
            p=node
    def reverse(self):
        p=self.head.next
        self.head.next=None
        while p is not None:
            q=p
            p=p.next
            q.next=self.head
            self.head=q
lst = [1, 2, 3, 4, 5]
linked_list = LinkList(lst)

# Print the original list
print("Original List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Reverse the list
linked_list.reverse()

# Print the reversed list
print("Reversed List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
'''
`LinkList` 类中的 `reverse` 函数负责反转链表中元素的顺序。让我们逐步解释这个函数背后的主要思想：

1. **初始化**：
   - `p = self.head.next`：将指针 `p` 初始化为列表中的第二个节点（头节点之后的第一个节点）。
   - `self.head.next = None`：将头节点的 `next` 指针设置为 `None`，因为它将成为反转后链表的最后一个节点。

2. **反转指针**：
   - 进入一个 `while` 循环，直到 `p` 变为 `None`，表示我们已经遍历了整个原始链表。
   - 在循环内部：
     - `q = p`：将当前节点 `p` 赋值给 `q`。
     - `p = p.next`：将 `p` 移动到原始链表中的下一个节点。
     - `q.next = self.head`：将当前节点 `q` 的 `next` 指针设置为反转后链表的当前头节点，从而实现指针方向的反转。
     - `self.head = q`：更新反转后链表的头节点为当前节点 `q`。

3. **完成**：
   - 循环完成后，原始链表的所有节点都已经反转，`self.head` 现在指向原始链表的原尾节点（现在是反转后链表的头节点）。

这里的关键思想是通过迭代地反转每个节点的 `next` 指针，使其指向相反的方向。通过这样做，我们有效地反转了链表中元素的顺序。
'''


