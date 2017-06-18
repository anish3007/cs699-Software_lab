import java.util.*;


class LinkedListTest {




 public static void main (String args[]) {


   LinkedList<Integer> l = new LinkedList <Integer> (); 

	l.add(10);
	l.addLast(30);
	l.add(20);
	l.add(1,100);

	for (int i=0; i<l.size(); i++)
		System.out.println (l.get(i));

 }


}
