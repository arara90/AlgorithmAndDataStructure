---

---

# 검색(Search) 알고리즘

[TOC]





##  6.1 검색 알고리즘

> NoSQL? https://namu.wiki/w/NoSQL



##### 1) 검색 알고리즘

* 많은 데이터 속에서 원하는 데이터를 찾는 것.

##### 2) 정렬 알고리즘의 종류

1. 순차 검색 ( Sequential Search )
2. 이진 검색 ( Binary Serach )
3. 문자열 검색 ( String Search )

==========================================

1. KMP 검색 알고리즘을 사용한 문자열 검색
2. BM 검색 알고리즘을 사용한 문자열 검색

+)

6. 피보나치
7. 해쉬기반
8. 이진트리



##### 3) 시간 복잡도

https://onsil-thegreenhouse.github.io/programming/algorithm/2018/02/26/binary_search/ (순차, 이진)



## 6.2 순차 검색 알고리즘

##### 1) 순차 검색(Sequential Search) 

* 주어진 데이터를 처음부터 하나씩 검사하여 원하는 항목을 찾아가는 알고리즘

  

##### 2) 시간 복잡도 : O(n)

data = {1, 12, 8, 7, 2, 11, 5, 81, 29, 10}

* 평균 연산 횟수 
  * data에서 1을 찾으려면 1번, 12를 찾으려면 2번, 8을 찾으려면 3번..
  * 평균 연산 횟수  = ( 1 + 2 + 3 + 4+ ....+ 9 + 10 ) / 10 = (n+1) /2 =>O(n)



## 6.3 이진 검색 알고리즘

##### 1) 이진 검색(Binary Search)

* **오름차순으로 정렬된 데이터를 대상**으로 중앙값을 이용하여 검색하는 알고리즘

  https://cjh5414.github.io/binary-search/

  ![Binary Search](https://d2slyrdc8sel4f.cloudfront.net/crawler/1521190392binary-search1.png)

##### 2) 시간 복잡도 (https://onsil-thegreenhouse.github.io/programming/algorithm/2018/02/26/binary_search/)

* 한번 연산을 하면 탐색해야 할 n개의 숫자가 반으로 줄어든다. 즉, n(1/2)^1 ->  n(1/2)^2 -> ... -> n(1/2)^k

* k번 연산 후 탐색해야할 숫자의 개수는 한개입니다. 이를 식으로 나타내면  n(1/2)^k = 1

* n으로 나눈 후, 분모분자 뒤집자. -> 2^k = n

* 양변에 log2를 씌우면 k = log2(N) (로그 2의 N)

  

  => k가 연산 횟수 이기 때문에 이진탐색의 복잡도는 O(log2N)

  

## 6.4 문자열 검색 알고리즘

##### 1) 문자열 검색(String Search)

* 주어진 문자열에서 찾고자 하는 문자열이 있을 때, 해당 문자열의 위치를 찾는 알고리즘

* [알고리즘문자열-검색고지식한-검색-라빈카프-KMP-보이어무어](https://otrodevym.tistory.com/entry/알고리즘문자열-검색고지식한-검색-라빈카프-KMP-보이어무어)

##### 2) 시간복잡도

* O(N*M)

## 6.5 KMP 검색 알고리즘

##### 1) KMP 검색(KMP(Knuth, Morris, Partt) Search)

* 문자열 안에서 부분 문자열을 검색할 때 검색에 실패한 위치를 기반으로 비교할 필요없는 문자열은 건너뛰고, 다음번 검색 위치를 결정하는 알고리즘
* 왼쪽부터 오른쪽으로 비교하면서 접두부(prefix)와 접미부(suffix)를 경계를 통해 비교
* 문자열에서 일치하는 접두부(prefix)와 접미부(suffix)에 해당하는 구간은 경계라고 칭함
* https://bowbowbow.tistory.com/6

##### 2) 최대일치길이

* 접두사와 접미사가 일치하는 최대 길이
* 접두사와 접미사가 일치하는 경우에 한해서는 점프를 수행할 수 있다는 점에서 몹시 효율적

##### 3) 시간 복잡도 : O (N + M) 

* 원본 문자열 : N / 찾으려는 문자열 : M



## 6.6 BM 검색 알고리즘

##### 1) BM 검색(BM(Boyer, Moore) Search) 

* 검색할 문자열의 끝에서부터 비교하다가 일치하지 않는 문자를 만나면 검색할 문자열만큼 이동하여 검색 수행