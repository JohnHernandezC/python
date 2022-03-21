from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='batman.png')
    
    def __str__(self):
        return self.user.username
    
class Post (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    timestamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return f'{self.user.username} : {self.content}'