from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=256, help_text="The name of the thing", null=False, blank=False)
    rank = models.IntegerField(null=True, blank=True)
    # reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse('thing_detail', args=[self.id])