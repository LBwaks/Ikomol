from email import message
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL 
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
# Create your models here.
periods=[
    ('Day','Day'),
    ('Month','Month'),
    ('Year','Year')
]
speed =[
    ('3 mbps','3 mbps'),
    ('6 mbps','6 mbps'),
    ('12 mbps','12 mbps')
]
types =[
    ('Ostrich','Ostrich'),
    ('Eagle','Eagle'),
    ('Falcon','Falcon')
]
def my_slugify_function(content):
    return content.replace('_', '-').lower()


class Package(models.Model):
    user =  models.ForeignKey(User,editable=False,related_name='user_package',on_delete=models.CASCADE,null=False)
    type =  models.CharField(choices=types,max_length=30)
    price = models.IntegerField()
    slug = AutoSlugField(populate_from='type',slugify_function=my_slugify_function)
    period =models.CharField(choices=periods,max_length=20)
    download_speed = models.CharField(choices=speed,max_length=20)
    sd_movie_music_streaming = models.CharField(max_length=255,blank= True,null=True)
    internet_surfing = models.CharField(max_length=255,blank= True,null=True)
    unlimited_usage = models.CharField(max_length=255,blank= True,null=True)
    hd_tv_shows = models.CharField(max_length=255,blank= True,null=True)
    light_video_downloads =models.CharField(max_length=255,blank= True,null=True)
    heavy_video_downloads =models.CharField(max_length=255,blank= True,null=True)
    multiple_devices =models.CharField(max_length=255,blank= True,null=True)
    online_gaming_live_streams =models.CharField(max_length=255,blank= True,null=True)
    cctv_devices_apability =models.CharField(max_length=255,blank= True,null=True)
    heavy_online_gaming_downloading =models.CharField(max_length=255,blank= True,null=True)

    created_date = models.DateTimeField(auto_now_add=True)



    
    def __str__(self):
        return self.type

class Service(models.Model):
    user = models.ForeignKey(User, editable=False,related_name='services', on_delete=models.CASCADE, null = False)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from ='title', slugify_function = my_slugify_function)
    description = models.TextField()
    photo = models.ImageField(upload_to ='services/',) 
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home")

class SiteDetails(models.Model):
    site_name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField
    twitter =models.URLField()
    instagram =models.URLField()
    facebook = models.URLField
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.site_name
    