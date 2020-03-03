package Basic;

import java.util.ArrayList;
import java.util.Date;
import java.util.Random;
import java.util.Scanner;

import model.Person;
import model.Hero;
import model.Character;
import model.ICharacter;
import model.Magician;

public class Basics {

	//static : 프로그램이 실행될 때 메모리에 로드되는 부분 (class와는 별도 영역)
	public static void main(String[] args) {
		int x = 30;
		final int y = 30; //변화 싫어
		short s = 30;
		long l = 30L;
		
		int i = (int)30L; // type casting 큰 값을 작은 상자에
		long ll = 30; // 작은 값을 큰 상자에 -> 자동 형변환
		
		
		double dd = 30.3; //실수 범위가 더 크다
		float ff = 30.0f; //
		
		dd = ff; // 자동형변환
		ff = (float)dd; // 강제 형변환
		
		boolean isMarried = true;
		char c = 'a';
		String str = "안뇽";
				
		System.out.println(str);
		System.out.printf("저는 %s입니다. 나이는 %d이고, 키는 %f입니다.\n", "홍길통", 20, 170.5f);
		
		String str2 = String.format("저는 %s입니다. 나이는 %d이고, 키는 %f입니다.", "홍길통", 20, 170.5f);
		System.out.println(str2);
		
		
		//Math
		System.out.println(Math.max(10, 30)); // min, abs
		
		//문자열 <-> 숫자열
		String str1 = "100";
		int ii = Integer.parseInt(str1);   //str -> num
		String str11 = String.valueOf(ii); //num -> str
		
		//Random
		Random random = new Random();
		int rand = random.nextInt(4) + 5 ; //  5- 9
		System.out.print(rand);
		
		// 문자입력
//		Scanner scanner = new Scanner(System.in);
//		System.out.println(scanner.next());
//		String scstr = scanner.next();
//		int sci = scanner.nextInt();
//		long scl = scanner.nextLong();
		
		//조건문
		int a = 10;
		if(a > 5) {
			System.out.println("참");
		}
		else if(a>3) {
			System.out.println("글쎄");
			}
		else {
			System.out.println("거짓");
		}
		

		String strr;
		strr = isMarried ? "함" : "안함";
		System.out.println(strr);
		// 조건문 Switch
		switch(strr) {
			case "함" : 
				System.out.println("ㅇㅇㅇ");
				break; // break 안하면 밑에거 실행됨
			case "안함" :
				System.out.println("xxx");
				break;
			default:
				System.out.println("몰라유");
		}
				
		//반목문 (continue, braek)
		for(i = 0; i < 10 ; i++) {
			
			if (i==6) {
				continue; // fi가 6이면 pass (실행안하고 7로 넘어간다.)
			}
			
			if(i==8) {
				break; // 8이면 반복문 빠져나간다.
			}
		}
		
		System.out.printf("i : %d", i);
		
		
		
		//배열
		int[] score;
		score = new int[5]; // 초기화는 0으로, String은 null로 들어있다.
		
		int[] arr = new int[5];		
		int count = score.length;
		score[0] = 10;
		
		int[] score2 = new int[] {1,2,3,4,5};
		int[] score3 = {1,2,3,4,5};
		
		String[] names = {"홍dd", "이"};
		String[] names2 = new String[2];
		
		System.out.println(names[0].length()); 
//		System.out.println(names2[0].length()); //nullpointerException
		
		// 리스트
		// 원하는 곳에 빠르게 데이터 삽입, 삭제
		ArrayList<Integer> scoreList = new ArrayList<>();
		scoreList.add(10);
		scoreList.add(20);
		scoreList.add(30);
		scoreList.add(2,1000); // index=2 자리에 1000추가.
		System.out.println(scoreList);
		scoreList.remove(2);
		System.out.println(scoreList);
		
		
		// 오버로드
		add(20,10);
		add(20,10,5);
		System.out.println(add(1,2,3,4,5));
		
		
	
		
		Person person = new Person();
		Person person2 = new Person("홍길동", 10);
		System.out.println(person);
		System.out.println(person2);
			
		Hero hero1 = new Hero("슈퍼맨");
		System.out.println(hero1.isFlying());
		
		Hero hero2 = new Hero("배트맨");
		hero2.isFlying();
		
		hero1.attack(hero2);
		
		
		// 추상클래스와 인터페이스 (상속 : Person > 추상 class Character, interface ICharacter > Magician, Hero) 
		
		Character chracter = new Hero("슈퍼맨2"); // 추상클래스는 new 할 수 없지만, 상속받은해로 할 수 있다.
		
		
		//다형성		
		Character magician2 = new Magician();	
		Magician magician = new Magician();
		ICharacter magiciani = new Magician();
		
		if(magician instanceof Magician) {
			System.out.println( "magician: I'm a Magician!");
		} 
		
		if(magician2 instanceof Magician) {
			System.out.println( "magician2: I'm a Magician!");
		} 
		
		if(magiciani instanceof Magician) {
			System.out.println( "magiciani: I'm a Magician!");
		} else {
			System.out.println( "magiciani: I'm not a Magician!");
		}
		
		// 
		ArrayList<Character> characterAL = new ArrayList<>();
		characterAL.add(magician);
		characterAL.add(magician2);
//		characterAL.add(magiciani); //error -> Character 범위까지만 가능 Magician 보러가봐! 
		characterAL.add(hero1); //hero1 도 Character 상속받음
		
		
		
	}
	
	
	
	//오버로드
	public static void add(int x, int y) {
		System.out.println(x+y);
		
	}
	
	public static void add(int x, int y, int z) {
		System.out.println(x+y+z);
		
	}

	public static int add(int ... numbers) {
		//... : 0개부터 n개, 배열로 들어온다.
		int sum = 0;
		for(int i = 0; i < numbers.length; i++) {
			sum = sum + numbers[i];
		}
		
		return sum;
		
	}

	
	
	//Generic
	
	
	

	

}





