from django.db import models
import uuid
from django.contrib.auth.models import User
class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
