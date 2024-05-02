# Generated by Django 5.0.4 on 2024-05-02 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='drink',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ratings.category'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dateC',
            field=models.DateField(blank=True, null=True, verbose_name='Date Conclusion'),
        ),
    ]
