package assignment2;

public class Resturant {
private String resturantName;
private long resturantContact;
private String resturantAddress;
private float rating;
public Resturant(String resturantName, long resturantContact, String resturantAddress, float rating) {
	this.resturantName=resturantName;
	this.resturantContact=resturantContact;
	this.resturantAddress=resturantAddress;
	this.rating=rating;
}
public String getResturantName() {
	return resturantName;
}
public void setResturantName(String resturantName) {
	this.resturantName = resturantName;
}
public long getResturantContact() {
	return resturantContact;
}
public void setResturantContact(long resturantContact) {
	this.resturantContact = resturantContact;
}
public String getResturantAddress() {
	return resturantAddress;
}
public void setResturantAddress(String resturantAddress) {
	this.resturantAddress = resturantAddress;
}
public float getRating() {
	return rating;
}
public void setRating(float rating) {
	this.rating = rating;
}
public void displayResturantDetails() {
	System.out.println("Resturant Details");
	System.out.println("********************");
	System.out.println("Resturant Name : "+getResturantName());
	System.out.println("Resturant Rating : "+getRating());
	System.out.println("Resturant Contact : "+getResturantContact());
	System.out.println("Resturant Address : "+getResturantAddress());
}
}
