# from django.core.exceptions import ValidationError
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db.models.fields import EmailField
# # Create your models here.


# class UserManager(BaseUserManager):

#     def create_user(self, email, username, password):
#         email = self.normalize_email(email)
#         if not email:
#             raise ValidationError("Email not provided")
#         if not username:
#             raise ValidationError("No username")
#         user = self.model(
#             email=email,
#             username=username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=email,
#             username=username,
#             password=password
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=120)
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["password", "username"]

#     objects = UserManager()

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True