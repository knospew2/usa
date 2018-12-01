# Generated by Django 2.1.3 on 2018-12-01 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20181130_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=30)),
                ('student_type', models.CharField(choices=[('H', 'High School'), ('C', 'College'), ('G', 'Graduate')], default='C', max_length=1)),
                ('hometown', models.CharField(max_length=128)),
                ('college_town', models.CharField(max_length=128)),
                ('dob', models.DateField()),
                ('hs_grad_year', models.IntegerField()),
                ('college_grad_year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('S', 'Student'), ('A', 'Admin'), ('D', 'Donor')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='student_profile',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.StudentProfile'),
        ),
    ]
