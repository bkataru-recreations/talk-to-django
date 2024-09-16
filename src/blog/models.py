from django.db import models
from pgvector.django import VectorField

# Create your models here.

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_LENGTH = 384

class BlogPost(models.Model):
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH, blank=True, null=True)