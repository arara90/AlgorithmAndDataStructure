package InputOuput;

public class ThreadPractice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("1");
		
		//별도의 thread에서 동작하게 된다. 누가 더 빨리 하는지는 컴퓨토 마음 
		new Thread(new Runnable() { //runnable은 interface
			@Override
			public void run() { // run은 추상 method
				// TODO Auto-generated method stub
				for(int i = 0 ; i < 5 ; i++) {					
					try {//1초 후 실행.
						Thread.sleep(1000);
						System.out.println(Thread.currentThread().getName() + ":" + i );
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}
		}).start();
		
		// 람다식 (lambda) - 추상메서드 하나만 갖는 인터페이스
		new Thread(()-> {
			for(int i = 0 ; i < 5 ; i++) {					
				try {//1초 후 실행.
					Thread.sleep(1000);
					System.out.println(Thread.currentThread().getName() + ":" + i );
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}).start();
		System.out.println("2");
		
//		결과
//		1
//		2
//		Thread-0:0
//		Thread-1:0
//		Thread-0:1
//		Thread-1:1
//		Thread-0:2
//		Thread-1:2
//		Thread-0:3
//		Thread-1:3
//		Thread-0:4
//		Thread-1:4

	}

}
