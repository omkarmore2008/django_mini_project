from django.db import models

 
# Create your models here.
'''
   product model to store related data of products
  
   Fields:
       product id
               name
               description
               price
               image
 
'''
class Products(models.Model) :
 
   product_id = models.IntegerField(primary_key = True, null = False)
   product_name = models.CharField(max_length = 20)
   product_description = models.CharField(max_length = 150)
   product_price = models.FloatField()
   product_image = models.ImageField(upload_to='images/')
 
   def __str__(self) :
       return f'{self.product_id} {self.product_name} {self.product_description} {self.product_price} {self.product_image}'
 

