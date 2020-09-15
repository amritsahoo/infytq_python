package com;
import java.util.Scanner;
public class IterAssignment7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the first number");
		int firstNumber=sc.nextInt();
		System.out.println("Enter the second number");
		int secondNumber=sc.nextInt();
		int lcm=(firstNumber>secondNumber)?firstNumber:secondNumber;
		while(true){
			if(lcm%firstNumber==0 && lcm%secondNumber==0) {
				System.out.println(lcm);
				break;
			}
			lcm++;
		}

	}

}
