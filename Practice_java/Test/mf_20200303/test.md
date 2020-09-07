#### 문자열 정규화하기 **제출 완료**

 문제의 입력값은 각 언어의 표준입력(stdin) 함수를, 출력값은 표준출력(stdout) 함수를 사용해주세요.

 알파벳 대소문자로 이루어진 이름과 성이 주어질 때 이를 아래의 형식을 따르는 문자열로 변환하는 함수를 작성하시오.

- `{이름} {성}` 순서를 따르며 이름과 성 사이는 하나의 공백으로 구분한다.

- 이름과 성은 가장 첫 글자가 대문자이고 이후는 모두 소문자로 변환되어야 한다.

- - (예시) **이름:** `donGyi`, **성:** `kiM` 일 때 => **결과:** `Dongyi Kim`



#### 입력 형식

 첫 줄에는 테스트케이스의 수를 나타내는 100이하의 자연수 ***T\***가 주어진다.

이후 총 ***T\***줄에 걸쳐서 각 테스트케이스에 대한 입력이 차례로 주어진다.

- 각 테스트케이스는 한 줄에 걸쳐서 주어진다.
- 한 줄에 알파벳만으로 구성 된 두 문자열이 하나의 공백으로 구분되어  `F L`형식으로 주어지며 ***F\***와 ***L\***은 각각 이름과 성을 나타낸다.
- 두 문자열은 모두 알파벳으로만 구성된 100글자 이하의 문자열임이 보장된다.



#### 출력 형식

 각 테스트케이스에 대하여 두 줄에 걸쳐서 정답을 출력한다.

- 첫 줄에는 테스트케이스의 번호를 `Case #%d`형식으로 출력한다. 테스트케이스의 번호는 입력으로 주어진 순서대로 ***1~T\***로 부여한다.
- 두 번째 줄에는 문제에 주어진 조건에따라 형식화 된 이름 문자열을 한 줄에 출력한다. 성과 이름은 하나의 공백으로 구분되어야 한다.



입/출력 예시

⋇ 입출력 형식을 잘 지켜주세요.

␣ : 공백

↵ : 줄바꿈

−⇥ : 탭

보기 입력 1

1
donGyi ␣kiM

1
donGyi kiM

출력 1

Case ␣#1↵
Dongyi ␣Kim↵

Case #1
Dongyi Kim



보기 입력 2

3↵
mijoo ␣lee↵
JIAE ␣Yoo↵
jiSOO ␣seo

3
mijoo lee
JIAE Yoo
jiSOO seo

출력 2

Case ␣#1↵
Mijoo ␣Lee↵
Case ␣#2↵
Jiae ␣Yoo↵
Case ␣#3↵
Jisoo ␣Seo↵

Case #1
Mijoo Lee
Case #2
Jiae Yoo
Case #3
Jisoo Seo



```java
import java.io.*;
import java.util.*;

class Main {
	/** 
		@description
			알파벳으로 구성된 이름과 성을 입력받아 일정한 형식으로 합쳐 반환하는 함수

		@param first_name 알파벳으로 이루어진 이름 
		@param last_name  알파벳으로 이루어진 성
		@return           문제에 주어진 형식으로 합쳐진 문자열
 */
	
	public static String ChangeStr(String str){
		str = str.toLowerCase();
		char upper = Character.toUpperCase((str.charAt(0)));
		str = upper + str.substring(1, str.length());
		return str;
	}
		
	
	public static String getFormattedName(String firstName, String lastName){
		String formattedName;
		formattedName = ChangeStr(firstName) + " "  +  ChangeStr(lastName);
		return formattedName;
	}
	
	
	/* 
	** 메인 함수에는 테스트케이스와 입출력에 대한 기본적인 뼈대 코드가 작성되어 있습니다. 
	** 상단의 함수만 완성하여도 문제를 해결할 수 있으며, 
	** 메인 함수를 제거한 후 스스로 코드를 모두 작성하여도 무방합니다.
	** 단, 스스로 작성한 코드로 인해 발생한 에러 등은 모두 참가자에게 책임이 있습니다.
	*/
  public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//테스트케이스의 수를 입력받는다 
		int caseNum = scanner.nextInt();
		
		//테스트케이스 수 만큼 반복하며 데이터를 입력받고 정답을 출력한다
		for(int caseIndex = 1; caseIndex <= caseNum; caseIndex++)
		{
			//성과 이름을 차례로 입력받는다 
			String firstName = scanner.next();
			String lastName = scanner.next();
			
			//주어진 함수를 이용해 포메팅된 이름 문자열을 얻는다 
			String answer = getFormattedName(firstName, lastName);
			
			//정답을 형식에 맞게 출력한다
			System.out.printf("Case #%d\n", caseIndex);
			System.out.println(answer);
		}
  }
}

```

