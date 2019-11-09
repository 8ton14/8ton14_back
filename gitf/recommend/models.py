from django.db import models
from django.conf import settings

def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s.%s' % (pid, extension) # 예 : wayhome/abcdefgs.png

# Create your models here.
class Item(models.Model):
    image = models.ImageField(upload_to = user_path, default="")
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    common_price = models.IntegerField(default=0)
    
    # 추천 가중치

    # 목적
    birthday = models.FloatField(default=0.0)
    anniversary = models.FloatField(default=0.0)
    houses = models.FloatField(default=0.0)
    celebrate = models.FloatField(default=0.0)
    general = models.FloatField(default=0.0)

    # 성별
    male = models.FloatField(default=0.0)
    female = models.FloatField(default=0.0)
    # 나이대
    age10 = models.FloatField(default=0.0)
    age20 = models.FloatField(default=0.0)
    age30 = models.FloatField(default=0.0)
    age40 = models.FloatField(default=0.0)
    age50older = models.FloatField(default=0.0)
    
    # 직업
    teenager = models.FloatField(default=0.0)
    university_student = models.FloatField(default=0.0)
    worker = models.FloatField(default=0.0)
    jobless = models.FloatField(default=0.0)

    # 관심사
    exercise = models.FloatField(default=0.0)
    healthcare = models.FloatField(default=0.0)
    beauty = models.FloatField(default=0.0)
    game = models.FloatField(default=0.0)
    it = models.FloatField(default=0.0)
    fashion = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
