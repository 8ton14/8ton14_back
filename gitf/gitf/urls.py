# # """gitf URL Configuration

# # The `urlpatterns` list routes URLs to views. For more information please see:
# #     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# # Examples:
# # Function views
# #     1. Add an import:  from my_app import views
# #     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# # Class-based views
# #     1. Add an import:  from other_app.views import Home
# #     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# # Including another URLconf
# #     1. Import the include() function: from django.urls import include, path
# #     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# # """
# # from django.contrib import admin
# # from django.urls import path

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     # url(r'^api-auth/', include('rest_framework.urls')),
# # ]
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
# from recommend.models import Item

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# # Serializers define the API representation.
# class ItemSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Item
#         fields = ['name', 'desc', 'common_price']

# # ViewSets define the view behavior.
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# # router1 = routers.DefaultRouter()
# router.register(r'items', ItemViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from recommend import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'items', views.ItemViewSet)
# router.register(r'test', views.SettingAPIView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('recommend', views.recommendView),
    # path('recommendq', views.recommendQuestion),
    path('test', views.getRecommendTest),
    path('getAllProducts', views.getAllProducts),
    path('api/recommend', views.recommend),
    path('api/getPosts', views.getPosts),
    path('api/getPost', views.getOnePost),
    path('api/writePost', views.writePost),
    path('api/getTags', views.getTags),
    path('api/getComments', views.getCommnets),
    path('api/writeComment', views.writeComment),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
from django.conf import settings
from django.conf.urls.static import static

# 어떤 URL을 정적으로 추가할래? > MEDIA_URL을 static 파일 경로로 추가
# 실제 파일은 어디에 있는데? > MEDIA_ROOT 경로내의 파일을 static 파일로 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
