from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username','password']
        extra_kwargs = { 'password': {'write_only':True}}

    def save(self):
        account = Account(username=self.validated_data['username'])
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account




# from todos import models
#
#
# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'description',
#         )
#         model = models.Todo