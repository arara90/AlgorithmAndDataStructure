class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init():
    global node1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4


def delete(del_data):
    global node1

    # 1. 지운 뒤 앞노드와 뒷노드를 연결하기 위해 앞노드의 정보 저장
    pre_node = node1
    next_node = pre_node.next

    # 2. delete
    # 2_1. 지울 노드가 시작 node라면
    if pre_node.data == del_data:
            # node1의 다음 노드가 node1이 되고
        node1 = next_node
            # 원래의 node1은 delete!
        del pre_node
        return

    # 2_2. next_node가 존재할때까지만 while
    while next_node:
        # 다음 노드가 삭제 대상 노드라면
        if next_node.data == del_data:
            # 현재 노드(pivot node) 다음 노드의 next로 저장 (즉, 현재 노드의 다음을 수정)
            pre_node.next = next_node.next
            # 삭제 대상 노드를 삭제하고 while문 종료
            del next_node
            break

        # pivot 이동
        pre_node = next_node
        next_node = next_node.next

# 추가하기 ( node1 앞 쪽에 추가 )
def insert(ins_data):
    global node1
    new_node = Node(9, node1)
    node1 = new_node

def print_list():
    global node1
    pv_node = node1

    while pv_node:
        print(pv_node.data)
        pv_node = pv_node.next

def LinkedList():
    init()
    delete(2)
    insert("9")
    print_list()

LinkedList()




