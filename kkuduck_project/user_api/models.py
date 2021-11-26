from django.db import models
from django.db.models.expressions import F

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(
        help_text="user ID", 
        null=False,
        primary_key=True)
    user_name = models.CharField(max_length=128, null=False)
    # address = models.CharField(max_length=256, null=True)
    class Meta:
        db_table = 'User' # database 안에 이제 user란 테이블을 만들거야.

class Subscription(models.Model):
    service_name = models.CharField(max_length=256, null=False) # 새로 추가한 구독서비스이름
    plan_name = models.CharField(max_length=128, null=False)
    plan_price = models.CharField(max_length=128, null=False)
    cycle = models.CharField(max_length=128, null=False)
    head_count = models.IntegerField(default=1, null=False) # 새로 추가한 사용인원
    start_date = models.DateTimeField(max_length=128, null=False)
    service_id = models.CharField(max_length=128, null=True)  # 구독서비스아이디 여러개 만들어서 하시는 분
    end_date = models.DateTimeField(null=True)
    share_id = models.CharField(max_length=128, null=True) # 구독한 서비스의 ID, 꾸덕id 아님 주의
    image_id = models.CharField(max_length=1024, null=True)

    # User 클래스의 user_id를 가져와서 쓸거야
    user_id = models.ForeignKey(User,max_length=128, null=False,on_delete=models.CASCADE, db_column="user_id_hee")
    class Meta:
        db_table = 'Subscription'

class DefaultSubscription(models.Model):
    service_name = models.CharField(primary_key=True, max_length=128)
    # plans = models.AutoField(max_length=128, null=False) #primary_key 추가함
    image_id = models.CharField(null=True, max_length=128)
    class Meta:
        db_table = 'DefaultSubscription'

class Plan(models.Model):
    plan_name = models.CharField(null=False,max_length=128)
    plan_price = models.IntegerField(null=False)
    cycle = models.CharField(max_length=64, null=False)

    # DefaultSubscription의 service_name을 가져와서 쓸거야 
    default_sub_id = models.ForeignKey(DefaultSubscription, max_length=128, null=False, on_delete=models.CASCADE, db_column='default_sub_id')
    class Meta:
        db_table = 'Plan'
    

 



