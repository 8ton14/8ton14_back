from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from community.models import *

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    # queryset = Comment.objects.all()
    serializer_class = ItemSerializer


class SettingAPIView(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, username):
        user=get_object_or_404(MyUser, username=username)
        content = {'user': user.username, 'greeting': "안녕"}
        return Response(content)



def getRecommendTest(request):
    Items = Item.objects.all()
    serializer = ItemSerializer( Items, many=True )
    print("##", serializer.data)
    data = json.dumps({'items':serializer.data}, ensure_ascii = False)
    return HttpResponse(data)