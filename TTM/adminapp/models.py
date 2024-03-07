from django.db import models
class Admin(models.Model):
    id:models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,blank=False,unique=True)
    password=models.CharField(max_length=12,blank=False)
    class Meta:
        db_table="ttmadmin_table"












class Packages(models.Model):
    id=models.AutoField(primary_key=True)
    tourcode=models.CharField(max_length=10, blank=False)
    tourname=models.CharField(max_length=30, blank=False)
    tourpackage=models.CharField(max_length=30, blank=False)
    desc=models.CharField(max_length=35, blank=False)
    class Meta:
        db_table="package_table"