* 참고 : 위 제시된 코드에서는 객체를 생성하고 있지 않기 때문에 모든 함수를 static으로 지정해야만 정상적으로 동작한다. 그렇지 않으면 

> non static method cannot be referenced from a non static context

에러가 생길 것이다! 



#### 실내 온도 **제출 완료** 

### 오답

-> int, double 계산시 double로 자동 형변환

-> hashmap으로 재구현해보기





 문제의 입력값은 각 언어의 표준입력(stdin) 함수를, 출력값은 표준출력(stdout) 함수를 사용해주세요.

 대부분의 냉난방 장치는 리모콘을 통해 원격으로 전원을 켜거나 끌 수 있고, 온도를 조절할 수 있다. 구름 생활가전의 냉난방 장치는 리모콘으로부터 수신한 명령에 대한 로그를 저장한다. 구름 생활가전의 엔지니어들은 이 로그를 분석하여 해당 날짜에 냉난방기가 켜져 있던 동안의 평균 온도를 계산하고자 한다. 하루 동안 냉 난방기가 수신한 명령어 로그가 주어질 때 작동 시간동안의 평균 온도를 계산하는 프로그램을 작성하시오.



 명령어 로그들은 시간 순서대로 주어지며, 각 로그는 한 줄로 `{타임스탬프} {명령어}` 형식으로 주어진다. 타임스탬프와 명령어는 하나의 공백으로 구분된다. 모든 로그는 아래의 세 유형 중 하나이다.

- `HH:MM:SS SET-**XX**` 

- - 즉시 냉난방기의 온도를 ***XX\***도로 바꾸는 명령이다.
  - 온도를 나타내는 값은 항상 두 자리 10진수이다.

- `HH:MM:SS TURN-ON-**XX**`

- - 즉시 냉난방기의 전원을 켜는 명령이다. 
  - 그리고 즉시 냉난방기는 온도를 ***XX\***도로 설정하여 동작을 시작한다.

- `HH:MM:SS TURN-OFF` 

- - 즉시 냉난방기의 전원을 끄는 명령이다.



 타임스탬프는 숫자와 콜론으로 이루어진 8자리 형식의 문자열이며, `00:00:00`~`23:59:59` 범위 의 시간을 나타내는 값이다. 타임 스탬프는 해당 명령어가 수신되는 시간을 나타낸다. 모든 명령어는 수신되는 즉시 실행된다. 편의상 자정에 냉난방기가 켜져있는 경우는 없다고 가정한다.

 냉난방기가 켜져 있는데 전원을 켜는 명령어가 중복해서 들어오거나, 냉난방기가 꺼져 있을 때 전원 종료나 온도 조절 명령어가 들어오는 경우는 존재하지 않는다.



#### 입력 형식

 첫 줄에는 해당 날짜에 남겨진 명령어 로그의 수를 나타내는 3,000이하의 자연수 ***N\***이 주어진다.

이후 총 ***N\***줄에 걸쳐서 한 줄에 하나 씩 로그가 시간순서대로 주어진다. 로그는 문자열로 입력되며 그 형식은 문제에 주어진 형식을 따른다.

 각 로그들의 타임스탬프는 최소 1초 이상의 시간 간격을 가진다.

 타임스탬프는 항상 8글자 문자열로 표현되며, 온도는 15도 이상 35도 이하의 두 자리 자연수다.



