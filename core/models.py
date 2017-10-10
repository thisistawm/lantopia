from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=75, blank=True)
    song = models.CharField(max_length=75, blank=True)
    movie = models.CharField(max_length=75, blank=True)
    tv = models.CharField(max_length=75, blank=True)

#def create_todo(sender, **kwargs):
#    user = kwargs["instance"]
#    if kwargs["created"]:
#        user_todo = Todo(user=user)
#        user_todo.save()

class Todo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    unpacked = models.BooleanField(default=False)
    setup = models.BooleanField(default=False)
    connected = models.BooleanField(default=False)

#def create_profile(sender, **kwargs):
#    user = kwargs["instance"]
#    if kwargs["created"]:
#        user_profile = Profile(user=user)
#        user_profile.save()

#post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Todo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.todo.save()


class HomeInfo(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    details = models.TextField(max_length=1000, blank=True)
    nextUp = models.CharField(max_length=200, blank=True)
    post_time = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.post_time = timezone.now()
        self.save()

    def __str__(self):
        return self.headline