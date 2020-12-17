from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, nick_name, date_of_birth, profile_img=None, representation=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nick_name=nick_name,
            date_of_birth=date_of_birth,
            profile_img=profile_img,
            representation=representation,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, nick_name, date_of_birth, profile_img=None, representation=None):
        user = self.create_user(
            email=email,
            password=password,
            nick_name=nick_name,
            date_of_birth=date_of_birth,
            profile_img=profile_img,
            representation=representation,
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
    representation = models.CharField(max_length=10000, null=True)

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
        

class DailyRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    what_kind = models.CharField(max_length=50)
    workout_date = models.DateField('workout date')
    workout_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'what_kind', 'workout_date')
