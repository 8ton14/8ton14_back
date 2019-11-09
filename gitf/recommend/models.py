from django.db import models

# Create your models here.
class Item(models.Model):
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
