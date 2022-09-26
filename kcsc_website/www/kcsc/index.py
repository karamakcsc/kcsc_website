import frappe

def get_context(context):
	#Banners Loop
	customer = frappe.db.sql(""" SELECT name, customer_name, image
						   FROM `tabCustomer` WHERE publish = 1 ORDER BY creation DESC;""", as_dict=True)
	context.customer = customer

	#Blogs Loop
	# blog = frappe.db.sql(""" SELECT name, creation, title, blog_intro, published, published_on, meta_image, content
	# 					   FROM `tabBlog Post`  WHERE published =1 ORDER BY creation DESC LIMIT 3;""", as_dict=True)
	# context.blog = blog




	return context
