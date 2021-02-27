from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Question(models.Model):
    content = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True, upload_to='posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return f"{self.id}: {self.content}"
        
@receiver(post_delete, sender=Question)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
      return f"{self.id}: {self.content} - {self.user.username}"

      