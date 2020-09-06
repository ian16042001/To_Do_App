from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
