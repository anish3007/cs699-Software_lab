import java.util.Scanner;
import java.io.*;


class TestScanner {


 public static void main (String [] args) {
   Scanner s = new Scanner(System.in);

   int i=  s.nextInt ();
   String str = s.next();
   float f = s.nextFloat();
   String l = s.nextLine();
  
   System.out.println(i);
   System.out.println(str);
   System.out.println(f);
   System.out.println(l);
  
   s.close();


 }

}
