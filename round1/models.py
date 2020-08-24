from django.db import models

class user(models.Model):
    objects = models.Manager()
    iD_member=models.CharField(max_length=20)
    real_name=models.CharField(max_length=20)
    tz=models.CharField(max_length=20)
    activity_period=models.DateTimeField()

    def __str__(self):
        return self.real_name

