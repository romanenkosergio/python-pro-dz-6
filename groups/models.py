from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.id
