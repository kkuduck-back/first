from django.db import models
from django.db.models.expressions import F

# Create your models here.
class User(models.Model):
    user_id = models.CharField(
        help_text="user ID", 
        max_length=128, null=False,
        primary_key=True)
    user_name = models.CharField(max_length=128, null=False)
    # address = models.CharField(max_length=256, null=True)
    class Meta:
        db_table = 'User' # database 안에 이제 user란 테이블을 만들거야.

class Subscription(models.Model):
    plan_name = models.CharField(max_length=128, null=False)
    plan_price = models.CharField(max_length=128, null=False)
    cycle = models.CharField(max_length=128, null=False)
    start_date = models.DateTimeField(max_length=128, null=False)
    service_id = models.CharField(max_length=128, null=True)
    end_date = models.DateTimeField(max_length=128, null=True)
    image_id = models.CharField(max_length=1024, null=True)

    user_id = models.ForeignKey(User,max_length=128, null=False,on_delete=models.CASCADE,db_column="user_id")
    class Meta:
        db_table = 'Subscription'

class DefaultSubscription(models.Model):
    plan_name = models.CharField(max_length=128, null=False)
    image_id = models.CharField(max_length=1024, null=True)
    class Meta:
        db_table = 'DefaultSubscription'

class Plan(models.Model):
    field = models.CharField(max_length=256, null=False)
    cycle = models.CharField(max_length=64, null=False)

    default_sub_id = models.ForeignKey(DefaultSubscription, max_length=128, null=False, on_delete=models.CASCADE, db_column='default_sub_id',default='')
    class Meta:
        db_table = 'Plan'
    

 



