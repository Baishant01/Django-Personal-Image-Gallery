from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ImagePost(models.Model):
    image = models.ImageField(upload_to='Images/')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    def __str__(self):
        return f"{self.id} by {self.user.username}"
    
    class Meta:
        ordering = ['-id']