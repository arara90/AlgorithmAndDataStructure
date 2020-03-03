package model;

public class Hero extends Character {
	private boolean isFlying;
	
	public Hero(String name) {
		setName(name);
		
	}

	public boolean isFlying() {
		return isFlying;
	}

	public void setFlying(boolean isFlying) {
		this.isFlying = isFlying;
	}
	
	// 추상 메소드는 상송 받은 쪽에서 무조건 구현을 해줘야한다.
	@Override
	public void attack(Hero hero) {
		System.out.println(this.getName() + "은 " + hero.getName() + "과 싸움을 했다.");
		
	}
	

}
