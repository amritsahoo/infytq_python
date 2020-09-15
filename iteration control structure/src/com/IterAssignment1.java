package com;
import java.util.Scanner;
public class IterAssignment1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number:");
int num=sc.nextInt();
int tempnum=num;
int rev=0;
while(tempnum>0) {
	int mod=tempnum%10;
	rev=rev*10+mod;
	tempnum/=10;
}
if(num==rev) {
	System.out.println(num+" is a pallindrome number");
}
else {
	System.out.println(num+" is not a pallindrome number");
}
	}

}
