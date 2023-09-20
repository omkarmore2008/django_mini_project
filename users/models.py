from django.db import models

# Create your models here.
'''
User model to store User Data
   Fields:
       user id
            name
            mail id
            phone number
            password
'''
class Users(models.Model) :
 
   user_id = models.IntegerField(primary_key = True, null = False)
   user_name = models.CharField(max_length = 50)
   user_mail_id = models.CharField(max_length = 32)
   user_phone_number = models.CharField(max_length = 10)
   password = models.CharField(max_length = 16)
 
   def __str__(self) :
       return f'{self.user_id} {self.user_name} {self.user_mail_id} {self.user_phone_number} {self.password}'
 