#### 출력 형식

 냉난방기가 동작한 동안의 평균 온도를 소수점 두 번째 자리에서 반올림하여 첫 번째 자리까지 출력한다.



입/출력 예시

⋇ 입출력 형식을 잘 지켜주세요.

␣ : 공백

↵ : 줄바꿈

−⇥ : 탭

보기 입력 1 --**오답**

4↵
00:00:00  TURN-ON-27↵
06:30:00  SET-29↵
08:00:00  SET-30↵
12:00:00  TURN-OFF

4
00:00:00 TURN-ON-27
06:30:00 SET-29
08:00:00 SET-30
12:00:00 TURN-OFF

출력 1

28.2↵

28.2



보기 입력 2

7↵
01:03:00 ␣TURN-ON-20↵
03:30:00 ␣TURN-OFF↵
04:00:00 ␣TURN-ON-35↵
05:00:00 ␣TURN-OFF↵
07:00:00 ␣TURN-ON-30↵
10:00:00 ␣SET-25↵
12:00:00 ␣TURN-OFF

7
01:03:00 TURN-ON-20
03:30:00 TURN-OFF
04:00:00 TURN-ON-35
05:00:00 TURN-OFF
07:00:00 TURN-ON-30
10:00:00 SET-25
12:00:00 TURN-OFF

출력 2

26.5↵

26.5





```java
import java.util.*;
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Locale;
import java.util.Date;

class Main {

	/** 
		@description
			로그를 이용해 냉난방기가 동작한 동안의 평균 온도를 계산하는 함수
		@param logs 시간 순서로 저장된 로그들
		@return     냉난방기 동작 시간 동안의 평균 온도
	*/
	
	public static double convertTime(String str){		
		SimpleDateFormat f = new SimpleDateFormat("HH:mm:ss");
		Date time = new Date();
		
		try {
			time = f.parse(str);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		double res = time.getTime()/1000;
		
		// long diff = d1.getTime() - d2.getTime();
		// long sec = diff / 1000;
		// System.out.println(sec);

		return res;
	}
	
	public static double calculateAverageTemperature(String[] logs)
	{
		double averageTemperature = 0.0;
		
		String[] row  = new String[2]; //[시간, 명령어]
		String[] commands  = new String[2]; // [명령, 온도]

		int currntTemp = 0;  		// 현재 온도
		double startTime = 0d;	// 새로운 온도 시작 시간
		double endTime = 0d;		// 끝난 시간
		double duration = 0d;		// 지속시간 (endTime - startTime)
		
		//평균 계산을 위한 최종값
		double totalSum = 0d;
		double totalTime = 0d;
		
		
		for( int i = 0 ; i < logs.length ; i ++ ){
			// 로그 기록 분리
			row = logs[i].split(" "); //0: time, 1: 명령, 2: 온도
            // -> // [0] time, [1] 명령 로 주석 수정할 것 ㅠㅠ 
			
			//명령어
			commands = row[1].replace("TURN-", "").split("-"); // [ {on || off || Set} , temp ]

			//명령어에 따른 로직
			if(commands[0].equals("ON")){
				// 1.현재 온도, 시작시간 기록하기
				currntTemp = Integer.parseInt(commands[1]);
				startTime = convertTime(row[0]);
				
			} else if(commands[0].equals("SET")){
				// 1. 이전 온도 지속시간 구하기
				endTime = convertTime(row[0]);
				duration = endTime - startTime;
				
				//2. 총 평균을 위해 total 값 저장
				totalTime = totalTime + duration;
				totalSum = totalSum + (duration * currntTemp);
				
				//3. 시작시간, 현재온도 갱신
				currntTemp = Integer.parseInt(commands[1]);
				startTime = endTime;	
				
			} else if(commands[0].equals("OFF")){
				// 1. 이전 온도 지속시간 구하기
				endTime = convertTime(row[0]);
				duration = endTime - startTime;
				
				//2. 총 평균을 위해 total 값 저장
				totalTime = totalTime + duration;
				totalSum = totalSum + (duration * currntTemp);
				
			} else{
				break;
			}
		}

		averageTemperature = totalSum / totalTime;
		return averageTemperature;
	}
	
	/* 
	** 메인 함수에는 테스트케이스와 입출력에 대한 기본적인 뼈대 코드가 작성되어 있습니다. 
	** 상단의 함수만 완성하여도 문제를 해결할 수 있으며, 
	** 메인 함수를 제거한 후 스스로 코드를 모두 작성하여도 무방합니다.
	** 단, 스스로 작성한 코드로 인해 발생한 에러 등은 모두 참가자에게 책임이 있습니다.
	*/
  public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//로그 문자열의 수를 입력받는다
		int logNum = scanner.nextInt();
		scanner.nextLine(); //불필요한 개행을 제거
		
		//각 로그를 차례로 입력받아 logs에 저장한다
		String[] logs = new String[logNum];
		for(int logIndex = 1; logIndex <= logNum; logIndex++)
		{
			logs[logIndex-1] = scanner.nextLine().trim();
		}
		
		//주어진 함수를 이용해 평균 온도를 계산한다 
		double answer = calculateAverageTemperature(logs);
		
		//계산한 평균 온도를 형식에 맞게 출력한다
		System.out.printf("%.1f\n", answer);
  }
}

```





