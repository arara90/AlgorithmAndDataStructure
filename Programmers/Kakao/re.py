# https://comdoc.tistory.com/entry/4-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8-Doubly-linked-list-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=800088
class Node:
    def __init__(self, element, weak):
        self.element = element
        self.weak = weak;
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node('0',False)

    def find(self, item):
        cur_node = self.head
        while cur_node.element != item: cur_node = cur_node.next
        return cur_node

    def insert(self, new, item, weak):
        new_node = Node(new, weak)
        cur_node = self.find(item)
        new_node.next = cur_node.next
        cur_node.next = new_node
        new_node.previous = cur_node

    def show(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.element,cur_node.weak, end=' -> ')
            cur_node = cur_node.next
            print(cur_node.element, cur_node.weak )

    def remove(self, item):
        cur_node = self.find(item)
        cur_node.previous.next = cur_node.next
        cur_node.previous = None
        if cur_node.next is not None:
            cur_node.next.previous = cur_node.previous
            cur_node.next = None

    def find_last(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            return cur_node

    def show_reverse(self):
        cur_node = self.find_last()
        while cur_node.previous is not None:
            print(cur_node.element, end=' <- ')
            cur_node = cur_node.previous
        print(cur_node.element)


###################################

def solution(n, weak, dist):
    answer = 0
    weak_point = weak.pop(0)
    boo = DoublyLinkedList()
    boo.show()

    print('ddddd')

    for i in range(0, n-1):
        isWeak = True
        print(i, weak_point)

        if i == weak_point :
            isWeak = True
            if len(weak) > 0:
                weak_point = weak.pop(0)
        boo.insert(f'{i+1}', f'{i}', isWeak)

    # boo.insert('2', '1', False)
    # boo.insert('3', '2', False)
    # boo.insert('4', '3', False)
    # boo.show()
    # boo.remove('3')
    # boo.show()
    # print(boo.find_last().element)
    # boo.show_reverse()

    boo.show()
    return answer

solution(12,[1, 5, 6, 10],[1, 2, 3, 4])

# n은 1 이상 200 이하인 자연수입니다.  - 둘레
# weak의 길이는 1 이상 15 이하입니다. = 취약점
# 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
# 취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
# dist의 길이는 1 이상 8 이하입니다.  - 한번에 이동할 수 있는 거리  (최대 8명?)
# dist의 원소는 1 이상 100 이하인 자연수입니다.
# 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.