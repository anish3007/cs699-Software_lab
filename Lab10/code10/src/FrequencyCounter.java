import java.util.TreeMap;
import java.util.Scanner;
import java.io.*;
import java.util.Map;
import java.util.Iterator;
import java.util.Set;

public class FrequencyCounter {
private TreeMap<String,Integer> tm=new TreeMap<String,Integer>();
	
	void build (String filename){
		File f=new File (filename);
		try{
			Scanner s=new Scanner(f);
			String str = "";
			while(s.hasNext()){
				str=s.next();
				str=cleanString(str);
				str=changeToLower(str);
				buildMap(str);
				//System.out.println(str);
			}
			s.close();
		}
		catch(FileNotFoundException e){
			System.out.println("file not found");
			e.printStackTrace();
		}
	}
	private void buildMap(String str){
		if(tm.containsKey(str)){
			int i=tm.get(str);
			tm.put(str, ++i);
		}
		else
			tm.put(str, 1);
			
	}
	private String cleanString(String str){
		return (str.replaceAll("[0-9?!();:.,]", ""));
	}
	private String changeToLower(String str){
		StringBuilder sb=new StringBuilder();
		for(int i=0;i<str.length();i++){
			char c=str.charAt(i);
			if(Character.isUpperCase(c)){
				sb.append(Character.toLowerCase(c));
			}
			else
				sb.append(c);
		}
		return (sb.toString());
	}
	void dump (){
		Set set=tm.entrySet();
		Iterator itr=set.iterator();
		try{
			//File outF=new File("sampleOutputQ1");
			//FileWriter fw=new FileWriter(outF);
			//PrintWriter pw=new PrintWriter(fw);
			while(itr.hasNext()){
				Map.Entry mentry=(Map.Entry)itr.next();
				System.out.println(mentry.getKey()+"  "+mentry.getValue());
	
			//	pw.println(mentry.getKey()+" "+mentry.getValue());
				
			}
			//pw.close();
		}
		catch(Exception e){
			e.printStackTrace();
		}
		
	}


}
