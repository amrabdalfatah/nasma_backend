# Generated by Django 5.1.4 on 2024-12-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pss", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qustionstest",
            name="multichoiceanswer",
            field=models.CharField(
                choices=[
                    ("0", "Never"),
                    ("1", "Almost Never"),
                    ("2", "Sometimes"),
                    ("3", "Fairly Often"),
                    ("4", "Very Often"),
                ],
                max_length=1,
            ),
        ),
    ]
