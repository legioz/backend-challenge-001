from django.db import models


class Role(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=200, null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)


class Claim(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False)
    user = models.ManyToManyField(User)
    

user = Claim.objects.filter(
    'user__name', 
    'user__email', 
    'user__password',
    'user__role__description',
    'description'
).values()
