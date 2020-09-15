package com;
import java.util.Scanner;
public class IterAssignment6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number");
int num = sc.nextInt();
int rev=0;
int temp=num;
while(temp>0) {
	int mod=temp%10;
	rev=rev*10+mod;
	temp/=10;
}
int count=0;
temp=rev;
int sum=0;
while(temp>0){
	int mod=temp%10;
	count++;
	if(count%2==0) {
		sum+=(int)Math.pow(mod, 2);
	}
	temp/=10;
}
if(sum%9==0) {
	System.out.println("The number "+num+" is a lucky number");
}
else {
	System.out.println("The number "+num+" is not a lucky number");
}
	}

}
