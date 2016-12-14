from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validate(self, data):
        warnings = []
        if len(data['first_name']) < 2:
            warnings.append('First Name must not have fewer than 2 characters')
        if len(data['last_name']) < 2:
            warnings.append('Last Name must not have fewer than 2 characters')
        if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']) == None:
            warnings.append('Please include a valid email')
        if data['password'] != data['confirm_password']:
            warnings.append('Passwords must match!')
        if len(data['password']) < 8 or len(data['confirm_password']) < 8:
            warnings.append('Passwords must be more than 8 characters')
        if len(warnings) >= 1:
            print warnings
            return (True, warnings)
        else:
            hashed = bcrypt.hashpw(data['password'].encode('UTF-8'), bcrypt.gensalt())
            User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=hashed)
            user = User.objects.last().first_name
            return (False, user)
    def login(self, email, password):
        try:
            user = User.objects.get(email=email)
            return user
        except:
            return False

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
