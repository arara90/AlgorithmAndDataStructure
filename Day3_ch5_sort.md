##  5.1 정렬 알고리즘

<https://www.growingwiththeweb.com/2015/06/bucket-sort.html>

* auxiliary memory : 보조기억장치

##### 1) 정렬 알고리즘의 종류

1. 버킷 (Bucket)

2. 선택 (Selection)

3. 삽입 (Insert)

4. 병합 (Merge)

5. 힙 (Heap)

6. 기수 (Radix)

7. 교환 ( Exchange )

8. 셀 (Shell)

9. 퀵 (Quick) - C언어 STL(표준라이브러리)로 제공하는 정렬

2) 시간 복잡도

![](https://gmlwjd9405.github.io/images/algorithm-insertion-sort/sort-time-complexity.png)



> ## 5.2 버킷 정렬 
>
> ##### 1) 버킷 정렬 알고리즘 

* 자료를 버킷이라는 단위 기억장소에 정렬하고 버킷별 키 값에 따라 다시 정렬하는 알고리즘

* 데이터가 특정 범위 내에 확률적으로 균등하게 분포한다고 가정할 수 있을 때 적용.

  (그림출처 : <http://egloos.zum.com/Duckkk/v/668549> )

  ![추상적개념도](http://pds19.egloos.com/pds/201106/15/22/c0130622_4df7a1c95e65a.png)   ![](http://pds21.egloos.com/pds/201106/15/22/c0130622_4df7a1d6adbd7.gif)

   <https://ratsgo.github.io/data%20structure&algorithm/2017/10/18/bucketsort/>

  두번째 그림과 같이 10개의 데이터 AA가 주어졌을 때 같은 크기의 버킷 BB를 만듭니다. 만약 AA의 분포가 균등하다면 각 버킷에는 1~2개의 요소만 속해 있을 것입니다. 
  이렇게 1~2개 값들만 있는 버킷 하나를 정렬하는 데 필요한 계산복잡성은 O(1)O(1)이 될 것이고, 
  이 작업을 nn개 버킷에 모두 수행한다고 하면 전체적인 계산복잡성은 O(n)O(n)이 될 것입니다. 이것이 바로 버킷 정렬이 노리는 바입니다.

  

##### 2) 사용 방법

- 데이터 nn개가 주어졌을 때 데이터의 범위를 nn개로 나누고 이에 해당하는 nn개의 버킷을 만든다.

- 각각의 데이터를 해당하는 버킷에 집어 넣는다. (C 등에서는 [연결리스트](https://ratsgo.github.io/data%20structure&algorithm/2017/09/30/list/)를 사용하며 새로운 데이터는 연결리스트의 head에 *insert*한다)

- 버킷별로 정렬한다.

- 이를 전체적으로 합친다.

  

> ## 5.3 기수 정렬 
>
> ##### 1) 기수 정렬 알고리즘 

- 버킷 정렬의 한계? 모양에 따른 제한. 즉, 데이터가 1, 1000이면 1000개의 데이터 공간이 필요한 문제. 이를 개선한 것이 기수정렬
- **각 자릿수별로 버킷 정렬을 반복 수행**하는 방법

##### 2) 사용 방법 

<https://juff.tistory.com/entry/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-7-%EA%B8%B0%EC%88%98-%EC%A0%95%EB%A0%ACRadix-Sort> 

1. 정렬할 데이터 확보

2. 각자릿수는 0-9값을 가짐

3. 데이터 1의 자릿수를 기준으로 버킷정렬

4. 데이터 2의 자릿수를 기준으로 버킷정렬

5. 데이터 3의 자릿수를 기준으로 버킷정렬

6. Queue(FIFO) 를 이용해 pop하면 최종적으로 정렬된 결과를 얻을 수 있다! 

   

## 5.4 선택 정렬 

##### 1) 선택 정렬 알고리즘 

* 가장 작은 데이터를 찾아(선택) 가장 앞에 있는 데이터화 교환하는 알고리즘

<img src="https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png" alt="drawing" width="500"/>



## 5.5 교환 정렬 (≒버블정렬)

##### 1) 교환 정렬 알고리즘 

- 첫번째 요소와 다른 요소들을 비교하고 교환하는 방식으로 진행
- 책에서는 bubble과 혼란이 오니 책 내용은 보지 말 것.

##### 2) 교환 vs 버블정렬 ( <http://blog.naver.com/PostView.nhn?blogId=ryutuna&logNo=100123462798> )

​         How is the exchange sort different from the bubble sort? : https://www.codingunit.com/exchange-sort-algorithm>

* 요소들을 비교하는 방법에 차이가 있음

* **교환정렬은** 첫번째 요소와 다른 요소들을 비교하고 교환하는 방식으로 진행

* **버블정렬은**  **인접한 요소들**끼리만 비교하며 교환 -> 모든 정렬이 끝난 후에도 반드시 final pass가 한번 더 돌아서 정렬됐는지 체크해야한다. 

* **교환정렬** : 첫번째 요소에 대한 sort가 끝나면 두번째 요소에 대해 비교시작하고, 모든 배열이 올바르게 정렬되면 끝난다

  **Exchange sort** (https://www.youtube.com/watch?v=KKdKhSd2MPE)

  ![Exchange sort](https://github.com/arara90/images/blob/master/exchange_sort.jpg?raw=true)

​	**Bubble**

​	![bubble sort](https://github.com/arara90/images/blob/master/bubblesort.jpg?raw=true)



## 5.6 삽입 정렬 알고리즘

##### 1) 삽입(Insert) 정렬 

* 



## 5.7 쉘 정렬 알고리즘

##### 1) 쉘(shell) 정렬 

- 삽입 정렬의 느린 속도 보안
- 데이터의 그룹을 나누어 그룹 안에서 쉘 정렬을 수행하고 마지막에 삽입정렬을 수행



## 5.8 병합 정렬 알고리즘

##### 1) 병합(Merge) 정렬 

- 데이터를 분할한 다음 계산 후 합쳐서 정렬

##### 2) 2차 병합 정렬 알고리즘

* 이미 정렬된 데이터 무리를 하나로 정렬하기 위한 알고리즘 
* 무리의 맨 앞의 수만을 비교하여 정렬



## 5.9 퀵 정렬 알고리즘

##### 1) 퀵(Quick) 정렬 

- 중앙 값 정렬 방식을 확장해서 개발한 방식
- 임의로 선정한 값을 기준으로 데이터 2등분, (작은 부분, 큰부분)
- 그 분리된 더미 속에서 임의의 값 기준으로 2등분 -> 반복 



## 5.10 힙 정렬 알고리즘

##### 1) 힙(heap) 정렬 

- 



## 5.11 정렬 알고리즘 선택 기준 

##### ![](https://github.com/arara90/images/blob/master/sorts.jpg?raw=true)

