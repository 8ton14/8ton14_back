from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from community.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class ItemSerializer(serializers.Serializer):
#     class Meta:
#         model = Item
#         fields = ['name', 'desc', 'common_price']


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    desc = serializers.CharField(max_length=100)
    common_price = serializers.IntegerField(default=0)


class PostSerializer(serializers.Serializer):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(default="")
    tags = models.CharField(max_length=100, default="")



class ItemSerializer(serializers.Serializer):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    content = models.TextField(default="")
    likes = models.IntegerField(default=0)