package assignment3;

public class Calculator {
public int num1;
public int num2;
public int num3;
public int num4;
public int num5;
public int sum;
public Calculator(int num1, int num2, int num3, int num4, int num5) {
	this.num1=num1;
	this.num2=num2;
	this.num3=num3;
	this.num4=num4;
	this.num5=num5;
}
public int sumOfDigits() {
	sum=num1+num2+num3+num4+num5;
	return sum;
}
	}

