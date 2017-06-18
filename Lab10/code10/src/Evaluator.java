import java.io.*;
import java.util.*;


class CalcExp{
	private String exp=new String();
	private double xval;
	
	CalcExp(){
		exp="";
		xval=0.0;
	}
	CalcExp(String str, double x){
		exp=str;
		xval=x;
	}
	Double evaluateExp(){
		char tok[]=exp.toCharArray();
		Stack<Double> valstk=new Stack<Double>(); 	//Stack for numbers
		Stack<Character> opstk=new Stack<Character>();	//Stack for operators
		int i=0;
		while(i<tok.length){
			//System.out.println(tok[i]);
			if(tok[i]=='x'){
				valstk.push(xval);
				i++;
			}
			else if(tok[i]>='0'&&tok[i]<='9'){
				StringBuffer numbuf=new StringBuffer();
				while(i<tok.length && ((tok[i]>='0'&&tok[i]<='9')||(tok[i]=='.')))
					numbuf.append(tok[i++]);
				valstk.push(Double.parseDouble(numbuf.toString()));
			}
			else if(isOpr(tok[i])){
				while(!opstk.empty() && checkPredMore(opstk.peek(),tok[i])){
					char op=opstk.pop();
					double val2=valstk.pop();
					double val1=valstk.pop();
					double res=applyOperation(op,val1,val2);
					valstk.push(res);
				}
				opstk.push(tok[i++]);
			}
			else{
				System.out.print("Expression not proper");
				break;
			}
		}
		
		while(!opstk.empty()){
			char op=opstk.pop();
			double val2=valstk.pop();
			double val1=valstk.pop();
			double res= applyOperation(op,val1,val2);
			valstk.push(res);
		}
		return valstk.pop();
	}
	double applyOperation(char op, double val1, double val2){
		switch(op){
			case '^': return(Math.pow(val1, val2));
			case '*': return(val1*val2);
			case '/': return(val1/val2);
			case '+': return(val1+val2);
			case '-': return(val1-val2);
			default: return (0.0);
		}
	}
	boolean checkPredMore(char op1, char op2){
		if(op1=='^'&&(op2=='*'||op2=='/'||op2=='+'||op2=='-'))
			return true;
		else if((op1=='*'||op1=='/')&&(op2=='+'||op2=='-'))
			return true;
		else
			return false;
	}
	boolean isOpr(char op){
		if(op=='+'||op=='-'||op=='*'||op=='^'||op=='/')
			return true;
		else
			return false;
	}
}


public class Evaluator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str=args[0];
		double lval=Double.parseDouble(args[1]);
		double rval=Double.parseDouble(args[2]);
		double step=Double.parseDouble(args[3]);
		try{
			//File outF=new File("OutputQ2");
			//FileWriter fwriter=new FileWriter(outF);
			//PrintWriter pw=new PrintWriter(fwriter);
			for(double i=lval;i<=rval;i=i+step){
				CalcExp ce=new CalcExp(str,i);
				double res=ce.evaluateExp();
				//pw.format("%.2f %.2f\n",i,res);
				System.out.format("%.2f %.2f\n",i,res);
			}
			//pw.close();
		}
		catch(Exception e){
			e.printStackTrace();
		}

	}

}
