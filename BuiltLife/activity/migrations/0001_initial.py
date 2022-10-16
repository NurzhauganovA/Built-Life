# Generated by Django 4.0.5 on 2022-10-16 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/', verbose_name='Company Logo')),
                ('company_goal', models.CharField(choices=[('Get more visitors', 'Get more visitors'), ('Get more money', 'Get more money'), ('Get more messages', 'Get more messages'), ('Get more likes', 'Get more likes')], max_length=255, verbose_name='Company Goal')),
                ('company_description', models.TextField(blank=True, null=True, verbose_name='Company Description')),
                ('company_email', models.EmailField(max_length=254, verbose_name='Company Email')),
                ('company_phone_number', models.CharField(max_length=255, verbose_name='Company Phone Number')),
                ('company_address', models.CharField(max_length=255, verbose_name='Company Address')),
                ('company_address_second', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Address Second')),
                ('company_city', models.CharField(max_length=255, verbose_name='Company City')),
                ('company_post_code', models.PositiveIntegerField(verbose_name='Company Post Code')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Category name')),
                ('category_cover_image', models.ImageField(upload_to='category_cover_images/', verbose_name='Category Cover Image')),
                ('category_description', models.TextField(blank=True, null=True, verbose_name='Category description')),
                ('category_follow_users', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Are you interested in this category?')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255, verbose_name='Activity Name')),
                ('activity_cover_image', models.ImageField(blank=True, null=True, upload_to='activity_cover_images/', verbose_name='Activity Cover Image')),
                ('activity_description', models.TextField(blank=True, null=True, verbose_name='Activity Description')),
                ('activity_type', models.CharField(choices=[('Personal Activity', 'Personal Activity'), ('Team Activity', 'Team Activity')], max_length=255, verbose_name='Activity Type')),
                ('activity_gender_permissions', models.CharField(choices=[('All', 'All'), ('Male', 'Male'), ('Female', 'Female')], max_length=255, verbose_name='Activity Gender_Permissions')),
                ('activity_age_permissions_lower', models.PositiveIntegerField(default=9, verbose_name='Activity Age Permissions Lower')),
                ('activity_age_permissions_upper', models.PositiveIntegerField(default=25, verbose_name='Activity Age Permissions Upper')),
                ('activity_format', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=255, verbose_name='Activity Format')),
                ('activity_price', models.PositiveIntegerField(default=0, verbose_name='Activity Price')),
                ('activity_price_type', models.CharField(choices=[('Per Hour', 'Per Hour'), ('Per Day', 'Per Day'), ('Per Week', 'Per Week'), ('Per Month', 'Per Month'), ('Per Year', 'Per Year'), ('For Activity', 'For Activity')], max_length=255, verbose_name='Activity Price Type')),
                ('activity_started_date', models.DateField(verbose_name='Activity Started Date')),
                ('activity_duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Activity Duration')),
                ('activity_duration_type', models.CharField(choices=[('Per Day', 'Per Day'), ('Per Week', 'Per Week'), ('Per Month', 'Per Month'), ('Per Year', 'Per Year'), ('Depends on person', 'Depends on person')], max_length=255, verbose_name='Activity Duration Type')),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_category_type', to='activity.category', verbose_name='Category Activation')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_company', to='activity.company', verbose_name='Company Activation')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'db_table': 'activity',
            },
        ),
    ]