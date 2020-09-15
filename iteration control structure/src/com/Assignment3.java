package com;
import java.util.Scanner;
public class Assignment3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc= new Scanner(System.in);
System.out.println("Enter the first number");
int num1=sc.nextInt();
System.out.println("Enter the second number");
int num2=sc.nextInt();
System.out.println("Enter the third number");
int num3=sc.nextInt();
int res;
if(num3==7) {
	res=-1;
}
else if(num2==7) {
	res=num3;
}
else if(num1==7) {
	res=num2*num3;
}
else {
	res=num1*num2*num3;
}
System.out.println(res);

	}

}
