from django.db import models
from django.utils import timezone

class Note(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    title=models.CharField(max_length=255,blank=False,verbose_name="Title")
    description=models.TextField(blank=False,verbose_name="Description")
    created=models.DateTimeField(auto_now_add=timezone.now(),editable=False)
    updated=models.DateTimeField(auto_now=timezone.now())
    class Meta:
        ordering=("-updated",)

    def __str__(self):
        return "{} - {}".format(self.id,self.title)
    def __unicode__(self):
        return "{}".format(self.id)
