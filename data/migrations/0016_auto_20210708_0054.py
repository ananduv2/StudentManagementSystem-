# Generated by Django 3.2.3 on 2021-07-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20210708_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course_enrolled',
        ),
        migrations.AddField(
            model_name='student',
            name='course_enrolled',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='student',
            name='now_attending',
        ),
        migrations.AddField(
            model_name='student',
            name='now_attending',
            field=models.CharField(max_length=100, null=True),
        ),
    ]