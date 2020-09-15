package com;
import java.util.Scanner;
public class IterAssignment3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc =new Scanner(System.in);
System.out.println("Enter the number");
int num= sc.nextInt();
int temp=num;
int sum=0;
while(temp>0) {
	int mod=temp%10;
	sum+=mod;
	temp/=10;
}
if(num%sum==0) {
	System.out.println(num+" is divisible by sum of its digit");
}
else {
	System.out.println(num+" is not divisible by sum of its digit");
}
	}

}
