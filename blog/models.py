from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    datetime = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.title + ".......by " + self.author

class Comment(models.Model):
    num = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    postnum = models.CharField(max_length=10)
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self): 
        return  "Comment from Post ......" + self.postnum + ".......by " + self.user.username
