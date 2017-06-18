import java.util.Scanner;
import java.io.*;


class TestScanner {


 public static void main (String args[]) {

   System.out.println(args[0]);
   File f = new File (args[0]);
	
   try {
   	Scanner s = new Scanner(f);
   	int i=  s.nextInt ();
   	String str = s.next();
   	float fl = s.nextFloat();
   	String l = s.nextLine();
  
   	System.out.println(i);
   	System.out.println(str);
   	System.out.println(fl);
   	System.out.println(l);
  
   	s.close();


   }
   catch (FileNotFoundException e) {
	System.out.println("file not found");
   }


 }

}
