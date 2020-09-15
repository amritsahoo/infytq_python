package com;
import java.util.Scanner;
public class IterAssignment5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number");
int num=sc.nextInt();
int count=0;
int temp=num;
while(temp>0){
	temp/=10;
	count++;
}
int sum=0;
temp=num;
while(temp>0) {
	int mod=temp%10;
	sum+=(int)Math.pow(mod, count);
	temp/=10;
}
if(sum==num) {
	System.out.println(num+" is an Armstrong number");
}
else {
	System.out.println(num+" is not an Armstrong number");
}
	}

}
