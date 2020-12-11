from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, nick_name, date_of_birth, profile_img=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nick_name=nick_name,
            date_of_birth=date_of_birth,
            profile_img=profile_img,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, nick_name, date_of_birth, profile_img=None):
        user = self.create_user(
            email=email,
            password=password,
            nick_name=nick_name,
            date_of_birth=date_of_birth,
            profile_img=profile_img,
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nick_name = models.CharField(max_length=20, null=False)
    date_of_birth = models.DateField()

    profile_img = models.ImageField(null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick_name', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        