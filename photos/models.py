from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=150)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["-create"]
