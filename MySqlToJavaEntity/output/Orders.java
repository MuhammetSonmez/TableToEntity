import java.sql.Date;

public class Orders{

	private int customer_id;

	private Date order_date;

	private int order_id;

	private double total_amount;


	public int getCustomer_id() { 
		return customer_id;
	}


	public void setCustomer_id(int customer_id){
		this.customer_id = customer_id;
	}

	public Date getOrder_date() { 
		return order_date;
	}


	public void setOrder_date(Date order_date){
		this.order_date = order_date;
	}

	public int getOrder_id() { 
		return order_id;
	}


	public void setOrder_id(int order_id){
		this.order_id = order_id;
	}

	public double getTotal_amount() { 
		return total_amount;
	}


	public void setTotal_amount(double total_amount){
		this.total_amount = total_amount;
	}

	public Orders(int customer_id, Date order_date, int order_id, double total_amount){
	this.customer_id = customer_id;
	this.order_date = order_date;
	this.order_id = order_id;
	this.total_amount = total_amount;

	}
}