from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length= 255, help_text= "The Name of the Thing", default="Thing")
    rank = models.IntegerField()
    desc = models.TextField(default='Description', blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Our Thing"
        verbose_name_plural = "Our Things"