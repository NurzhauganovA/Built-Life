from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    premium_check = models.BooleanField(default=False)


class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_image = models.ImageField(verbose_name='Profile image', upload_to='profile_images/', blank=True, null=True)
    birthdate = models.DateField(verbose_name='Birth date', blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name='Country', default='Kazakhstan')
    city = models.CharField(max_length=255, verbose_name='City', blank=True, null=True)
    gender = models.CharField(max_length=255, verbose_name='Gender', blank=True, null=True, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255, verbose_name='Phone Number', blank=True, null=True)
    telegram_id = models.CharField(max_length=255, verbose_name='Telegram id', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'Users profile'
        db_table = 'user_profile'