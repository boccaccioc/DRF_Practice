# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout, authenticate
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


from .models import Account
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from .serializers import RegistrationSerializer, AccountSerializer


# creates an account given an account instance
@api_view(['POST'])
def accountCreate(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successfully registered a new user."
        data['username'] = account.username
        data['email'] = account.email
    else:
        data = serializer.errors
    return Response(data)


# returns all accounts in the database from the get request
@api_view(['GET'])
def accountList(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


# returns one account from the database through a get request and an account username
@api_view(['GET'])
def accountDetail(request, username):
    account = get_object_or_404(Account,username = username)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)


# returns one updated account from the database through a put request that takes in an account username and an account instance
@api_view(['PUT'])
def accountUpdate(request, username):
    account = get_object_or_404(Account,username = username)
    serializer = AccountSerializer(instance=account,data=request.data)

    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


# deletes an account from an account username from the database
@api_view(['DELETE'])
def accountDelete(request,username):
    account = get_object_or_404(Account,username = username)
    account.delete()
    return Response("Account deleted")


# logs account out through get request
@api_view(['GET'])
def log_out(request):
    logout(request)
    return Response("Logout Successful")


#Example request
# {
# "username" : "testaccount",
# "password" : "test",
# "firstName" : "Test",
# "lastName" : "Account"
# }
# creates user account and authentication token for future logins and logs the user into the website
@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successfully registered a new user."
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)




# from todos import models
# from .serializers import TodoSerializer

# class ListTodo(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer
#
#
# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer
#
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer