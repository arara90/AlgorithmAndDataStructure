package sort;

import java.util.Arrays;

public class sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] src = {2, 1, 8, 7, 9, 10, 6, 5, 4, 3};

// O(n*n)		
//		select(src);
//		bubble(src);
		insert(src);
		
// 분할 정복 		pivot에 따라 분할 
		//quick(src); // O(N*logN)  -- 
	}
	
	public static void select(int[] arr) {
		//시간복잡도 O(n*n) : 비효율
		int min, tmp;
		int index = 0;
		
		for( int i = 0; i < 10; i++) {
			min = 9999;
			for(int j=i; j<10; j++) {
				if (min > arr[j]) {
					min = arr[j];
					index = j;
				}
			}
			
			tmp = arr[i];
			arr[i] = arr[index];
			arr[index] = tmp;
			
		}
		System.out.println(Arrays.toString(arr));
	}
	
	public static void bubble(int[] arr) {
		//가장 효율성 떨어짐 O(n*n), 실재 수행은 선택정렬보다 느리다. (계속 자리를 바꾼다. 선택은 마지막에만 바꾼다 )
		int p, tmp;

		for ( int i = arr.length ; i > 1 ; i-- ) {
			p = 0;
			
			 while( p < i -1 ){
				if (arr[p+1] < arr[p]) {
					tmp = arr[p+1];
					arr[p+1] = arr[p];
					arr[p] = tmp;
				}
				p++;
			}
		}

		System.out.println(Arrays.toString(arr));
	}
	
	public static void insert(int[] arr) {
		// O(n*n) 중에 가장 빠르다. 적절한 위치에 필요할때만. 정렬되었다고 가정하는 것
		// [정렬됨] 대상원소 [비정렬] 대상 원소만 정렬된 애들 사이에 적절한 위치에 삽입
		// 1. 대상 원소 지정
		// 2. 내 바로 앞에 애부터 비교. 나보다 작으면 멈춰. 여기가 내자리
		// 거의 정렬된 상태에서 빠르다! 사용 자원도 적고, 빠르다. 효율적.

		int tmp;

		
		for(int i= 1; i < arr.length ; i++) {			
			for(int j = i ; j > 0 ; j--) {
				if(arr[j-1] < arr[j]) {
					break;
				}else {
					tmp = arr[j-1];
					arr[j-1] = arr[j];
					arr[j] = tmp;
				}
			}
		}
		System.out.println(Arrays.toString(arr));
	}
	
	
	public static void quick(int[] arr) {
		// 특정 값을 기준으로 큰 숫자와 작은 숫자를 나눈다.
		// pivot 있다! 가장 앞에있는 값을 pivot으로 많이한다.
		// 왼쪽에서 기준보다 큰 값, 오른쪽에서 기분보다 작은 값 하나씩 선택되면 둘이 바꿔준다.
		// 왼쪽포인트 index가 오른쪽 포인트 index보다 커지면 stop, 왼쪽 포인터 index에 pivot 삽입(엇갈린상황)
		if(arr.length < 2) {
			System.out.println(Arrays.toString(arr));
		}
		
		int key = 0;
		int i = 1; // 왼쪽 출발지점
		int j = arr.length - 1; // 오른쪽 출발 지점
		
		while(i<=j) { //엇갈릴때까지 반복
			while(arr[i] <= arr[key] ){
				
			}
		}	
	}
}
