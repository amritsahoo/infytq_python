package com;
import java.util.Scanner;
public class Assignment1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the first number");
int num1=sc.nextInt();
System.out.println("Enter the second number");
int num2=sc.nextInt();
int res;
if(num1==num2) {
	res=num1+num2;
}
else {
	res=2*(num1+num2);
}
System.out.println(res);
	}

}
