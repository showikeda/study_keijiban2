from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    # auto_now_add = Trueを指定するとデータが登録されたときの日時を自動的に保存する
    # auto_now = Trueを指定するとデータが更新されたときの日時が自動的に保存される
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
