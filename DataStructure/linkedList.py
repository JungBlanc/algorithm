class Node(object):
    def __init__(self):
        self.data = data
        self.next = None

# size(self) : 연결 리스트의 크기(항목 수)
# is_empty(self) : 연결 리스트의 항목이 없는지(empty)의 여부
# search(self, target) : 탐색, 순차탐색을 하므로 수행시간은 O(N)
# insert_front(self, item) : 새 노드를 처음에 삽입, O(1)

class SinglyLinkedList(object) :
    def __init__(self):
        self.head = None
        self.count = 0
    def append(self, node):
        if self.head== None :
            self.head = node
        else :
            cur = self.head
            while cur.next != None :
                cur = cur.next
            cur.next = node    