package d_binarytree;

//이진트리를 구성하는 실제적인 클래스
public class TreeNode { 
	private int itsKey; 						// 노드의 key값
	private Object itsValue; 					// 노드의 value값
	private TreeNode nodes[] = new TreeNode[2];	// 자식 노드 두개를 갖으므로 두개의 node를 갖는다.
	
	// 생성자
	public TreeNode(int key, Object value) {
		itsKey = key;
		itsValue = value;
		System.out.println("Start TreMapNode");
		
	}
	
	// 어느 자식으로 갈지 select (입력 key가 현재 노드의 key보다 작으면 0.. 즉 왼쪽애 or 오른쪽애 선택 ) 
	public int selectSubNode(int key) {
		return (key < itsKey)? 0 : 1 ;
	}
	
	
	// key 검사해서 일치하면 리턴 / 일치하지 않으면 자식노드로 pivot 이동 
	public Object find(int key) {
		// 일치하는 키를 찾으면 리턴!
		if(key == itsKey) 
			return itsValue;

		// 키가 일치 하지 않으면 다시 자식노드 선택해서 검색 (=pivot이동)
		return findSub(selectSubNode(key), key);	
	}
	
	
	public Object findSub(int node, int key) {
		// 해당하는 위치에 자식 노드가 없으면 null을 리턴, 해당하는 위치에 자식노드 있으면  find함수 실행
		return nodes[node] == null? null : nodes[node].find(key);
	}
	
	
	// 추가 : key값에 따라 마지막 레벨에 추가.
	public void add(int key, Object value) {

		// key가 현재노드의 key와 일치하면 value갱신  (ex.topNode.add첫 실행 시, key가 topNode의 key와 일치하면 , topNode value갱신)
		if(key == itsKey) 
			itsValue = value;
		
		else 
			SubNode(selectSubNode(key), key, value);
		// case1. SubNode( 0 , key, value) : 새로운 키가 더 작은 경우 (새로 들어올 key가 topNode의 key보다 작다) - 왼쪽
		// case2. SubNode( 1 , key, value) : 새로운 키가 더 큰 경우 (새로 들어올 key가 topNode의 key보다 크다) - 오른쪽
	}

	
	private void SubNode(int node, int key, Object value) {
		// 해당 위치에 아직 node가 없는 경우 -> 그 위치에 새로운 노드 생성. add 로직이 완료!
		if(nodes[node]==null) 
			nodes[node] = new TreeNode(key, value);
		
		// 해당 위치에 이미 node가 있는 경우 -> 해당 노드 위치를 시작으로 add로직 수행. (즉, topNode가 아니라 topNode의 자식 중 하나의 노드가 기준이 됨. pivot 이동) 
		// itsKey가 topNode의 Key에서 그 자식노드의 Key가 되겠지? 
		else
			nodes[node].add(key, value);
		
	}
	
}
