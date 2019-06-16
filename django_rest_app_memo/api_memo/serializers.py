from .models import Memo
from rest_framework import serializers

class MemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memo
        fields = ('id', 'text')
 
