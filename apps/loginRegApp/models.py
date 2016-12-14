from __future__ import unicode_literals
import re, bcrypt
from django.db import models

# Create your models here.
class userManager(models.Manager):
    def validate(self, postData):
        flag = False
        errors = {}
        # info is not blank
        if not postData['f_name'] or not postData['l_name'] or not postData['email'] or not postData['password'] or not postData['c_password']:
            flag = True
            errors['message'] = "All fields must be filled in."
        # passwords match
        if postData['password'] != postData['c_password']:
            errors['message_2'] = "Your passwords don't match."
        # validate email
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            flag = True
            errors['message_3'] = "Please enter a valid email."

        if flag:
            return (flag, errors)
        else:
            hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())

            # Data is clean, ready to be written to database
            User.objects.create(first_name = postData['f_name'], last_name = postData['l_name'], email = postData['email'], password = hashed)

            return(flag, "gratz")

class User(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    email = models.CharField(max_length = 55)
    password = models.CharField(max_length = 100)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = userManager()
