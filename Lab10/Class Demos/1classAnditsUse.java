
class Account {  
	int balance;  

	public Account (int init) {balance=init;}  
	public void deposit (int i) { balance=balance+i;}  
	public void withdraw (int i) {balance=balance-i;}  
	public int bal() {return balance;}  

}


class Operations {

	public static void main(String args[]) {  

		Account n = new Account (10);  
		n.withdraw(5);  
		System.out.println(n.bal());  
	}

}  
