package com;
import java.util.Scanner;
public class Assignment4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc = new Scanner(System.in);
System.out.println("Enter the type of food(VEG/NONVEG)");
String food=sc.next();
char foodtype=food.charAt(0);
System.out.println("Enter the distance in km");
int distance=sc.nextInt();
System.out.println("Enter the quantity of order");
int noOfOrder=sc.nextInt();
int sum;
if(distance>0) {
	if(foodtype=='V' || foodtype=='N') {
		if(noOfOrder>0) {
			if(foodtype=='V') {
				if(distance>0 && distance<=3) {
					sum=10*noOfOrder;
				}
				else if(distance>3 && distance<=6) {
					sum=10*noOfOrder+distance;
				}
				else {
					sum=10*noOfOrder+3+2*(distance-6);
				}
			}
			else {
				if(distance>0 && distance<=3) {
					sum=15*noOfOrder;
				}
				else if(distance>3 && distance<=6) {
					sum=15*noOfOrder+distance;
				}
				else {
					sum=15*noOfOrder+3+2*(distance-6);
			}
	
			}
		}
		else {
			sum=-1;
		}
	}
	else {
		sum=-1;
	}
}
else {
	sum=-1;
}
System.out.println(sum);
	}

}
