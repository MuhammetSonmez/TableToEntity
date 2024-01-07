class Customers{

	private int customer_id;

	private String email;

	private String first_name;

	private String last_name;


	public int getCustomer_id() { 
		return customer_id;
	}


	public void setCustomer_id(int customer_id){
		this.customer_id = customer_id;
	}

	public String getEmail() { 
		return email;
	}


	public void setEmail(String email){
		this.email = email;
	}

	public String getFirst_name() { 
		return first_name;
	}


	public void setFirst_name(String first_name){
		this.first_name = first_name;
	}

	public String getLast_name() { 
		return last_name;
	}


	public void setLast_name(String last_name){
		this.last_name = last_name;
	}

	public Customers(int customer_id, String email, String first_name, String last_name){	this.customer_id = customer_id;
	this.email = email;
	this.first_name = first_name;
	this.last_name = last_name;

	}
}