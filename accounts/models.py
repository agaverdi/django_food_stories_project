from django.db import models
from django.contrib.auth.models import AbstractUser


Gender_Choises = ( 
    ("1", ""), 
    ("2", "male"), 
    ("3", "female"), 
    ("4", "other"),  
)


class CustomUser(AbstractUser):
    user_followings = models.ManyToManyField('self', related_name='followings', )
    friends = models.ManyToManyField('self', related_name='friends', )

    gender=models.CharField(max_length=20, choices=Gender_Choises, default='1')
    image = models.ImageField(upload_to="users/", null=True, blank=True)



    # class Meta:
    #     db_table = 'User'
    #     verbose_name= ("User")
    #     verbose_name_plural= ("User")