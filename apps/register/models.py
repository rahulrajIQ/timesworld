from __future__ import unicode_literals
from django.db import models


# create multiple group 
class RoleGroup(models.Model):
    role_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Short title of Role")

    class Meta:
        db_table = 'role_group'

    """
    Four roles are initially created.
    ROLES = (

        ('student', 'student'),
        ('staff', 'staff'),
        ('admin', 'admin'),
        ('editor', 'editor')

    # )
    """



class User(models.Model):
    user_id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null= True)
    mobile = models.CharField(max_length=10, unique=True)
    nationality = models.CharField(max_length=255)

    # ROLES = (

    #     ('student', 'student'),
    #     ('staff', 'staff'),
    #     ('admin', 'admin'),
    #     ('editor', 'editor')

    # )

    # role = models.CharField(max_length=50, choices = ROLES)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'user'


    


# Assign Multiple group to user 
class UserGroup(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='role_group', on_delete=models.CASCADE )
    role_group = models.ForeignKey(RoleGroup, related_name='role_group_name', null = True, blank = True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_role_relation'
    
