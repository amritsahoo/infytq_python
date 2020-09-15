package com;
import java.util.Scanner; 
public class Exercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter a positive integer");
int count=sc.nextInt();
int num=1;
while(count>1) {
	System.out.print(num+",");
	num*=2;
	count--;
}
System.out.print(num);
	}

}