#### 영역 교차 검사하기 **제출 완료**

* x,y가 뒤집혔지만 문제를 푸는데에는 이상 없음

  

 문제의 입력값은 각 언어의 표준입력(stdin) 함수를, 출력값은 표준출력(stdout) 함수를 사용해주세요.

 이차원 평면에 존재하는 두 직사각형의 정보가 주어질 때, 두 직사각형이 교차하는 영역의 넓이를 출력하는 프로그램을 작성하시오. 만약 두 직사각형이 교차하지 않는다면 영역의 넓이는 0이 된다.

 두 직사각형의 네 변은 항상 좌표축과 수직/수평한 방향으로 주어지며 넓이는 0보다 큰 값을 가진다. 직사각형의 정보는 직사각형을 구성하는 네 개의 모서리 중 대각선으로 마주보는 두 점의 좌표로 주어진다. 

 

![img](data:image/png;base64,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iQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7OzAAkEUAA0D55X2dmAJIIIABon7yvMzMASQQQALRP3teZGYAkAggA2ifv68wMQBIBBADtk/d1ZgYgiQACgPbJ+zozA5BEAAFA++R9nZkBSCKAAKB98r7O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)

***<두 사각형을 이루는 네 점이 주어진 예시>\***



 위의 예시에서는 첫 번째 사각형을 이루는 두 점 ***R, S\***와 두 번째 사각형을 이루는 두 점 ***P, Q\***가 주어진 상황이다. 이 경우 두 사각형이 교차한 영역의 넓이는 6이 된다.



#### 입력 형식

 문제의 입력은 총 네 줄에 걸쳐서 주어진다. 모든 좌표는 절대값이 10,000이하인 정수다.

- 첫 번째 줄에는 점 ***P\***에 대한 좌표가 `X Y`형식으로 주어진다.
- 두 번째 줄에는 점 ***Q\***에 대한 좌표가 `X Y`형식으로 주어진다.
- 세 번째 줄에는 점 ***R\***에 대한 좌표가 `X Y`형식으로 주어진다.
- 네 번째 줄에는 점 ***S\***에 대한 좌표가 `X Y`형식으로 주어진다.

***P\***와 ***Q\***는 한 직사각형에서 대각선으로 마주보는 두 점이다. 마찬가지로 ***R\***과 ***S\***는 한 직사각형에서 대각선으로 마주보는 두 점이다.

모든 사각형은 네 변의 길이와 넓이가 0보다 크다.



#### 출력 형식

 한 줄에 두 직사각형이 교차하는 영역의 넓이를 정수로 출력한다.



입/출력 예시

⋇ 입출력 형식을 잘 지켜주세요.

