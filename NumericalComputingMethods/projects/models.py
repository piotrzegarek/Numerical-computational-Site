import uuid
from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import FileField
from uuid import uuid4

from django.db.models.fields.related import ForeignKey
from users.models import Profile



# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    # owner = ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(max_length=512, blank=True, null=False)
    excel_file = models.FileField(upload_to='excels')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title