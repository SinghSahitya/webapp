from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_gift_selection_time = models.DateTimeField(null=True, blank=True)

    # other fields and methods for UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Letters(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name