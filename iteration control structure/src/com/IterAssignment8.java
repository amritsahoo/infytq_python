package com;
import java.util.Scanner;
public class IterAssignment8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int num=sc.nextInt();
for(int i=1;i<=num;i++) {
	for (int j=1;j<=(6-i);j++) {
		System.out.print("*");
	}
	System.out.println();
}
	}

}
