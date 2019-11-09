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

from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter

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
    data = json.dumps({'items':serializer.data}, ensure_ascii = False)
    return HttpResponse(data)


def getAllProducts(request):
    products = []
    Items = Item.objects.all()
    for i in Items.values():        # 각 상품들을 
        product = dict()
        product['name'] = i['name']
        comment = []
        Post_qs = Post.objects.filter(tags__icontains=product['name'])
        # print(Post_qs.values())
        for j in Post_qs.values():      ## 상품명이 태그로 들어간 글들에서
            Comment_qs = Comment.objects.filter(postID=j['id']).order_by('-likes')  # 좋아요순으로
            for k in Comment_qs.values():  ## 각 댓글들을
                this_comment = dict()
                this_comment['content'] = k['content']
                this_comment['likes'] = k['likes']
                this_comment['postID'] = j['id']
                comment.append(this_comment)
        product['comment'] = comment
        products.append(product)
    # print(products)
    # Post_qs = Post.objects.filter(tags__icontains="지갑")
    # Comment_qs = Comment.objects.filter(postID=Post_qs) #??

    # serializer = ItemSerializer( Items, many=True )
    data = json.dumps(products, ensure_ascii = False) #{'items':serializer.data}
    return HttpResponse(data)

@csrf_exempt
def recommend(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Items = Item.objects.all()
        weights = []
        for product in Items.values():
            this_product = dict()
            this_value = 0
            this_value += product[data['forWhat']]
            this_value += product[data['sex']]
            this_value += product['age' + str(data['age'])]
            this_value += product[data['job']]
            for favor in data['favor']:
                this_value += product[favor]
            this_product['id'] = product['id']
            this_product['weight'] = this_value/(4 + len(data['favor']))
            weights.append(this_product)
        # print(weights)
        
        ranked_product = sorted(weights, key=itemgetter('weight', 'id'), reverse=True)[:3]
        products = []
        for i in ranked_product:
            product_object = Item.objects.filter(pk=i['id']).values()[0]
            product = dict()
            product['name'] = product_object['name']
            product['desc'] = product_object['desc']
            comment = []
            Post_qs = Post.objects.filter(tags__icontains=product['name'])
            for j in Post_qs.values():      ## 상품명이 태그로 들어간 글들에서
                Comment_qs = Comment.objects.filter(postID=j['id']).order_by('-likes')  # 좋아요순으로
                for k in Comment_qs.values():  ## 각 댓글들을
                    this_comment = dict()
                    this_comment['content'] = k['content']
                    this_comment['likes'] = k['likes']
                    this_comment['postID'] = j['id']
                    comment.append(this_comment)
            product['comment'] = comment
            product['weight'] = round(i['weight'],2)
            products.append(product)
        data = json.dumps(products, ensure_ascii = False)
        return HttpResponse(data)
    else:
        return HttpResponse("not post")