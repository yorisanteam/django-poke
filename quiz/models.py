from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'quiz'