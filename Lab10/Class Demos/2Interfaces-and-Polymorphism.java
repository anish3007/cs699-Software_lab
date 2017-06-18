import java.util.Scanner;

interface Account {  
	public boolean deposit (float i);
	public boolean withdraw (float i);
	public float bal();

}

class RupeeAccount implements Account {  
 float balance;
	public RupeeAccount (float i ) {balance=i;}  
	public boolean deposit (float i) { balance=balance+i; return true;}  
	public boolean withdraw (float i) {balance=balance-i; return true;}  
	public float bal() {return balance;}  
}
class DollarAccount implements Account {  
 float balance;
	public DollarAccount (float init) {balance=init;}  
	public boolean deposit (float i) { balance=balance+(float)1.1*i; return true;}  
	public boolean withdraw (float i) {balance=balance-(float)1.1*i; return true;}  
	public float bal() {return balance;}  
}

class Operations {

	public static void main(String args[]) {  

		Account a;

		System.out.println("Choice(1:R   any other:$)?");

		Scanner s = new Scanner (System.in);

		int x = s.nextInt();

		if (x==1) a = new RupeeAccount (10);  
		else a = new DollarAccount(10);

		System.out.println("Choice(1:withdraw 0:deposit 2:Quit)?");
		x = s.nextInt();

		while (x!=2) {

			switch (x) {
				case 1: a.withdraw(2); break;
				case 0: a.deposit(3); break;
			}
			System.out.println(a+" has "+a.bal());

			System.out.println("Choice(1:withdraw 0:deposit 2:Quit)?");
			x = s.nextInt();
		}
	}
}  
