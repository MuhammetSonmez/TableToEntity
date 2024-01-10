import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="MyDatabase"
)

cursor = conn.cursor()

def getTableNames():
    cursor.execute("SHOW TABLES")
    tables_tuple= cursor.fetchall()

    tables = []
    for table in tables_tuple:
        tables.append(table[0])

    return tables

def getDataFromTable(table):
    cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
    cols = cursor.fetchall()
	
    return cols

def addGetter(dataType, varName):
    getter = "\n\t"
    getter += "public " + dataType + " get"+varName[0].upper() + varName[1:-1] + "() { \n" + "\t\treturn " + varName[0:-1] +";\n" + "\t}\n\n" 
	
    return getter


def addSetter(dataType, varName):
    setter = "\n\t"
    setter += "public void set" + varName[0].upper() + varName[1:-1] + "("+dataType + " " + varName[:-1] + "){\n"+"\t\tthis." + varName[:-1] + " = " + varName[:-1] + ";\n\t}\n"

    return setter

def addConstructor(dataTypes, varNames, name):
    #print(name, dataTypes, varNames)
    constructor = "\n\t"
    head = "public " + name[0].upper() + name[1:] + "("
    body = ""
	
    for i in range(len(dataTypes)):
        head += dataTypes[i] + " "+ varNames[i] +", "
	    
    head = head[:-2] + "){\n"


    for i in range(len(varNames)):
        body += "\tthis."+varNames[i]+ " = " +varNames[i] + ";\n"
    constructor += head + body + "\n\t}"

    return constructor
    


def addGetterSetter(lines, name):
    output = "\n"
    dataTypes = []
    varNames = []
	
    for var in lines:
        _, dataType, varName = var.split(" ")
        varName = varName.replace(";", "")
        varName = varName[0].lower() + varName[1:]
        
        dataTypes.append(dataType)
        varNames.append(varName.replace("\n",""))
        output += addGetter(dataType, varName)
        output += addSetter(dataType, varName)


    #print(dataTypes, varNames, name)
    output += addConstructor(dataTypes, varNames, name)
    
    return output

"""
//example:        
	private int customer_id;
	
    public Customers(int customer_id, String first_name, String email, String last_name) {
		this.customer_id = customer_id;
		this.first_name = first_name;
		this.email = email;
		this.last_name = last_name;
	}

	public int getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id;
    }
"""

def dataParser(data, name):
    output = "public class "+ name[0].upper() + name[1:]+"{\n"
    temp = data
    data = []
    for i in temp:
        if i not in data:
            data.append(i)
    lines = []
    for var, typ in data:
        if typ == "varchar":
            typ = "String"
        elif typ == "decimal":
            typ = "double"
        elif typ == "date":
            typ = "Date"
            if "import java.sql.Date;" not in output:
                output = "import java.sql.Date;\n\n" + output
        
        # elif ...        

        output += "\n\tprivate " + typ +" " + var + ";\n"
        lines.append("\tprivate " + typ +" " + var + ";\n")
        
                               
    #addGetterSetter(lines)
    output += addGetterSetter(lines, name)
    output += "\n}"
    return output


def createJavaClass():
    tables = getTableNames()
    for table in tables:
        with open(fr"output\{table[0].upper() + table[1:]}.java", "w", encoding="utf-8") as f:
            f.write(dataParser(getDataFromTable(table), table))
            f.close()
#dataParser(getDataFromTable(getTableNames()[2]))

createJavaClass()

conn.close()
