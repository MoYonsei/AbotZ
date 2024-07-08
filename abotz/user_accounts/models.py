from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    gender = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender"]

    class Meta:
        db_table = 'user_accounts_customuser'  # تحديد الاسم الجديد للجدول هنا

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.get_full_name()

class Profile(models.Model):
    user = models.OneToOneField('user_accounts.CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'user_accounts_profile'  # تغيير اسم الجدول هنا إلى الاسم الجديد

    def __str__(self):
        return self.user.username