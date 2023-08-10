from django.contrib.auth.models import User 
from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering=('name',)
        #verbose... xac dinh ten so' nhieu thay vi mac dinh categorys
        verbose_name_plural = 'Categories'
    #Hiển thị tên chính nó thay vì là Category Object (1,2,3)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    create_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)#khi user bi xoa thi xoa het item lien quan toi user
    create_at = models.DateTimeField(default=datetime.now,blank=True) #auto_now_add=True
    def __str__(self):
        return self.name
    
    @property
    def imageURl(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url

