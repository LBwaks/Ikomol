from enum import unique
from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
User = settings.AUTH_USER_MODEL 
from django.urls import reverse
from django.contrib.postgres.indexes import GinIndex
from django_extensions.db.fields import AutoSlugField

class PublishedBlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published =True)
# Create your models here.
def my_slugify_function(content):
    return content.replace('_', '-').lower()

class Tag(models.Model):
    user=models.ForeignKey(User,editable=False,on_delete=models.CASCADE,null=False,related_name='blog_tag_user')
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name' ,slugify_function=my_slugify_function,unique=True)
    description =CKEditor5Field('Text', config_name='extends')
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("blog_tags",kwargs={'slug':self.slug})
class Blog(models.Model):
    user=models.ForeignKey(User,editable=False,on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='title', slugify_function=my_slugify_function,unique=True)   
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='blog_tag')     
    description = CKEditor5Field('Description', config_name='extends')
    photo= models.ImageField(upload_to ='blogs/blog_images/',)    
    is_published = models.BooleanField(default=False)
    
    objects = models.Manager()
    published =PublishedBlogManager()
    
    created_date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog-details", kwargs={"slug": self.slug})

class Comment(models.Model):
    blog = models.ForeignKey("Blog", related_name='comments', on_delete=models.CASCADE,null =False)
    name = models.CharField( max_length=50)
    slug =AutoSlugField(populate_from='name', slugify_function=my_slugify_function, unique=True)
    email = models.EmailField( max_length=254)
    body = CKEditor5Field('Your Comment',config_name='extends')
    is_published =models.BooleanField(default=True)
    created_date = models.DateTimeField( auto_now_add=True)

   
    def __str__(self) :
        return self.name  