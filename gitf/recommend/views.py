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
import operator

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
            if data['price'][0] <= product['common_price'] <= data['price'][1]:
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
        
        ranked_product = sorted(weights, key=itemgetter('weight', 'id'), reverse=True)[:3]
        products = []
        for i in ranked_product:
            product_object = Item.objects.filter(pk=i['id']).values()[0]
            product = dict()
            product['name'] = product_object['name']
            product['desc'] = product_object['desc']
            product['common_price'] = product_object['common_price']
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



@csrf_exempt
def getPosts(request):
    if request.method == "GET": # 그냥 글 가져오기
        Posts = Post.objects.all()

        result = []
        for post in Posts.values():
            this_post = dict()
            this_post['id'] = post['id']
            this_post['title'] = post['title']
            this_post['content'] = post['content']
            this_post['tags'] = post['tags'].split(',')
            result.append(this_post)
        data = json.dumps(result, ensure_ascii = False)
        return HttpResponse(data)
    elif request.method == "POST": # 태그로 글검색
        tags = json.loads(request.body)['tags']
        Posts = Post.objects.all()

        result = []
        for post in Posts.values():
            this_post = dict()
            this_post['id'] = post['id']
            this_post['title'] = post['title']
            this_post['content'] = post['content']
            this_post['tags'] = post['tags'].split(',')
            this_post['count'] = 0
            for i in tags:
                if i in this_post['tags']:
                    this_post['count'] += 1
            result.append(this_post)
        
        result = sorted(result, key=itemgetter('count', 'id'), reverse=True)
        last = 0
        for i in result:
            if i['count'] == 0:
                break
            else:
                del i['count']
                last += 1
        data = json.dumps(result[:last], ensure_ascii = False)
        return HttpResponse(data)
    else:
        return HttpResponse("에러")


@csrf_exempt
def writePost(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data['title']
        content = data['content']
        tags = ""
        for i in data['tags']:
            tags += i + ','
        
        Post(title=title, content=content, tags=tags[:-1]).save()
        return HttpResponse("OK")
    else:
        return HttpResponse("not Post")


def getTags(request):
    if request.method == "GET":
        Posts = Post.objects.all()

        result = []
        tags = dict()
        for post in Posts.values():
            this_tags = post['tags'].split(',')
            for i in this_tags:
                count = tags.get(i,0)
                tags[i] = count + 1
        
        result = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)
        result = [i[0].strip() for i in result]
        data = json.dumps(result, ensure_ascii = False)
        return HttpResponse(data)
    else:
        return HttpResponse("not GET")
