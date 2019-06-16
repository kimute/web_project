from django.db import models


class Memo(models.Model):
    text = models.TextField()
