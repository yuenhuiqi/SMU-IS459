from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 200)

    my_post = models.ManyToManyField(
        User,
        through='Post',
        through_fields=('topic', 'user'))

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)

    content = models.TextField()
