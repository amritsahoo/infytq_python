package assignment1;

public class SwiftFood {
private int orderId;
private String orderedFood;
private double totalPrice;
private String status;
public int getOrderId() {
	return orderId;
}
public void setOrderId(int orderId) {
	this.orderId = orderId;
}
public String getOrderedFood() {
	return orderedFood;
}
public void setOrderedFood(String orderedFood) {
	this.orderedFood = orderedFood;
}
public double getTotalPrice() {
	return totalPrice;
}
public void setTotalPrice(double totalPrice) {
	this.totalPrice = totalPrice;
}
public String getStatus() {
	return status;
}
public void setStatus(String status) {
	this.status = status;
}
public double calculateTotalPrice(int unitPrice) {
	totalPrice=unitPrice+unitPrice*0.05;
	return totalPrice;
}
public void display() {
	System.out.println("Order Details");
	System.out.println("===============");
	System.out.println("Order Id : "+getOrderId());
	System.out.println("Ordered Food : "+getOrderedFood());
	System.out.println("Order Status : "+getStatus());
	System.out.println("Total Price : "+getTotalPrice());
}
}
