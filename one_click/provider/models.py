from django.db import models
import uuid


class service(models.Model):
    sid=models.IntegerField(primary_key=True)
    stype=models.CharField(max_length=20)
    sprice=models.FloatField()

    def __str__(self):
        return str(self.stype.__str__())
    

class provider(models.Model):
    pid=models.IntegerField(primary_key=True,)
    pname = models.CharField(max_length=30)
    pcontactno = models.CharField(max_length=12)
    pemail=models.CharField(max_length=40)
    sid=models.ForeignKey(service,on_delete=models.CASCADE)
    pstatus=models.BooleanField()
    pservicetype=models.CharField(max_length=20)
    exp=models.CharField(max_length=40,)
    peducation=models.CharField(max_length=40)
    pDOB=models.DateField()
    pimage=models.ImageField(upload_to='profileimages/')
    password=models.IntegerField(default=1234)
    
    
    def __str__(self):
        return str(self.pname.__str__())
class appointments(models.Model):
    # appid=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.appid.__str__())

class providerpaymentdetails(models.Model):
    payid=models.IntegerField(primary_key=True)
    sid=sid=models.ForeignKey(service,on_delete=models.CASCADE)
    pid=models.ForeignKey(provider,on_delete=models.CASCADE)
    method=models.CharField(max_length=20)
    appid=models.IntegerField()
    amount=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str({self.payid.__str__()}) + "-" + str({self.pid.__str__()})

class editprovider(models.Model):
    name=models.CharField(max_length=20)
    mailid=models.CharField(max_length=30)
    service=models.CharField(max_length=20)
    phone=models.IntegerField()
    experience=models.CharField(max_length=50)
    education=models.CharField(max_length=50)
    dob=models.DateField()
    image=models.ImageField(upload_to='profileimages/')

    def __str__(self):
        return str(self.name.__str__())
