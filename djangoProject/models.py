from django.db import models


class StringConversionTable(models.Model):
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    max_line_length = models.IntegerField(default=0)
