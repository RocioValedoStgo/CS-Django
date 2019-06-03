from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete = models.SET(-1)) #1..*
    address = models.CharField(max_length = 250, null = False) 

    name = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    year = models.IntegerField(null=False)
    img = models.ImageField(upload_to='media/', null=True,blank=True)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)



    def __str__(self):
        return self.img.name

    class Meta:
        db_table = 'Profile'