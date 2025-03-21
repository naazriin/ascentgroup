# Generated by Django 5.1.7 on 2025-03-15 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_partner_project_video_contact_is_active_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="banners")),
                ("text", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="partner",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="partner",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="project",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="project",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="project",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="video",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="video",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="video",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
