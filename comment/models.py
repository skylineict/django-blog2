from django.db import models
from blogapp.models import Post
from tinymce.models import HTMLField

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(
        Post,  related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    your_comment = HTMLField()
    date = models.DateField(auto_now=True)
    approve_comment = models.BooleanField(default=False)

    def appoved(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.name
