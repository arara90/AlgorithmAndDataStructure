package model;

//내용이 없는 추상 class, method
// new 형식으로 만들 수 없다.
public abstract class Character extends Person {

	// abstract 모든 캐릭터가 attack이란 것을 가져야한다. 를 강제하고 싶을 때
	public abstract void attack(Hero hero);
	
}

interface ICharacter1{
	void attack1(Person person);
}

interface ICharacter2{
	void attack2(Hero hero);
}


// abstrack vs interface
