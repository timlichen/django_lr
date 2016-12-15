from __future__ import unicode_literals
<<<<<<< HEAD
=======
import re, bcrypt
>>>>>>> 66e2efd558275a9e996b695afa052b8c89cf1701
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

<<<<<<< HEAD
    objects = UserManager()
=======
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
>>>>>>> 66e2efd558275a9e996b695afa052b8c89cf1701
