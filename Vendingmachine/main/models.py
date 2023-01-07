from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
from django.core.validators import MaxValueValidator, MinValueValidator

class UserManager(BaseUserManager):
  def create_user(self, email, username, password=None, password2=None):
      """
      Creates and saves a User with the given email, username, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          username=username,
         
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, username, password=None):
      """
      Creates and saves a superuser with the given email, username, tc and password.
      """
      user = self.create_user(
          email=email,
          password=password,
          username=username,
          
      )
      user.is_admin = True
      user.save(using=self._db)
      return user


#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  username = models.CharField(max_length=50,unique=True)
  organization_id=models.CharField(blank=True,null=True,max_length=255)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin



class Department(models.Model):
    department_name=models.CharField(max_length=250,null=True,blank=True)
    dep_id=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class Doctors_details(models.Model):
    doctor_name=models.CharField(max_length=250,null=True,blank=True)
    doctor_id=models.CharField(max_length=50,null=True,blank=True)
    department=models.CharField(max_length=250,null=True,blank=True)
    dep_doc_id=models.CharField(max_length=250,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Patient_details(models.Model):
    patient_name=models.CharField(max_length=250, null=True,blank=True)
    doctor_id=models.CharField(max_length=50,null=True,blank=True)
    department_id=models.CharField(max_length=50,null=True,blank=True)
    token=models.CharField(max_length=255,null=True,blank=True)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)





