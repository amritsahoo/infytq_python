package com;
import java.util.Scanner;
public class IterAssignment2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number of heads");
int heads=sc.nextInt();
System.out.println("Enter the number of legs");
int legs=sc.nextInt();
int chickens=0;
int rabbits=0;
if(legs%2==0 && heads<legs) {
	chickens=(int)(2*heads)-legs/2;
	rabbits=(int)(legs-2*heads)/2;
	System.out.println("chickens : "+chickens);
	System.out.println("rabbits : "+rabbits);
}
else {
	System.out.println("The number of chickens and rabbit cannot be found");
}
	}

}
