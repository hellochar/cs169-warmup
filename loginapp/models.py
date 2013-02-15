from django.db import models
from django.conf import settings

# Create your models here.
class UsersModel(models.Model):
    user = models.CharField(max_length=128, blank=False, primary_key=True)
    password = models.CharField(max_length=128)
    count = models.IntegerField(default=0)

    @staticmethod
    def login(user, password):
        # find user with specified name, check password, increment login count, return accordingly
        try:
            usermodel = UsersModel.objects.get(user=user, password=password)
            usermodel.count += 1
            usermodel.save()
            return usermodel.count
        except UsersModel.DoesNotExist:
            return settings.STATUS_CODES['ERR_BAD_CREDENTIALS']
    

    @staticmethod
    def add(user, password):
        if UsersModel.objects.filter(user=user).exists():
            return settings.STATUS_CODES['ERR_USER_EXISTS']
        
        if user == "" or len(user) > 128:
            return settings.STATUS_CODES['ERR_BAD_USERNAME']
        if len(password) > 128:
            return settings.STATUS_CODES['ERR_BAD_PASSWORD']

        usermodel = UsersModel(user=user, password=password, count=1)
        usermodel.save()
        return usermodel.count

    @staticmethod
    def TESTAPI_resetFixture():
        # reset database
        UsersModel.objects.all().delete()
        return settings.STATUS_CODES['SUCCESS']
