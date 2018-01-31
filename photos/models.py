from django.db import models

# Create your models here.
COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSE = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons'),
)

class Photos(models.Model):

    name= models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True,null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3,choices=LICENSE)