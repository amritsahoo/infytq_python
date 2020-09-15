package com;
import java.util.Scanner;
public class IterAssignment4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the first number");
int num1=sc.nextInt();
System.out.println("Enter the second number");
int num2=sc.nextInt();
int temp=num1;
int res=num1;
while(temp>0) {
	int mod=temp%10;
	res*=mod;
	temp/=10;
}
if(res==num2) {
	System.out.println(num1+" is a seed of "+num2);
}
else {
	System.out.println(num1+" is not a seed of "+num2);
}
	}

}
