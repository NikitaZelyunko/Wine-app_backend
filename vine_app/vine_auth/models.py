from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
#from django.utils.translation import ugettext_lazy as 
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
 
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True, max_length=255)
    first_name=models.CharField(('first_name'),max_length=30, blank=True)
    last_name=models.CharField(('last_name'),max_length=30, blank=True)
    phone=models.CharField('Phone number', max_length=11, blank=True)
    is_staff=models.BooleanField(
        ('staff_status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    date_joined=models.DateTimeField(('date_joined'), default=timezone.now)

    objects=CustomUserManager()
    
    USERNAME_FIELD='email'
    REQUIRE_FIELD=[]

    class Meta:
        verbose_name=('user')
        verbose_name_plural=('users')
        swappable='AUTH_USER_MODEL'

    def get_full_name(self):
        full_name-'%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)