from rest_framework import serializers

from .models import Users
'''
    Serializer for User model
'''

class User_Serializer(serializers.ModelSerializer) :
    class Meta :
        model = Users
        fields = '__all__'

