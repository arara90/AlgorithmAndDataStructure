## 4.9 데크(Deque) 자료구조

##### 1) 데크

* 리스트 양쪽 끝에서 삽입과 삭제가 모두 이루어지는 자료구조
* **스택과 큐를 혼합**한 구조 / 두개의 포인터가 양쪽 끝을 가리킨다.

##### 2) 종류

* 입력 제한 데크 (스크롤) : 삽입이 한쪽에서만 일어나는 데크
* 출력 제한 데크 (셀프) : 출력이 한쪽에서만 일어나는 데크

> ##### 3) operation <http://examradar.com/deque/>
>
> ![deque](http://examradar.com/wp-content/uploads/2016/10/Figure-4.5.-Representation-of-a-deque..png)
>
> ![operation](http://examradar.com/wp-content/uploads/2016/10/Figure-4.6.-Basic-operations-on-deque.png)
>
> 

## 4.10 트리(Tree) 자료구조

##### 1) 트리

- 임의의 노드에서 다른 노드로의 경로가 하나 밖에 없는 것.
- **비선형 계층** 구조 : 단 하나의 루트 노드에서 하위 노드들이 연결
- 배열 또는 연결 리스트를 사용하여 구조

##### 2) 이진 트리 구조 : 다음 데이터를 가리키는 것이 2개인 단방향 트리 구조

##### 3) B 트리 구조 :  다음 데이터를 가리키는 것이 2개 이상이 될 수 있다.

* DB and File System에 널리 사용

​			![B-Tree](https://1.bp.blogspot.com/-ToUDNp6fhmw/Wg0Uxll4bGI/AAAAAAAAJDc/4PVPnEkEUhAjpS-PQkjukNUF4F3fDSzpQCLcBGAs/s640/B%25ED%258A%25B8%25EB%25A6%25AC.PNG)

##### 4) 구조와 용어

![tree](https://cdn-images-1.medium.com/max/1200/1*TuJ3FO1cxXR12fNZAlWF0Q.jpeg)

##### 5) 용도

- OS 의 File System



## 4.11 이진 트리(Binary Tree)

##### 1) 이진 트리

- 트리 자료구조 중에서 모든 노드가 **최대 2개의 자식 노드를 가질 수 있는** 구조.
- **왼쪽** 서브 트리의 값 **< 루트**의 값 / **오른쪽** 서브트리의 값 **> 루트**의 값
- 주로 **빠른 검색이 필요한 곳**에서 사용 

##### 2) 모양에 따른 분류 : <https://www.tutorialride.com/data-structures/types-of-binary-tree.htm>

* 포화 이진 트리 ( Full / Strictly Binary Tree) : 레벨의 노드가 꽉 차있는 트리

* 완전 이진 트리 ( Complete / perfect Binary Tree ) : 마지막 레벨 전까지는 노드가 꽉 차 있고, 마지막 레벨의 왼쪽에서 오른쪽으로 노드가 채워져 있음( 마지막 레벨이 다 채워지지 않아도 됨)

* 편향 이진 트리 ( Skewed Binary Tree ) : 왼쪽 혹은 오른쪽 서브 트리만을 가지는 트리

  ![](https://2.bp.blogspot.com/-iD61KYN8-CM/Wgz89po2SNI/AAAAAAAAJDI/xRplbDnsPToTNyBSTd1Da16ZoFLkg2UBwCLcBGAs/s640/%25EC%259D%25B4%25EC%25A7%2584%25ED%258A%25B8%25EB%25A6%25AC_%25EB%25AA%25A8%25EC%259D%258C.PNG)

##### 3) 알고리즘

##### 4) 응용 사례 및 구현

1. 수식 트리(expression Tree) ; 컴파일러와 같은 프로그램 로직을 구성하면서 사용자가 입력한 정보를 관리하는 방식.  (   [ 그림 수식 예: 9 – 6 / 2 + 4 ]  )

   ![수식트리](https://t1.daumcdn.net/cfile/tistory/216EBA3B57124AFB04)

   ​													  

   * [수식트리의 구현 ]: <https://yahma.tistory.com/22>

   * 개념 : 전위/중위/후위 표기법과 같은 하나의 수식을 표현하는 방식

     

2. ##### 이진트리를 컴퓨터에서 구현하는 방식 <<https://yahma.tistory.com/19>>

   * **순차 자료구조 방식**

     * 노드에 번호가 부여됨
     *   트리가 완성 된 이후부터는 그 트리를 대상으로 매우 빈번한 탐색이 이뤄지기 때문에 연결 리스트보다 **탐색이 빠른 이점**이 있음

     ![순차 자료구조 방식의 이진트리](https://t1.daumcdn.net/cfile/tistory/23222442570DAB9B1C)

     

   * **연결 자료구조** 방식 

     * 형태가 트리 형태와 일치

     ![연결자료구조방식의 이진트리](https://t1.daumcdn.net/cfile/tistory/2221DE42570DAB9B1C)

    

   ##### 5) 깊이 우선 탐색 vs 너비 우선 탐색

   1. 깊이 우선 탐색

      * 전위 순회 : 뿌리 > 왼쪽 > 오른쪽 
      * 중위 순회 : 왼쪽 > 뿌리 > 오른쪽
      * 후위 순회 : 왼쪽 > 오른쪽 > 뿌리

      

   2. 너비 우선 탐색

      * 뿌리 노드부터 깊이 순으로 방문 

   

## 4.12 힙(Heap)

##### 1) 힙

1. 컴퓨터 분야에서 두가지 의미의 힙

* 컴퓨터에서 프로세스가 만들어졌을 때, **메모리를 할당하는 방법으로서의 힙**과 스택

* 이진 트리의 일종(**완전이진트리**)으로 **max, min값을 빠르게 찾을 수 있도록 구성된 자료구조** 

  * 데이터를 정렬하는 것이 아니라 가장 큰/작은 값 몇개만 필요할 때 

  * 최소 힙(min heap) : 부모노드의 값이 항상 하위 노드의 값보다 작은 경우

  * 최대 힙(max heap) : 부모 노드의 값이 항상 하위 노드의 값보다 큰 경우

     - 위에서 설명한 것과 다르게, 큰 값이 루트고 왼쪽값이 오른쪽 값보다 크다. (루트 > 왼 > 오)

       ![최대힙](https://t1.daumcdn.net/cfile/tistory/251587335718CFDF2D)

       ​															[max heap]

        

* 일반적으로 **배열을** **이용하여 구현**

  ![배열index](https://t1.daumcdn.net/cfile/tistory/253DA44E562E45C611)

##### 2) 힙 사용 예

1. 여러 프로세스의 우선순위를 결정하는 방법으로 사용하는 경우
   * 최대 힙으로 구성 : 우선 순위가 큰 프로세스가 최상위에 위치
   * 프로세스를 요청할 때는 최상위 노드(루트노드)에 있는 프로세스를 반환
   * 루트 노드가 반환되면 나머지 노드를 우선순위 숫자에 근거하여 트리 구조를 재구성



##### 3) 최대 힙에서의 삽입, 삭제 과정

1. 삽입(up heap) -> **가장 마지막 위치(트리 마지막 레벨의 가장 오른쪽)에 추가** 후 부모와 비교하겨 자리 옮긴 후 형제와 비교 하는 방식으로 적절한 위치를 찾아간다

2. 삭제(down heap) -> 루트 삭제 후, 가장 마지막 위치에 있던 애를 root에 올릴 후 비교하며 내려오는 방식

   https://www.swexpertacademy.com/main/main.do

   * **? 삽입 후 완전 정리 된 상태가 아닌데 이렇게 남겨두는 것인가..?**

     <https://books.google.co.kr/books?id=E7FMDwAAQBAJ&pg=PA315&lpg=PA315&dq=%ED%9E%99+%EC%B6%94%EA%B0%80+%ED%9B%84+%EC%A0%95%EB%A0%AC&source=bl&ots=vwWWLwlh50&sig=ACfU3U2qfiaFbKdt36yg_eQF92GZAlwK0w&hl=ko&sa=X&ved=2ahUKEwi_s6PmkpbjAhXEvLwKHVyoCrE4ChDoATAHegQICRAB#v=onepage&q=%ED%9E%99%20%EC%B6%94%EA%B0%80%20%ED%9B%84%20%EC%A0%95%EB%A0%AC&f=false>

     *: 단순히 부모-자식간의 크기 비교이며, 루트의 값이 중요하므로 루트 아래의 정렬상태가 크게 중요하지 않다.*

   



##### 4) 우선순위 큐에서의 힙 

![우선순위큐 구현](https://gmlwjd9405.github.io/images/data-structure-heap/data-structure-heap-priorityqueue.png)



## 4.13 그래프 자료구조(Graph)

##### 1) 그래프

1. 2개 이상의 항목이 어떤 관계를 맺고 있는지를 노드(정점)와 엣지(선)을 이용하여 표현하는 것
2. 방향이 있는/없는 그래프로 구분

##### 2) 사용

* 페이스북, 트위터 : 각 사용자가 다른 사용자와 어떤 관계를 맺는지 표현하는 경우

* PERT/CPM (Program Evaluation and Review Technique/Critical Path Method): 비용을 적게 사용하면서 최단 시간 안에 계획을 완성하기 위한 프로젝트 일정관리 기법

* **최단 경로** : 그래프에서 정점 a,b를 연결하는 경로 중에서 가중치의 합이 최소가 되는 경로를 찾는 방법 (ex. 다익스트라(Dijkstra)) - **Lumos!!!**( A* algorithm 사용)

  

##### 3) 그래프에서 알아 두어야 할 용어

1.  **깊이 우선 탐색(DFS) / 너비 우선탐색(BFS)** 

   * **깊이 우선 탐색** (DFS : Depth First Serch) : 시작 정점에서 한 방향으로 갈 수 있는 가장 먼 경로까지 탐색하다가 갈 곳이 없으면, 가장 마지막에 만났던 부모노드로 돌아와서  다른 방향을 탐색하는 방법 <https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html>

   ![DFS](https://gmlwjd9405.github.io/images/algorithm-dfs-vs-bfs/dfs-example.png)

   

   

   * **너비 우선 탐색** (BFS: Breadth First Search) : 시작 정점에서 인접한 모든 정점들을 우선 방문한 후, 더이상 방문하지 않은 정점이 없을 때까지 방문했던 정점들을 다시 시작점으로 해서 모든 정점들을 차례로 방문하는 방법.

     ![BFS](https://gmlwjd9405.github.io/images/algorithm-dfs-vs-bfs/bfs-example.png)

     

2. **신장트리** : 그래프 안의 **모든 정점을 포함하는 트리**, **모든 정점들이 연결**되어 있어야 하고 **사이클을 포함하지 않는다**.

   

3. **최소 비용 신장트리** : **가중치가 부여된 무방향 그래프**에서 **신장 트리 비용의 최소화를 구하는 방법**. 

   * Prim
     * 시작하는 노드에 연결된 것 중에서 가중치가 최소인 노드를 선정합니다.
     * 선정된 노드에 연결된 것 중에서 가중치가 최소인 것을 선정합니다.
     * 이어진 노드에서 최솟값을 계속 선정하는 방법입니다.
   * Kruskal 
     * 전체 그래프를 보고 최소 가중치를 선정
     * 그 다음 최소 가중치를 가지는 것을 선정
     * 선정 시 사이클을 구성하는 것이 있으면 제외하고 작업진행. 동일한 것이 여러 개 있으면 임의로 하나를 선정하여 진행

##### 4) 구현 <https://m.blog.naver.com/occidere/220923695595> , https://sarah950716.tistory.com/12

1. ###### 배열 (matrix 이용) - 인접 행렬 그래프

   * **모든 정보 저장**

   * 장점 : 직관적 , 쉬운 구현

   * 단점 : 불필요한 정보 저장이 많음 -> 크기가 커지면 메모리 초과 발생

     ![단방향](https://t1.daumcdn.net/cfile/tistory/21029250584C0F2413)

     ​												[단방향 인접 행렬 그래프]

     

![무방향 인접 행렬 그래프](https://t1.daumcdn.net/cfile/tistory/2405384D584C11BC2E)

​														[무방향 인접 행렬 그래프]



2. ###### 연결리스트 - 인접 리스트 그래프

   * **갈 수 있는 곳만 저장**
   * 장점 : 필요한 정보만 저장 - > 메모리 절약
   * 단점 : 인접행렬에 비해 다소 어려움
   * List나 vector등의 자료구조를 이용하여 각 정점에서 이동가능한 정점들을 저장



![단방향인접리스트그래프](https://t1.daumcdn.net/cfile/tistory/2269874B584C17F301)

​														[단방향 인접 리스트 그래프]





![무방향인접리스트그래프](https://t1.daumcdn.net/cfile/tistory/265E074D584C26DD2B)

​														[ 무방향 인접 리스트 그래프 ]



##### 5) 트리와 그래프 비교

<https://gmlwjd9405.github.io/2018/08/13/data-structure-graph.html>

![graph-vs-tree](https://gmlwjd9405.github.io/images/data-structure-graph/graph-vs-tree.png)

## 4.14 프로그램 언어에서의 자료구조 지원

##### 1) 자바 컬렉션(Collection)에서 제공하는 자료구조 

1. HashSet, ArrayList, Vector, Stack, LinkedList, HashMap

   * HashSet : 값만 저장할 때 사용. 중복 허용하지 않는다. 따라서 Key나 Index 저장에 주로 사용되며 자료구조에서 리스트의 개념을 구현

   * ArrayList, Vector: 기존 배열의 크기 제한에 따른 문제를 해결한 것으로, 자료구조 중에서 배열의 개념을 구현. (즉, 동적 배열)

     [ArrayList vs Vector]: https://yeolco.tistory.com/94

     * Vector : 쓰레드에서 동기화를 기본적으로 수행 - 한 번의 하나의 스레드만 벡터의 메소드를호출할 수 있다. (Thread safe)
     * ArrayList : 쓰레드에서 동기화 되지 않은 상태. - 동시에 여러 스레드가 작업 가능 -> 명시적으로 동기화해 줄 필요가 있음.

   * Stack : Stack 구현
   * LinkedList : Queue 구현
   * HashMap; key 와 value 쌍으로 이루어진 데이터를 다룬다.

##### 2) C언어에서는 자바컬렉션을 'STL(Standard Template Library) 라이브러리' 라고 함. 

