from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Memo
from .serializers import MemoSerializer


class MemoViewSet(viewsets.ModelViewSet):
    '''
    REST用のビューを作成
    '''
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

