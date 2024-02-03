from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
    user=models.OneToOneField(User,primary_key='True',on_delete=models.CASCADE)
    # firstname=models.CharField(max_length=30,default='DefaultFirstName')
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],default='DefaultGender')
    # mail=models.CharField(max_length=30,default='DefaultMail')
    # lastname=models.CharField(max_length=30,default='DefaultLastName')
    images=models.ImageField(upload_to='ProfileImages/')
    # userid=models.CharField(primary_key=True, max_length=30)

    
class appointmentdetails(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=45)
    service=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField()
    phoneno=models.IntegerField(default='123')
    workers=models.IntegerField(default='123')
    

    def __str__(self):
      return str(self.name.__str__())

# class login(models.Model):
#     username = models.CharField(max_length=50,unique=True)
#     password = models.CharField(max_length=50)


#     def __str__(self):
#         return str(self.username.__str__())



