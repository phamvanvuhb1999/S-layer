from django.db import models


class TimeStampModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modified_time = models.DateTimeField(auto_now_add=True, editable=True, null=True)

    class Meta:
        abstract = True
