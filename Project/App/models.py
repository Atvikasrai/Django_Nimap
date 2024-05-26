from django.contrib.auth.models import User
from django.db import models


#-------------------------------------------------------------------------------------------------
class Client(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_clients')

    def __str__(self):
        return self.name


#--------------------------------------------------------------------------------------------------
class Project(models.Model):
    name = models.CharField(max_length=60)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')

    def __str__(self):
        return self.name
    

#--------------------------------------------------------------------------------------------------