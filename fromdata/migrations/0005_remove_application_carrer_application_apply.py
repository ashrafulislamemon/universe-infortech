# Generated by Django 4.0.2 on 2022-02-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fromdata', '0004_alter_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='carrer',
        ),
        migrations.AddField(
            model_name='application',
            name='apply',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]