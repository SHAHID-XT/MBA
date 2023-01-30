from django.db import models
from django.contrib.auth.models import User


class Recharge(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    taget = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class img(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    img = models.ImageField(
        upload_to='static/profilepictures', null=True)
    def __str__(self):
        return str(self.img)


class Profile(User):
    gender = models.CharField(max_length=10, null=True)
    birthday = models.CharField(null=True, max_length=20)
    country = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    passion = models.CharField(max_length=20, null=True)
    connection = models.CharField(max_length=20, null=True)
    looking = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)


class Rooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="user", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField('Like')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
