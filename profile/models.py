        
from django.db import models

class Images(models.Model):
    image = models.FileField(upload_to = 'media/uploads',null=True)


