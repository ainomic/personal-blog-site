# Generated by Django 4.2.9 on 2024-02-21 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ainomic_blog', '0002_alter_blogs_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogs',
            new_name='Blog',
        ),
    ]
