from django.db import models

# Create your models here.



class Category(models.Model):
    caption = models.CharField(max_length=16)

class ArticleType(models.Model):
    caption = models.CharField(max_length=16)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,)
    article_type = models.ForeignKey(to=ArticleType,on_delete=models.CASCADE,)


class FileTest(models.Model):
    src = models.FileField(max_length=32,verbose_name='图片路径',upload_to='static/images')
    title = models.CharField(max_length=32,verbose_name='标题')
    summary = models.CharField(max_length=32,verbose_name='简洁')

    class Meta:
        verbose_name_plural = '图片'
    def __str__(self):
        return self.title