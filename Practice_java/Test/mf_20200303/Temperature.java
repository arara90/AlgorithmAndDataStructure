package mf_20200303;

import java.util.*;
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Temperature {
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
//		4
//		00:00:00 TURN-ON-27
//		06:30:00 SET-29
//		08:00:00 SET-30
//		12:00:00 TURN-OFF
//		28.3이 되어야 한다.
		
		
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
