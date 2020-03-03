package model;


////abstact
//public class Magician extends Character  {
//
//	@Override
//	public void attack(Hero hero) {
//		// TODO Auto-generated method stub
//		
//	}
//	
//}

//
////interface
//public class Magician implements ICharacter  {
//
//	@Override
//	public void attack(Hero hero) {
//		// TODO Auto-generated method stub
//		
//	}
//	
//}


// 다형성에 의해 Character이기도하고,  ICharacter이고, ICharacter1이고, ICharacter2이다.
public class Magician extends Character implements ICharacter, ICharacter1, ICharacter2  {

	@Override
	public void attack2(Hero hero) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void attack1(Person person) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void attack(Hero hero) {
		// TODO Auto-generated method stub
		
	}




	
}
