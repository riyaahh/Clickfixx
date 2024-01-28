from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30,default='DefaultFirstName')
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],default='DefaultGender')
    mail=models.CharField(max_length=30,default='DefaultMail')
    lastname=models.CharField(max_length=30,default='DefaultLastName')
    # userid=models.CharField(primary_key=True, max_length=30)



    def __str__(self):
        return str(self.userid.__str__())
    
# class login(models.Model):
#     username = models.CharField(max_length=50,unique=True)
#     password = models.CharField(max_length=50)


#     def __str__(self):
#         return str(self.username.__str__())



