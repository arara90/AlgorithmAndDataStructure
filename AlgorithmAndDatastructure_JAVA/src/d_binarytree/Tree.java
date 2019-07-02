package d_binarytree;


//이진트리 생성, 자료 추가/조회 기능 제공

public class Tree {
	TreeNode topNode = null;
	
	public void add(int key, Object value) {
		if(topNode == null)
			topNode = new TreeNode(key,value);
		else
			// topNode를 기준으로 추가하게 된다.
			topNode.add(key, value);
	}
	
	// 전달받은 key값을 갖는 node 찾아서 주기
	public Object get(int key) {
		return topNode == null? null : topNode.find(key);
	}
	
}
