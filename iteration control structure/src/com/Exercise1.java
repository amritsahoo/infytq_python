package com;
import java.util.Scanner;
public class Exercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number");
int num=sc.nextInt();
if(num<0) {
	System.out.println("Plese enter positive number");
}
else if(num==0) {
	System.out.println("The factorial of 0 is 1");
}
else {
int factorial=1;
for(int i=num; i>=1;i--) {
	factorial*=i;
}
System.out.println("The factorial of "+num+" is "+factorial);
}
	}

}
