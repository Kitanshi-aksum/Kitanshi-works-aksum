import frappe

def execute(filters=None):
    try:
        print("Executing the 'execute' function...")
        # Call the 'get_data' function to fetch purchase and sales data
        purchase_data, sales_data = get_data(filters)
        print("Fetched purchase and sales data.")

        # Initialize an empty list to store the merged data
        merged_data = []
        print("Initializing 'merged_data' list.")

        # Iterate through the purchase and sales data
        for purchase_record in purchase_data:
            for sales_record in sales_data:
                # Check if the 'purchase_custom_sales_invoice' from purchase matches the 'sales_name' from sales
                if purchase_record["purchase_custom_sales_invoice"] == sales_record["sales_name"]:
                    # Merge the purchase and sales records into a single dictionary
                    merged_record = {**purchase_record, **sales_record}
                    # Append the merged record to the 'merged_data' list
                    merged_data.append(merged_record)
        print("Merged purchase and sales data.")

        # Call 'get_columns' function to define the report columns
        columns = get_columns()
        print("Retrieved column definitions.")

        # Call 'format_data' function to format the merged data based on the report columns
        data = format_data(merged_data, columns)
        print("Formatted merged data.")

        # Return the columns and formatted data as the result of the 'execute' function
        print("Returning columns and formatted data.")
        return columns, data

    # Handle exceptions and display an error message if any exception occurs
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        frappe.msgprint(f"An error occurred: {str(e)}")

def get_data(filters):
    # Fetch data from Purchase Register
    purchase_data = frappe.get_all(
        "Purchase Invoice",
        filters={"docstatus": 1},
        fields=[
            "name as purchase_name",
            "posting_date as purchase_posting_date",
            "credit_to as purchase_credit_to",
            "supplier_name as purchase_supplier_name",
            "tax_id as purchase_tax_id",
            "bill_no as purchase_bill_no",
            "bill_date as purchase_bill_date",
            "custom_sales_invoice as purchase_custom_sales_invoice",
            "project as purchase_project",
            "owner as purchase_owner",
            "remarks as purchase_remarks",
        ]
    )

    # Fetch data from Sales Register
    sales_data = frappe.get_all(
        "Sales Invoice",
        filters={"docstatus": 1},
        fields=[
            "name as sales_name",
            "posting_date as sales_posting_date",
            "debit_to as sales_debit_to",
            "project as sales_project",
            "customer_name as sales_customer_name",
            "owner as sales_owner",
            "remarks as sales_remarks",
            "territory as sales_territory",
            "tax_id as sales_tax_id",
            "customer_group as sales_customer_group",
            "base_net_total as sales_base_net_total",
            "base_grand_total as sales_base_grand_total",
            "base_rounded_total as sales_base_rounded_total",
            "outstanding_amount as sales_outstanding_amount",
            "is_internal_customer as sales_is_internal_customer",
            "represents_company as sales_represents_company",
            "company as sales_company",
        ]
    )

    return purchase_data, sales_data

def get_columns():
    # Define the columns for your report
    columns = [
        {
            "label": "Purchase Name",
            "fieldname": "purchase_name",
            "fieldtype": "Link",
            "options": "Purchase Invoice",
            "width": 100
        },
        {
            "label": "Sales Name",
            "fieldname": "sales_name",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 100
        },
        {
            "label": "Customer Name",
            "fieldname": "sales_customer_name",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Customer Group",
            "fieldname": "sales_customer_group",
            "fieldtype": "Link",
            "options": "Customer Group",
            "width": 100
        },
        {
            "label": "Owner",
            "fieldname": "sales_owner",
            "fieldtype": "Link",
            "options": "User",
            "width": 100
        },
        {
            "label": "Remarks",
            "fieldname": "sales_remarks",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Territory",
            "fieldname": "sales_territory",
            "fieldtype": "Link",
            "options": "Territory",
            "width": 100
        },
        {
            "label": "Tax ID",
            "fieldname": "sales_tax_id",
            "fieldtype": "Data",
            "width": 100
        },
        
        # {
		# 	"label": "Sales Delivery Note",
		# 	"fieldname": "Sales_delivery_note",
		# 	"fieldtype": "Link",
		# 	"options": "Delivery Note",
		# 	"width": 100,
		# },
		{
			"label": "Cost Center",
			"fieldname": "cost_center",
			"fieldtype": "Link",
			"options": "Cost Center",
			"width": 100,
		},
		{
			"label": "Warehouse",
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"width": 100,
		},
		{
			"label": "Mode Of Payment",
			"fieldname": "mode_of_payment",
			"fieldtype": "Data",
			"width": 120,
		},
        {
            "label": "Base Net Total",
            "fieldname": "sales_base_net_total",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 100
        },
        {
            "label": "Base Grand Total",
            "fieldname": "sales_base_grand_total",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 100
        },
        {
            "label": "Base Rounded Total",
            "fieldname": "sales_base_rounded_total",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 100
        },
        {
            "label": "Outstanding Amount",
            "fieldname": "sales_outstanding_amount",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 100
        },
        {
            "label": "Is Internal Customer",
            "fieldname": "sales_is_internal_customer",
            "fieldtype": "Check",
            "width": 100
        },
        {
            "label": "Represents Company",
            "fieldname": "sales_represents_company",
            "fieldtype": "Link",
            "options": "Company",
            "width": 100
        },
        {
            "label": "Company",
            "fieldname": "sales_company",
            "fieldtype": "Link",
            "options": "Company",
            "width": 100
        },
        {
            "label": "Purchase Credit To",
            "fieldname": "purchase_credit_to",
            "fieldtype": "Link",
            "options": "Account",
            "width": 100
        },
        {
            "label": "Sales Receievable Account",
            "fieldname": "sales_debit_to",
            "fieldtype": "Link",
            "options": "Account",
            "width": 100
        },
        {
            "label": "Purchase Supplier",
            "fieldname": "purchase_supplier",
            "fieldtype": "Link",
            "options": "Supplier",
            "width": 100
        },
        {
            "label": "Purchase Supplier Name",
            "fieldname": "purchase_supplier_name",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Tax ID",
            "fieldname": "purchase_tax_id",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Bill No",
            "fieldname": "purchase_bill_no",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Bill Date",
            "fieldname": "purchase_bill_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": "Purchase Custom Sales Invoice",
            "fieldname": "purchase_custom_sales_invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 100
        },
        {
            "label": "Customer Group",
            "fieldname": "purchase_customer_group",
            "fieldtype": "Link",
            "options": "Customer Group",
            "width": 100
        },
        {
            "label": "Tax ID",
            "fieldname": "purchase_tax_id",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Project",
            "fieldname": "purchase_project",
            "fieldtype": "Link",
            "options": "Project",
            "width": 100
        },
        {
            "label": "Owner",
            "fieldname": "purchase_owner",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Remarks",
            "fieldname": "purchase_remarks",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Currency",
            "fieldname": "currency",
            "fieldtype": "Data",
            "width": 80
        },
    ]

    return columns

def format_data(data, columns):
    formatted_data = []

    for record in data:
        formatted_record = {}
        for col in columns:
            formatted_record[col["fieldname"]] = record.get(col["fieldname"], "")
        formatted_data.append(formatted_record)

    return formatted_data
