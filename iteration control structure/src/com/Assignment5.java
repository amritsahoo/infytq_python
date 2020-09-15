package com;
import java.util.Scanner;
public class Assignment5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc=new Scanner(System.in);
System.out.println("Enter your account number");
int accountNumber=sc.nextInt();
System.out.println("Enter your account balance");
long accountBalance=sc.nextLong();
System.out.println("Enter the Salary of Customer");
int salary=sc.nextInt();
System.out.println("Enter the loan type (Car, House, Business)");
String loanType=sc.next();
System.out.println("Expected loan Amount");
long expectedLoanAmount=sc.nextLong();
System.out.println("Expected no of EMIs");
int expectedNoEmi=sc.nextInt();
long eligibleAmount=0;
int noOfEmi=0;
if(accountNumber>=1000 && accountNumber<=1999) {
	if(accountBalance>=1000) {
		if(salary>25000 && salary<=50000) {
			if(loanType=="Car") {
				eligibleAmount=500000;
				noOfEmi=36;
			}
			else {
				System.out.println("You are not eligible for loan");
			}
		}
	else if(salary>50000 && salary<=75000){
		if(loanType=="Car") {
			eligibleAmount=500000l;
			noOfEmi=36;
		}
		else if(loanType=="House") {
			eligibleAmount=6000000l;
			noOfEmi=60;
		}
		else {
			System.out.println("You are not eligible for loan");
		}
	}
	else if(salary>75000) {
		if(loanType=="Car") {
			eligibleAmount=500000l;
			noOfEmi=36;
		}
		else if(loanType=="House") {
			eligibleAmount=6000000l;
			noOfEmi=60;
		}
		else if(loanType=="Business") {
			eligibleAmount=7500000l;
			noOfEmi=84;
		}
		else {
			System.out.println("You are not eligible for loan");
		}
	}
	}
	else {
		System.out.println("SORRY! Account balance is low");
	}
}
else {
	System.out.println("Invalid Account Number");
	
}
if(expectedLoanAmount<=eligibleAmount) {
	if(expectedNoEmi<=noOfEmi) {
		System.out.println(accountNumber);
		System.out.println("You are eligible for Loan");
		System.out.println("eligibleLoanAmount = "+eligibleAmount);
		System.out.println("eligibleEMIs "+noOfEmi);
	}
	else {
		System.out.println("Sorry! You are not eligible for "+expectedNoEmi+" no of EMI");
	}
}
else {
	System.out.println("Sorry! You are not eligible for "+expectedLoanAmount+" loan");
}
	}

}
