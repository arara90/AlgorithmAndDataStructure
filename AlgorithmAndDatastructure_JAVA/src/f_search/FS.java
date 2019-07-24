// https://www.youtube.com/watch?v=_hxFgg7TLZQ
// 따라해보기 
package f_search;
import java.util.LinkedList;
import java.util.Iterator;
import java.util.Stack;
import f_search.Queue;
import java.util.NoSuchElementException;

class Graph{
	
	
	class Node{
		int data;
		LinkedList<Node> adjacent;
		boolean marked;
		
		Node(int data){
			this.data = data;
			this.marked = false;
			adjacent = new LinkedList<Node>();
		}
	}
	
		
	Node[] nodes;
	
	//생성자
	Graph(int size){	
		nodes = new Node[size];
		for(int i =0; i<size; i++) {
			nodes[i] = new Node(i);
		}	
	}
	
	//관계 저장, param은 index
	void addEgde(int i1, int i2) {
		Node n1 = nodes[i1];
		Node n2 = nodes[i2];
		
		if(!n1.adjacent.contains(n2)) {
			n1.adjacent.add(n2);
		}
		
		if(!n2.adjacent.contains(n1)) {
			n2.adjacent.add(n1);
		}
		
	}
	
	
	// node의 데이터 출력
	void visit(Node n) {
		System.out.print(n.data + " ");
	}
	
	
	
//////////////////// 1. dfs - stack ///////////////////////////
	void dfs() {
		dfs(0);
	}
	
	// param은 시작하는 노드의 인덱스 번호
	void dfs(int index) {
		Node root = nodes[index];
		Stack<Node> stack = new Stack<Node>();
		stack.push(root);
		root.marked = true;
		
		while(!stack.isEmpty()) {
			// 1. stack에서 출력
			Node r = stack.pop();
			
			// 2. 꺼낸 아이와 연결된 노드들을 stack에 넣기
			for(Node n:r.adjacent) {
				if(n.marked==false) {
					n.marked= true;
					stack.push(n);
				}
			}
			
		
			// 3. 꺼낸 아이의 data 출력
		visit(r);
		
		} //while(!stack.isEmpty()) end		
	}
	
	
//////////////////// 2. dfsR - dfs recursive ///////////////////////////	
	void dfsR(Node r) {
		
		// 노드가 비어있으면 종료
		if(r==null) return;
		r.marked = true;
		
		//1. 출력
		visit(r);
		
		//2. 연결된 노드들 방문
		for(Node n:r.adjacent) {
			if(n.marked==false) {
				dfsR(n);
			}
		}
	}
	
	//시작 다양하게 하기 위해
	void dfsR(int index) {
		Node r = nodes[index];
		dfsR(r);
	}
	
	void dfsR() {
		dfsR(0);
	}
	
	
//////////////////// 3. bfs ///////////////////////////
	void bfs() {
		bfs(0);
	}
	
	
	void bfs(int index) {
		Node root = nodes[index];
		Queue<Node> queue = new Queue<Node>();
		queue.enqueue(root);
		root.marked = true;
		
		while(!queue.isEmpty()) {
			Node r = queue.dequeue();
			for(Node n: r.adjacent) {
				if(n.marked == false) {
					n.marked = true;
					queue.enqueue(n);
				}
			}
			visit(r);
		}
	
	}
	
}


//////////////////// Test ///////////////////////////

public class FS {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		/*
		   0
		  /
	 	 1 -- 3    7
	 	 |   /|\  /
	 	 | /  | 5
	 	 2 -- 4  \
	 	 		  6 - 8
		 */
		
//		Graph g = new Graph(9);
//		g.addEgde(0, 1);
//		g.addEgde(1, 2);
//		g.addEgde(1, 3);
//		g.addEgde(2, 4);
//		g.addEgde(2, 3);
//		g.addEgde(3, 4);
//		g.addEgde(3, 5);
//		g.addEgde(5, 6);
//		g.addEgde(5, 7);
//		g.addEgde(6, 8);
//		
//		//g.dfs();	// 0 1 3 5 7 6 8 4 2 
//		//g.dfsR();	//0 1 2 4 3 5 6 8 7 
//		//g.bfs();	// 0 1 2 3 4 5 6 7 8 
//		
//		//g.dfs(3);	// 3 5 7 6 8 4 2 1 0 
//		//g.dfsR(3);	//3 1 0 2 4 5 6 8 7 
//		g.bfs(3);	//3 1 2 4 5 0 6 7 8 
		
		
		
		Graph g = new Graph(5);
		g.addEgde(1, 2);
		g.addEgde(1, 3);
		g.addEgde(1, 4);
		g.addEgde(2, 4);
		g.addEgde(3, 4);

		
		//g.dfs(1);	//1 4 3 2 
		g.dfsR(1); //1 2 4 3 
		
	}

}
