package com;

import java.util.Scanner;

public class Assignment2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the first number");
		int a=sc.nextInt();
		System.out.println("Enter the second number");
		int b=sc.nextInt();
		System.out.println("Enter the third number");
		int c=sc.nextInt();
		double root1=0,root2=0;
		double discriminant=Math.pow(b,2)-(4*a*c);
		if(discriminant==0.0){
		    root1=-b/(2*a);
		    System.out.println("The root is "+root1);
		}
		else if(discriminant>0.0){
		    root1=(-b+discriminant)/(2*a);
		    root2=(-b-discriminant)/(2*a);
		    System.out.println("The roots are "+root1+","+root2);
		}
		else{
		    System.out.println("The equation has no real roots");
		}
	}
	}




