from django.db import models




class user(models.Model):
    objects = models.Manager()
    iD_member=models.CharField(max_length=20)
    real_name=models.CharField(max_length=20)
    tz=models.CharField(max_length=20)
    id_int=models.IntegerField(primary_key=True)
    

    def __str__(self):
        return self.real_name


class Activity_period(models.Model):
    objects = models.Manager()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    id_int=models.ForeignKey(user,related_name='activity',on_delete=models.SET_DEFAULT,default=1)

