# Dynamic Programming

> 내용  : http://blog.naver.com/ndb796/221233570962

> 완전 탐색 ; 재귀 호출을 이용해 최적화 문제를 푸는 것
>
> 재귀호출 시 : 원소들의 총 개수, 더 골라야 할 원소들의 개수, 지금까지 고른 원소들의 번호

##### 1) 다이나믹 프로그래밍(동적 계획법)

* **부분 상황으로 정의할 수 있는가?**

* 주로 경우의 수를 세거나 확률을 계산하는 문제

* 하나의 문제를 단 한 번만 풀도록 하는 알고리즘 

* 분할 정복 기법은 동일한 문제를 다시 푼다는 단점이 있다. -> 정렬은 빠르다 / 피보나치는 비효율적
* 피보나치 수열은 특정한 숫자를 구하기 위해 그 앞에 있는 숫자와 두 칸 앞에 있는 숫자의 합을 구해야함
  * 분할 정복을 이용할때 12가 세번씩이나 반복 계산

##### 2) 언제?

* 가정1. 큰 문제를 작은 문제로 나눌 수 있다.

* 가정2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.



##### 3) 메모이제이션(Momorization)

* 이미 계산한 결과는 배열(캐시)에 저장 -> 나중에 동일한 계산시에 저장된 값을 단순히 반환 
* 시간과 공간 트레이드 오프로 동적 계획법 알고리즘 만들기



##### 4) 다이나믹 타일링 문제 풀어보기

* 11726 
