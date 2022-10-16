from django.db import models
from account.models import *


class Category(models.Model):
    category_name = models.CharField(verbose_name='Category name', max_length=255)
    category_cover_image = models.ImageField(verbose_name='Category Cover Image', upload_to='category_cover_images/')
    category_description = models.TextField(verbose_name='Category description', blank=True, null=True)
    category_follow_users = models.ManyToManyField(CustomUser, verbose_name='Are you interested in this category?', blank=True, null=True)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'


class Company(models.Model):

    GOAL_CHOICES = (
        ('Get more visitors', 'Get more visitors'),
        ('Get more money', 'Get more money'),
        ('Get more messages', 'Get more messages'),
        ('Get more likes', 'Get more likes')
    )

    company_name = models.CharField(verbose_name='Company Name', max_length=255)
    company_logo = models.ImageField(verbose_name='Company Logo', upload_to='company_logos/', blank=True, null=True)
    company_goal = models.CharField(verbose_name='Company Goal', max_length=255, choices=GOAL_CHOICES)
    company_description = models.TextField(verbose_name='Company Description', blank=True, null=True)
    company_email = models.EmailField(verbose_name='Company Email')
    company_phone_number = models.CharField(verbose_name='Company Phone Number', max_length=255)
    company_address = models.CharField(verbose_name='Company Address', max_length=255)
    company_address_second = models.CharField(verbose_name='Company Address Second', max_length=255, blank=True, null=True)
    company_city = models.CharField(verbose_name='Company City', max_length=255)
    company_post_code = models.PositiveIntegerField(verbose_name='Company Post Code')

    def __str__(self):
        return str(self.company_name) + ' ' + str(self.company_city)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        db_table = 'company'


class Activity(models.Model):

    ACTIVITY_TYPE = (
        ('Personal Activity', 'Personal Activity'),
        ('Team Activity', 'Team Activity')
    )

    GENDER_PERMISSIONS = (
        ('All', 'All'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    ACTIVITY_FORMAT = (
        ('Offline', 'Offline'),
        ('Online', 'Online')
    )

    PRICE_TYPE_ACTIVITY = (
        ('Per Hour', 'Per Hour'),
        ('Per Day', 'Per Day'),
        ('Per Week', 'Per Week'),
        ('Per Month', 'Per Month'),
        ('Per Year', 'Per Year'),
        ('For Activity', 'For Activity')
    )

    DURATION_TYPE_ACTIVITY = (
        ('Per Day', 'Per Day'),
        ('Per Week', 'Per Week'),
        ('Per Month', 'Per Month'),
        ('Per Year', 'Per Year'),
        ('Depends on person', 'Depends on person')
    )

    company_id = models.ForeignKey(Company, verbose_name='Company Activation', on_delete=models.CASCADE, related_name='activity_company')
    category_type = models.ForeignKey(Category, verbose_name='Category Activation', on_delete=models.CASCADE, related_name='activity_category_type')
    activity_name = models.CharField(verbose_name='Activity Name', max_length=255)
    activity_cover_image = models.ImageField(verbose_name='Activity Cover Image', upload_to='activity_cover_images/', blank=True, null=True)
    activity_description = models.TextField(verbose_name='Activity Description', blank=True, null=True)
    activity_type = models.CharField(verbose_name='Activity Type', max_length=255, choices=ACTIVITY_TYPE)
    activity_gender_permissions = models.CharField(verbose_name='Activity Gender_Permissions', max_length=255, choices=GENDER_PERMISSIONS)
    activity_age_permissions_lower = models.PositiveIntegerField(verbose_name='Activity Age Permissions Lower', default=9)
    activity_age_permissions_upper = models.PositiveIntegerField(verbose_name='Activity Age Permissions Upper', default=25)
    activity_format = models.CharField(verbose_name='Activity Format', max_length=255, choices=ACTIVITY_FORMAT)
    activity_price = models.PositiveIntegerField(verbose_name='Activity Price', default=0)
    activity_price_type = models.CharField(verbose_name='Activity Price Type', max_length=255, choices=PRICE_TYPE_ACTIVITY)
    activity_started_date = models.DateField(verbose_name='Activity Started Date')
    activity_duration = models.PositiveIntegerField(verbose_name='Activity Duration', blank=True, null=True)
    activity_duration_type = models.CharField(verbose_name='Activity Duration Type', max_length=255, choices=DURATION_TYPE_ACTIVITY)

    def __str__(self):
        return str(self.activity_name) + '' + str(self.activity_type) + '' + str(self.activity_format)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        db_table = 'activity'