from rest_framework import serializers

from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')
    

class EntrySerializer(serializers.ModelSerializer):
    # authorのnameとmailの情報を得る為にauthorを上書きする
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
