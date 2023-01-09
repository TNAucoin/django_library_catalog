# Generated by Django 4.1.5 on 2023-01-09 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": [("can_mark_returned", "Set book as returned")],
            },
        ),
    ]
