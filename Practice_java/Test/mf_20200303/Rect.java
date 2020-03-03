package mf_20200303;

import java.io.*;
import java.util.*;

public class Rect {
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
//			Point p = new Point(scanner.nextInt(), scanner.nextInt());
//			Point q = new Point(scanner.nextInt(), scanner.nextInt());
//			Point r = new Point(scanner.nextInt(), scanner.nextInt());
//			Point s = new Point(scanner.nextInt(), scanner.nextInt());
	      
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

