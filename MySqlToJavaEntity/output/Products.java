class Products{

	private double price;

	private int product_id;

	private String product_name;


	public double getPrice() { 
		return price;
	}


	public void setPrice(double price){
		this.price = price;
	}

	public int getProduct_id() { 
		return product_id;
	}


	public void setProduct_id(int product_id){
		this.product_id = product_id;
	}

	public String getProduct_name() { 
		return product_name;
	}


	public void setProduct_name(String product_name){
		this.product_name = product_name;
	}

	public Products(double price, int product_id, String product_name){
	this.price = price;
	this.product_id = product_id;
	this.product_name = product_name;

	}
}