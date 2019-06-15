import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


'''
Parameter
------------------
queryset:Djangoのmodelのクエリセットを指定
         フィタリングも可能
serializer_class:serializerに定義したserializerを指定
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