␣ : 공백

↵ : 줄바꿈

−⇥ : 탭

보기 입력 1

-7 5↵
0 0↵
-3 -3↵
4 2

-7 5
0 0
-3 -3
4 2

출력 1

6↵

6



보기 입력 2

1 ␣1↵
0 ␣0↵
2 ␣2↵
1 ␣1

1 1
0 0
2 2
1 1

출력 2

0↵

0





```java
import java.io.*;
import java.util.*;


public class Main {
	public static final Scanner scanner = new Scanner(System.in);
	
	/** 
  @description
    두 사각형을 이루는 네 점을 파라미터로 받아 교차하는 영역의 넓이를 반환하는 함수

  @param p	첫 번째 사각형의 한 점, q와 대각선상에 존재한다.
  @param q	첫 번째 사각형의 한 점, p와 대각선상에 존재한다.
  @param r	두 번째 사각형의 한 점, s와 대각선상에 존재한다.
  @param s	두 번째 사각형의 한 점, r과 대각선상에 존재한다.
  @return   두 직사각형이 교차하는 영역의 넓이
	**/
	
	
	public static void draw(Point p1, Point p2, int[][] canvas){		
		int rect_x_min = 0;
		int rect_x_max = 0;
		int rect_y_min = 0;
		int rect_y_max = 0;
		
		
		if (p1.x < p2.x){
			rect_x_min = p1.x;
			rect_x_max = p2.x;
		}else{
			rect_x_min = p2.x;
			rect_x_max = p1.x;
		}
		
		if (p1.y < p2.y){
			rect_y_min = p1.y;
			rect_y_max = p2.y;
		}else{
			rect_y_min = p2.y;
			rect_y_max = p1.y;
		}
		
		for(int i = rect_x_min; i < rect_x_max ; i++){
			for(int j = rect_y_min; j < rect_y_max ; j++){
				canvas[i][j]++;
				}
		}
		
	
	}
	
	public static int getDuplicatedArea(Point p, Point q, Point r, Point s)
	{
		int area = 0; //두 사각형이 교차하는 영역의 넓이
		
		int[] x_points = {p.x, q.x, r.x, s.x};
		int[] y_points = {p.y, q.y, r.y, s.y};
		
		int x_min = 0;
		int y_min = 0;
		int x_max = 0;
		int y_max = 0;
		
		
	// 좌표 offset - min값을 0으로 표준화.
		for(int i = 0; i<4; i++){
			if( x_min > x_points[i]){
				x_min = x_points[i];
				}
			if( x_max < x_points[i]){
				x_max = x_points[i];
				}
			if( y_min > y_points[i]){
				y_min = y_points[i];
				}
			if( y_max < y_points[i]){
				y_max = y_points[i];
				}
		}
		
		x_max = Math.abs(x_max - x_min); 
		y_max = Math.abs(y_max - y_min); 
		
		for(int i = 0; i<4; i++){
			x_points[i] = Math.abs(x_points[i] - x_min); 
			y_points[i] = Math.abs(y_points[i] - y_min);
		}
		

		p.setX(x_points[0]);
		p.setY(y_points[0]);
		
		q.setX(x_points[1]);
		q.setY(y_points[1]);
		
		r.setX(x_points[2]);
		r.setY(y_points[2]);
		
		s.setX(x_points[3]);
		s.setY(y_points[3]);
		
		// canvas에그리기
		int[][] canvas = new int[x_max][y_max];
		draw(p, q,canvas);
		draw(r, s,canvas);
		
		//겹치는 영역 너비
		for(int i = 0; i < x_max ; i++){
			for(int j = 0; j < y_max ; j++){
				if (canvas[i][j] > 1) area++; 
			}
		}
		
		// 최종 canvas 출력
		// for(int i = 0; i < x_max ; i++){
		// 	for(int j = 0; j < y_max ; j++){
		// 		System.out.print(canvas[i][j]);
		// 	}
		// 	System.out.println();
		// }
	
	
		
		return area;
	}
	
	/* 
	** 메인 함수에는 테스트케이스와 입출력에 대한 기본적인 뼈대 코드가 작성되어 있습니다. 
	** 상단의 함수만 완성하여도 문제를 해결할 수 있으며, 
	** 메인 함수를 제거한 후 스스로 코드를 모두 작성하여도 무방합니다.
	** 단, 스스로 작성한 코드로 인해 발생한 에러 등은 모두 참가자에게 책임이 있습니다.
	*/
  public static void main(String[] args) {
		//네 점 p, q, r, s를 차례로 입력받는다.
		//Point p = new Point(scanner.nextInt(), scanner.nextInt());
		//Point q = new Point(scanner.nextInt(), scanner.nextInt());
		//Point r = new Point(scanner.nextInt(), scanner.nextInt());
		//Point s = new Point(scanner.nextInt(), scanner.nextInt());
      
        Point p = new Point(-7,5);
		Point q = new Point(0,0);
		Point r = new Point(-3,-3);
		Point s = new Point(4,2);
		
		
		//주어진 함수를 통해 교차하는 영역의 넓이를 계산한다 
		int answer = getDuplicatedArea(p, q, r, s);
		
		//정답을 형식에 맞게 출력한다 
		System.out.println(answer);
  }
}

/** 
  @description
    하나의 점(좌표)를 나타내는 클래스
**/
class Point{
	public int x;
	public int y;
	public Point(int x, int y)
	{
		this.x = x;
		this.y = y;
	}
	
	public int getX()
	{
		return this.x;
	}
	
	public int getY()
	{
		return this.y;
	}
	
	public void setX(int x)
	{
		this.x = x;
	}
	public void setY(int y)
	{
		this.y = y;
	}
}

```





2017/18시즌 영국 축구 1부 리그의 득점과 도움 기록을 가진 테이블이 있습니다.

도움이 5개 이상인 선수 중에서 득점 기록에 대하여 내림차순으로 정렬하여 출력 형식에 맞게 출력하세요.



테이블 구조는 아래와 같습니다.

**PLAYERSTAT**

| **NAME(이름)** | **GOALS(득점)** | **ASSISTS(도움)** |
| -------------- | --------------- | ----------------- |
| VARCHAR(20)    | INT             | INT               |



출력 형식은 아래와 같습니다.

 \- **필드의 이름이 반드시 일치해야 합니다.**

 \- 출력에서 각 열은 탭문자로 구분됩니다.

예시)

NAME	GOALS	ASSISTS

A	44	5

B	34	8

C	31	22

...

Z	0	13

```sql
SELECT NAME, GOALS, ASSISTS
FROM PLAYERSTAT
WHERE ASSISTS > 4
ORDER BY GOALS DESC
```



#### 학생별 강의수 구하기 **제출 완료**

모든 학생의 목록을 뽑고 각 학생이 얼마나 많은 강의를 수강하고 있는지 확인하는 질의문을 작성하세요. 많은 강의를 수강하는 학생이 먼저 나오도록 해주세요.



**테이블 스키마** (* 표시 컬럼은 primary key 입니다)

Courses

| **CourseID \*** | **CourseName** | **TeacherID** |
| --------------- | -------------- | ------------- |
| BIGINT(20)      | VARCHAR(100)   | BIGINT(20)    |



Students

| **StudentID \*** | **StudentName** |
| ---------------- | --------------- |
| BIGINT(20)       | VARCHAR(100)    |



StudentCourses

| **CourseID \*** | **StudentID \*** |
| --------------- | ---------------- |
| BIGINT(20)      | BIGINT(20)       |



```sql
SELECT S.StudentName, COUNT(SC.CourseID) as COUNT
FROM Students S 
	LEFT OUTER JOIN StudentCourses SC
	ON S.StudentID = SC.StudentID 
GROUP BY S.StudentName
ORDER BY COUNT DESC
```

... 바보인가 , 그룹핑을 StudentName이 아닌 StudentID로 하는 것이 맞았을 것이다.

빠르게 풀려고 출력에만 집중한 탓..T.T 

