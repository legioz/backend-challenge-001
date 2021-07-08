from django.db import models


class Role(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.description}"

    class Meta:
        db_table = 'roles'
        verbose_name = '01 - Roles'
        verbose_name_plural = verbose_name


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=200, null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"{self.id} - {self.email}"

    class Meta:
        db_table = 'users'
        verbose_name = '01 - Users'
        verbose_name_plural = verbose_name


class Claim(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return f"{self.id} - {self.description}"

    class Meta:
        db_table = 'claims'
        verbose_name = '01 - Claims'
        verbose_name_plural = verbose_name
