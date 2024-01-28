from django.db import models

class service(models.Model):
    sid=models.IntegerField(primary_key=True)
    stype=models.CharField(max_length=20)
    sprice=models.FloatField()

    def __str__(self):
        return str(self.stype.__str__())
    

class provider(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30)
    pcontactno = models.CharField(max_length=12)
    pemail=models.CharField(max_length=40)
    sid=models.ForeignKey(service,on_delete=models.CASCADE)
    pstatus=models.BooleanField()
    
    def __str__(self):
        return str(self.pname.__str__())
class appointments(models.Model):
    appid=models.IntegerField(primary_key=True)
    pid=models.ForeignKey(provider,on_delete=models.CASCADE)
    sid=models.ForeignKey(service,on_delete=models.CASCADE)
    cid=models.IntegerField()
    cpayid=models.IntegerField()
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
    