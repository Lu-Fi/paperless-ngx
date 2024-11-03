# Generated by Django 5.1.1 on 2024-10-30 04:31

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        (
            "paperless_mail",
            "0027_mailaccount_expiration_mailaccount_account_type_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailaccount",
            name="password",
            field=models.TextField(verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="refresh_token",
            field=models.TextField(
                blank=True,
                help_text="The refresh token to use for token authentication e.g. with oauth2.",
                null=True,
                verbose_name="refresh token",
            ),
        ),
    ]