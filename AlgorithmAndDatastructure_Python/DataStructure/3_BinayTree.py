
#### 시간복잡도 http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html 보면서 다시 한 번 보기

class Node(object): #노드의 형식 정의
    def __init__(self, data):
        self.data = data
        self.left = self.right = None;

class BinarySearchTree(object):
    def __init__(self):
        self.root = None;

 ########## 1. 데이터 삽입 ##########
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        # 들어갈 위치에 아무것도 없으면 새로운 노드를 생성해서 그자리에 추가한다.
        if node is None:
            node = Node(data)

        else:
            # 부모가 새로 들어온 애보다 크면
            if data <= node.data:
                # 부모의 왼쪽에 추가한다. 단, 원래 왼쪽아이랑 비교해서 적절한 위치를 찾아간다. (쭉쭉 내려감)
                node.left = self._insert_value(node.left, data)
            else :
                node.right = self._insert_value(node.right, data)
        return node

    ########## 2. 데이터 검색 ##########
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        # 일치하는 노드 찾으면 retrurn
        if root is None or root.data == key:
            return root is not None
        elif key < root.data :
            return self._find_value(root.left, key)
        else :
            return self._find_value(root.right, key)
        
    ########## 3. 데이터 삭제 ##########
    def delete(self,key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False

        if key == node.data:
            deleted=True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent,child = child, child.left
                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child

            elif node.left or node.right:
                node = node.left or node.right

            else: node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)

        else :
            node.right, deleted = self._delete_value(node.right, key)

        return node, deleted

    ########## 4. 데이터 순회 ##########
    # 깊이 우선 탐색 중 전위 순회 : 뿌->왼->오
    def DFTravel(self):
        def _DFTravel(root):
            if root is None:
                pass
            else:
                print(root.data, end = ' ')
                _DFTravel(root.left)
                _DFTravel(root.right)

        _DFTravel(self.root)

    # 깊이 우선 탐색 중 중위 순회 : 왼->뿌->오
    def LFTravel(self):
        def _LFTravel(root):
            if root is None :
                pass
            else :
                _LFTravel(root.left)
                print(root.data, end = ' ')
                _LFTravel(root.right)
        _LFTravel(self.root)


    # 깊이 우선 탐색 중 후외 순회 : 오->뿌-> 왼
    def LRTravel(self):
        def _LRTravel(root):
            if root is None:
                pass
            else:
                _LRTravel(root.right)
                print(root.data, end=' ')
                _LRTravel(root.left)

        _LRTravel(self.root)


    # 너비 우선 탐색 (queue를 이용한다! )
    def layerTravel(self):
        def _layerTravel(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data, end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)

        _layerTravel(self.root)



if __name__ == '__main__':
    print('hi')
    # data의 선언
    data = [20,6,8,12,78,32,65,32,7,9]
    tree = BinarySearchTree()

    # 트리구조의 완성
    for x in data:
        tree.insert(x)

    # 트리 안의 데이터 존재에 대한 확인 및 조작
    print(tree.find(9))
    print(tree.find(3))

    print(tree.delete(6))

    print('전위순회')
    tree.DFTravel()

    print('\n중위순회')
    tree.LFTravel()

    print('\n후위순회')
    tree.LRTravel()

    print('\n너비우선탐색')
    tree.layerTravel()



