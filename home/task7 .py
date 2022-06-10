 from .models import Product


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_descri = models.CharField(max_length=500)


# I. Inserting a new record into the product Model

new_prod = Product('apple laptop',600000, 1, "The latest apple laptop, Silver colour, brand new")
new_prod.save()

# ii. Get all the records in the Product table

get_all_prod = Product.objects.all() #get all records and store them in the variable

get_all_prod  #This prints all the records stored in the varaiable


# iii. Filter products by their name

filter_prod_by_name = Product.objects.filter(product_name__icontains='apple laptop')
filter_prod_by_name #prints the filtered product


# iv. Get a single record from the Product table

get_single_product = Product.object.get(pk = 2)
get_single_product_2 = Product.object.get(id = 2)

# v. Change a product price

#using the new_prod variable used in add a record to the database earlier above
new_prod.product_price =800000
new_prod.save()